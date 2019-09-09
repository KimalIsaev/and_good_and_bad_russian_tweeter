import numpy as np
import os
import re
import gensim
import pickle
from pathlib import Path
from pathlib import PurePath 
from main_library import from_tweet_to_emoji_vector
from main_library import from_tweet_to_text_vector
from main_library import to_connect_and_size
from tensorflow.keras.models import model_from_json
base_path = os.path.abspath('')
my_model_directory = Path(base_path, 'my_model')
model_lst = [os.fspath(x)[:-5] for x in my_model_directory.glob("*.json")]
model_lst.sort()
name_of_best_model = model_lst[-1]

with open(name_of_best_model + ".json", 'r') as f:
        temp_json_model = f.read()
model = model_from_json(temp_json_model)
model.load_weights(name_of_best_model + '.h5')

def cormit_neuro(stroka):
    text = from_tweet_to_text_vector(stroka)
    emoji = from_tweet_to_emoji_vector(stroka)
    vec = to_connect_and_size(np.array([text]),np.array([emoji]), 14, 14)
    return model.predict(vec)[0][0]

while True:
    print(cormit_neuro(str(input())))
