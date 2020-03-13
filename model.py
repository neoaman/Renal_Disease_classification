from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
import numpy as np
modelRF = pickle.load(open("FinalRF", 'rb'))

def f_model(input_):
    answer = modelRF.predict([input_])
    return np.squeeze(answer)
