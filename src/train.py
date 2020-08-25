import pandas as pd 
import numpy as np 

from dataset import *

data = pd.read_csv(FILE_PATH)

Xtrain, Ytrain, xtest,ytest = CreateDataset(data).split_data()

