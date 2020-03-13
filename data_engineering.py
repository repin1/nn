import os
import pickle


def get_data():
    with open(os.path.join('data', 'data.sav'), 'rb') as file:
        data = pickle.load(file)
    with open(os.path.join('data', 'values.sav'), 'rb') as file:
        values = pickle.load(file)
    with open(os.path.join('data', 'true_values.sav'), 'rb') as file:
        true_values = pickle.load(file)

    return data, values, true_values
