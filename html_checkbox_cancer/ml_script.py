from sklearn import tree
import numpy as np


class ml_script:
    def __init__(self):
        self.f = open("pima-indians-diabetes-deepnet.csv")
        self.f.readline()  # skip the header
        self.data = np.loadtxt(self.f, delimiter=",")
        self.algo = tree.DecisionTreeClassifier()
        self.trained_algo = self.algo.fit(self.data[:, :-1], self.data[:,-1])

    def result(self, info):
        return self.trained_algo.predict([list(info)])
