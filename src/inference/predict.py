import pandas as pd
import numpy as np
import pickle


# df = pd.read_csv('../dataset/TestFile.csv')
# print(df.head())


class NotePredictor:

    def __init__(self):
        self.pickle_in = open("../training/note_classifier.pkl", "rb")
        self.classifier = pickle.load(self.pickle_in)

    def predict(self, variance, skewness, curtosis, entropy):
        result = self.classifier.predict([[variance, skewness, curtosis, entropy]])
        print(result)


nap = NotePredictor()
nap.predict(1.0552, 1.1857, -2.6411, 0.11033)