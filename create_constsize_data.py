import numpy as np
import pickle
import pandas as pd
from pathlib import PurePath
from main_library import to_connect_and_size
import os
base_path = os.path.abspath('')
processed_dataset = PurePath(base_path, 'processed_dataset')
dataset_length = 50000
half_of_ds_length = dataset_length //2
emb_dim = 300
with open(PurePath(processed_dataset, "pos_text_vecs_nonconst_len"),'rb') as pos_file:      
    pos_text_vectors = pickle.load(pos_file)[:half_of_ds_length]
with open(PurePath(processed_dataset, "neg_text_vecs_nonconst_len"),'rb') as neg_file: 
    neg_text_vectors = pickle.load(neg_file)[:half_of_ds_length]
with open(PurePath(processed_dataset, "pos_emoji_vecs_nonconst_len"),'rb') as pos_file:      
    pos_emoji_vectors = pickle.load(pos_file)[:half_of_ds_length]
with open(PurePath(processed_dataset, "neg_emoji_vecs_nonconst_len"),'rb') as neg_file: 
    neg_emoji_vectors = pickle.load(neg_file)[:half_of_ds_length]  
print("load files")
dataset_length = min(len(neg_emoji_vectors), len(pos_emoji_vectors))

text_vectors = np.append(neg_text_vectors[:dataset_length].apply(np.array).to_numpy(),
                         pos_text_vectors[:dataset_length].apply(np.array).to_numpy(),
                         axis=0)
emoji_vectors = np.append(neg_emoji_vectors[:dataset_length].apply(np.array).to_numpy(),
                          pos_emoji_vectors[:dataset_length].apply(np.array).to_numpy(),
                          axis=0)
print("translated_to_numpy")

with open(PurePath(processed_dataset, "vecs_const_len"), "wb") as datafile: #сделай название отражающие длину
    pickle.dump(to_connect_and_size(text_vectors, emoji_vectors, 14, 14), datafile)
