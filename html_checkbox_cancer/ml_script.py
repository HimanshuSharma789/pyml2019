from sklearn import tree
from sklearn.ensemble import RandomForestRegressor

import numpy as np
import pandas as pd


class ml_script:
    def __init__(self):
        self.file = pd.read_csv("pima-indians-diabetes-deepnet.csv")
        # self.f = open("pima-indians-diabetes-deepnet.csv")
        # self.f.readline()  # skip the header
        # self.data = np.loadtxt(self.f, delimiter=",")
        label = self.file['diabetes']
        features = self.file[self.file.columns[:-1]]

        self.dcs_algo = tree.DecisionTreeClassifier()
        self.rf_algo = RandomForestRegressor(n_estimators=20, random_state=0)

        self.trained_rf = self.rf_algo.fit(features, label)
        self.trained_dcs = self.dcs_algo.fit(features, label)

        # self.trained_rf = self.rf_algo.fit(self.data[:, :-1], self.data[:, -1])
        # self.trained_dcs = self.dcs_algo.fit(self.data[:, :-1], self.data[:, -1])

    def result(self, info):
        out_dcs = self.trained_dcs.predict([list(info)])
        out_rf = self.trained_rf.predict([list(info)])
        return (out_rf + out_dcs) / 2
