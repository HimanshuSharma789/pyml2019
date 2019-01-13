from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

import matplotlib.pyplot as plt

iris = load_iris()

#  now  splitting  training and testing dataset testing data 10%
split_data1 = train_test_split(iris.data, iris.target, test_size=0.1)
split_data2 = train_test_split(iris.data, iris.target, test_size=0.2)

train_data1, test_data1, train_target1, test_target1 = split_data1
train_data2, test_data2, train_target2, test_target2 = split_data2

features1 = train_data1
label1 = train_target1

features2 = train_data2
label2 = train_target2

regressor = RandomForestClassifier(n_estimators=20, random_state=0)
dsc_clf = tree.DecisionTreeClassifier()
neigh = KNeighborsClassifier(n_neighbors=5)

fit_reg1 = regressor.fit(features1, label1)
fit_reg2 = regressor.fit(features2, label2)

fit_clf1 = dsc_clf.fit(features1, label1)
fit_clf2 = dsc_clf.fit(features2, label2)

fit_knn1 = neigh.fit(features1, label1)
fit_knn2 = neigh.fit(features2, label2)

out_reg1 = fit_reg1.predict(test_data1)
out_reg2 = fit_reg2.predict(test_data2)

out_clf1 = fit_clf1.predict(test_data1)
out_clf2 = fit_clf2.predict(test_data2)

out_knn1 = fit_knn1.predict(test_data1)
out_knn2 = fit_knn2.predict(test_data2)

acc_rf1 = accuracy_score(test_target1, out_reg1)
acc_rf2 = accuracy_score(test_target2, out_reg2)

acc_clf1 = accuracy_score(test_target1, out_clf1)
acc_clf2 = accuracy_score(test_target2, out_clf2)

acc_knn1 = accuracy_score(test_target1, out_knn1)
acc_knn2 = accuracy_score(test_target2, out_knn2)

print(acc_rf1, acc_clf1, acc_knn1)
print(acc_rf2, acc_clf2, acc_knn2)

w = np.arange(3)

plt.bar(w, (acc_rf1, acc_clf1, acc_knn1), 0.25, label="10 %")
plt.bar(w + 0.25, (acc_rf2, acc_clf2, acc_knn2), 0.25, label="20 %")


plt.xticks(w + 0.25 / 2, ("R. Forest", "Desc. Tree", "KNN"))

plt.legend(loc=0)

plt.show()

