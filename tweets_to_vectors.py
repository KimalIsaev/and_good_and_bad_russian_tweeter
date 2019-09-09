import pandas as pd
import numpy as np
import pickle
from main_library import from_tweet_to_emoji_vector
from main_library import from_tweet_to_text_vector
from pathlib import Path
from pathlib import PurePath
import os

base_path = os.path.abspath('')

len_of_each_dataset = 50000
dataset_directory = PurePath(base_path, 'initial_dataset')
trained_models_directiory = PurePath(base_path, 'borrowed_model')

whole_pos_csv = pd.read_csv(os.path.join(dataset_directory,"pos.csv"),
                            sep= ';', header = None)[:len_of_each_dataset]
whole_neg_csv = pd.read_csv(os.path.join(dataset_directory,"neg.csv"),
                            sep= ';', header = None)[:len_of_each_dataset]
pos_text = whole_pos_csv.iloc[:,3]
neg_text = whole_neg_csv.iloc[:,3]
print("load files")

pos_text_vectors = pos_text.apply(from_tweet_to_text_vector)
neg_text_vectors = neg_text.apply(from_tweet_to_text_vector)
pos_emoji_vectors = pos_text.apply(from_tweet_to_emoji_vector)
neg_emoji_vectors = neg_text.apply(from_tweet_to_emoji_vector)
print("end of translation")

pos_text_filename = "pos_text_vecs_nonconst_len"
neg_text_filename = "neg_text_vecs_nonconst_len"
pos_emoji_filename = "pos_emoji_vecs_nonconst_len"
neg_emoji_filename = "neg_emoji_vecs_nonconst_len"
processed_dataset_directory = PurePath(base_path, 'processed_dataset')

with open(PurePath(processed_dataset_directory, pos_text_filename), 'wb') as pos_outfile:
    pickle.dump(pos_text_vectors, pos_outfile)
with open(PurePath(processed_dataset_directory, neg_text_filename), 'wb') as neg_outfile:
    pickle.dump(neg_text_vectors, neg_outfile)
with open(PurePath(processed_dataset_directory, pos_emoji_filename), 'wb') as pos_outfile:
    pickle.dump(pos_emoji_vectors, pos_outfile)
with open(PurePath(processed_dataset_directory, neg_emoji_filename), 'wb') as neg_outfile:
    pickle.dump(neg_emoji_vectors, neg_outfile)



