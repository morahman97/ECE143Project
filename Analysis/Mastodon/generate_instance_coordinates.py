#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_instance_coordinates.py

Module to produce a csv of lat-long coordinates from a dataset containing Mastadon instance data 

Created on Thu Mar  6 11:16:10 2020

@author: Mohammed Rahman
"""

import json
import csv

def generate(loc):
    '''
    Reads in a json dataset on general instance data
    Produces a new lat-long csv by extracting certain fields from the json
    :param loc: string representing directory of dataset
    :type loc: str
    
    :return: csv file with filtered data
    '''
    with open(loc + '/instances_position.json') as json_file:
        data = json.load(json_file)

    with open(loc + '/instance_coordinates.csv', mode="w") as coordinate_file:
        fieldnames = ['instance_name', 'lat', 'long']
        coord_writer = csv.writer(coordinate_file, delimiter=',')
        coord_writer.writerow(fieldnames)
        for key,val in data['Location'].items():
            coord_writer.writerow([key, val['latitude'], val['longitude']])