from sklearn import tree
# smooth 1 red 100 pred 80
# bumpy 0 orange 150 porange 130

features = [[1,100],[1,80],[0,150],[0,130]]
label = ["apple","apple","orange","orange"]
# calling algo
algo = tree.DecisionTreeClassifier()

#training the algo
trained_algo = algo.fit(features, label)
print(trained_algo.predict([[1,110]]))
