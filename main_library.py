import numpy as np
from emoji_translator import just_emojis
import zipfile
import os
import re
import gensim
from pathlib import Path
from pathlib import PurePath
from rusvectores_script.rus_preprocessing_udpipe import ultimate_process
emb_dim = 300
base_path = os.path.abspath('')
trained_models_directiory = PurePath(base_path, 'borrowed_model')
path_to_current_model = os.path.join(trained_models_directiory,
                                     "rusvectores_180.zip")
path_to_current_emoji_model = os.path.join(trained_models_directiory,
                                           "emoji2vec.bin")
with zipfile.ZipFile(path_to_current_model, 'r') as archive:
    stream = archive.open('model.bin')
    model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)
emoji_model = gensim.models.KeyedVectors.load_word2vec_format(path_to_current_emoji_model, binary=True)
vse_ne_bukvy = re.compile('[^а-я ]')
def from_tweet_to_text_vector(x):
    temp = x.lower()               #понижает регистр
    #temp =  re.sub('ё', 'е', temp) #заменяет Ё на Е 
    temp =  vse_ne_bukvy.sub('', temp)      #убирает всё кроме букв и пробелов
    return [model[word] for word in ultimate_process(temp) if word in model]

vse_ne_emoji = re.compile('[^\U0001f600-\U0001f650]') 
def from_tweet_to_emoji_vector(x):
    unicode_emoji_lst =  list(vse_ne_emoji.sub('', x)) #оставит только эмоджи
    ascii_emoji_lst = just_emojis(x) #оставит только ascii эмоджи
    emoji_lst = unicode_emoji_lst + ascii_emoji_lst
    return [emoji_model[emoji] for emoji in emoji_lst if emoji in emoji_model]

def to_connect_and_size(text, emoji, text_maxlen, emoji_maxlen):
    return np.append(to_size(text, text_maxlen),
                     to_size(emoji, emoji_maxlen),
                     axis=1)

def to_size(data, maxlen):
    output = []
    for smp in data:
        if smp.size >0:
            output.append(np.append(smp[:maxlen],
                                    np.zeros((max(0, maxlen - len(smp)),
                                              emb_dim)),
                                    axis = 0))
        else: output.append(np.zeros((maxlen - len(smp), emb_dim)))
    return np.array(output)
