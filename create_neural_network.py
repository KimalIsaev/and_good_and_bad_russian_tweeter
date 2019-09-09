import pickle
import numpy as np
import tensorflow as tf
from pathlib import PurePath
import os
base_path = os.path.abspath('')
processed_dataset = PurePath(base_path, 'processed_dataset')
my_model_directory = PurePath(base_path, 'my_model')

def shuffle_in_unison(a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)

emb_dim = 300
maxlen = 28
batch_size = 32
filters = 500
kernel_size = 12
hidden_dims = 400
epochs = 2

with open(PurePath(processed_dataset, "vecs_const_len"), "rb") as datafile:
    data = pickle.load(datafile)
data_len = len(data)
half_of_data_len = data_len // 2
labels = np.append(np.zeros(half_of_data_len),np.ones(half_of_data_len), axis=0)
shuffle_in_unison(data,labels)

split_point = round(data_len * 0.88)
train_data = data[:split_point]
test_data = data[split_point:]
train_labels = labels[:split_point]
test_labels = labels[split_point:]

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(
        filters,
        kernel_size,
        padding='valid',
        activation='relu',
        strides=1,
        input_shape=(maxlen, emb_dim)),
    tf.keras.layers.GlobalMaxPooling1D(),
    tf.keras.layers.Dense(hidden_dims),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dense(1),
    tf.keras.layers.Activation('sigmoid')
])

model.compile(optimizer='nadam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_data, train_labels,
                    batch_size=batch_size,
                    epochs=epochs,
                    validation_data=(test_data, test_labels))
                                           
id = history.history['accuracy'][-1]
model_structure = model.to_json()
model_name = "cnn{:.2f}".format(id*100)

with open(PurePath(my_model_directory, model_name+".json"), "w") as json_file:
    json_file.write(model_structure)
model.save_weights(os.fspath(PurePath(my_model_directory, model_name+".h5")))
