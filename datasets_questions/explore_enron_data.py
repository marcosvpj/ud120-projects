#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print('Dataset size:')
print(len(enron_data))

print('Number of features:')
print(len(enron_data.itervalues().next()))


def get_poi(i): return enron_data[i]['poi']


poi = map(get_poi, enron_data)

total_poi = sum(poi)
print('Number of  POI:')
print(total_poi)
