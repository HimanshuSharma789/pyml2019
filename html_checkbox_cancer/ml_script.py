from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier

# import numpy as np
import pandas as pd


class ml_script:
    def __init__(self, disease):
        if disease == "diabetes":
            self.file = pd.read_csv("pima-indians-diabetes-deepnet.csv")
        else:
            self.file = pd.read_csv("breast-cancer-wisconsin-data.csv")

        if disease == "diabetes":
            label = self.file['diabetes']
        else:
            label = self.file['breast_cancer']

        features = self.file[self.file.columns[:-1]]

        self.dcs_algo = tree.DecisionTreeClassifier()
        self.knn_algo = KNeighborsClassifier(n_neighbors=5)
        # self.rf_algo = RandomForestRegressor(n_estimators=20, random_state=0)

        # self.trained_rf = self.rf_algo.fit(features, label)
        self.trained_knn = self.knn_algo.fit(features, label)
        self.trained_dcs = self.dcs_algo.fit(features, label)

        # self.f = open("pima-indians-diabetes-deepnet.csv")
        # self.f.readline()  # skip the header
        # self.data = np.loadtxt(self.f, delimiter=",")
        #
        # self.trained_rf = self.rf_algo.fit(self.data[:, :-1], self.data[:, -1])
        # self.trained_dcs = self.dcs_algo.fit(self.data[:, :-1], self.data[:, -1])

    def result(self, info):
        out_dcs = self.trained_dcs.predict([list(info)])
        out_knn = self.trained_knn.predict([list(info)])
        return (out_knn + out_dcs) / 2
