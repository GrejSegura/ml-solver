import pandas as pd 
import numpy as np 
import os 

from sklearn.model_selection import train_test_split


class CreateDataset:
    def __init__(self, data):
        self.data = data

    def split_data(data):
    # change the target feature name to labels
    dataX = data.drop(['target'], axis = 1)
    dataY = data['target']
    
    # Create train and test dataset
    X_train, x_test, Y_train, y_test = train_test_split(dataX, dataY, random_state = 0)
    return X_train, x_test, Y_train, y_test
