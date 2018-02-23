#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel('salary')
matplotlib.pyplot.xlabel('salary')
matplotlib.pyplot.show()


for point in data_dict:
    if (data_dict[point]['salary'] == 'NaN' or data_dict[point]['bonus'] == 'NaN'):
        continue
    if (data_dict[point]['salary'] >= 1000000 and data_dict[point]['bonus'] >= 5000000):
        print (point, data_dict[point]['salary'], data_dict[point]['bonus'])
