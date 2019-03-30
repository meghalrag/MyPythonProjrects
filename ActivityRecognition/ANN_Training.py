import json
import codecs
import numpy as np
from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import Perceptron
import pickle


file1_path = "FeatureData.json"
file2_path = "Targets.json"

print('Loading  ' + file1_path + '...')
obj_text = codecs.open(file1_path, 'r', encoding='utf-8').read()
b_new = json.loads(obj_text)
FeaturesAll = np.array(b_new)
print('\nTotal of ' + str(FeaturesAll.shape[0]) + ' files ' + ' with ' + str(FeaturesAll.shape[1]) + ' features each.')

print('Loading  ' + file2_path + '...')
obj_text = codecs.open(file2_path, 'r', encoding='utf-8').read()
target = json.loads(obj_text)
# FeaturesAll = np.array(b_new)
# print(target)

X = FeaturesAll
y = target
# y = [ 0 ,0, 0, 0, 2, 2, 2, 2, 2, 2 ,0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
# print(len(y))
print('Target classes:')
print(y)
print()

# Data Preprocessing
scaler = StandardScaler()

scaler.fit(X)
X = scaler.transform(X)

clf = MLPClassifier(hidden_layer_sizes=(100, ), max_iter=100, alpha=1e-4,
                    solver='sgd', verbose=0, tol=1e-4, random_state=1,
                    learning_rate_init=.1)  #verbose = 1 for verbose
clf.fit(X, y)
print("Training set score: %f" % clf.score(X, y))
print(clf.predict(X[:,:]))
# myMLPClassifier = pickle.dumps(clf)
# p = Perceptron(random_state=42,
#               max_iter=10)
# p.fit(X, y)
#
joblib.dump(clf, 'myMLPClassifier1.pkl')

clf = joblib.load('myMLPClassifier1.pkl')