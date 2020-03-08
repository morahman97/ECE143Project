#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_instance_data.py

Module to produce a csv of lat-long coordinates from a dataset containing Mastadon instance data 

Created on Sat Mar  7 15:21:10 2020

@author: Mohammed Rahman
"""
import requests
import json

def generate(loc):
    '''
    Queries a Mastodon instance API to produce a dataset of instance data
    :param loc: string representing directory of dataset
    :type loc: str
    
    :return: json file with data
    :rtype: None
    '''
    API_KEY = 'Bearer PFZDa2UfyLe3sYTEXpJSQK0MlvbC98rNA1xuRfJ8fugcFGusAs18bRAG4QS8huniY57r863BMJQc0eupoIe7FVYde9D2CT0I3qlXbpmyX3BSR3mXACAAV0VsvlauTkEu'
    params = {'count': '0'}
    r = requests.get('https://instances.social/api/1.0/instances/list', headers={'Authorization': API_KEY}, params=params)
    data = r.json()
    with open(loc + '/mastodon_instance_data.json', 'w') as fp:
        json.dump(data['instances'], fp)