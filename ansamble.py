from data_engineering import get_data
import tensorflow as tf
from collections import Counter
from tensorflow import keras
import os
# from keras.utils import np_utils
import matplotlib.pyplot as plt
import random
import pickle
import json
import numpy as np


def get_networks():
    result_list = []
    newrons_list = os.listdir('models')
    for nn in newrons_list:
        path_nn = os.path.join('models', nn)
        result_list.append(tf.keras.models.load_model(path_nn))
    return result_list

def voting(nn_list, data):
    results_lisst = []
    only_result = []
    for nn in nn_list:
        results_lisst.append(nn.predict(data))
    for i in range(data.shape[0]):
        only_result.append(get_prediction_for_row(i, results_lisst))
    return only_result

def get_prediction_for_row(i, list_of_results):
    result_dict = Counter()
    for result_one in list_of_results:
        for j, x in enumerate(result_one[i]):
            if x == max(result_one[i]):
                result_dict[j] += 1
                break

    return result_dict.most_common(1)[0][0]


# data, values, true_values = get_data()
#
# data = data / 255.
# data = np.reshape(data, data.shape + (1, ))

# nns = get_networks()
#
# voting_res = voting(nn_list=nns, data=data)
#
# for i in range(len(voting_res)):
#     x = voting_res[i]
#     y = values[i]
#     assert 1




