#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_map.py

Module to produce heatmap distribution of Mastodon instances around the world

Created on Thu Mar  5 11:58:17 2020

@author: Mohammed Rahman
"""
import gmplot
import pandas as pd

def generate(csv_data):
    '''
    Produces a heatmap distribution based on lat-long coordinates passed into function
    :param data: csv file containing lat-long coordinates
    :type data: str
    
    :return: heatmap
    :rtype: html file 
    '''
    df = pd.read_csv(csv_data)
    latitudes = df["lat"]
    longitudes = df["long"]
    gmap = gmplot.GoogleMapPlotter(0, 0, 2)
    gmap.heatmap(latitudes,longitudes)
    gmap.scatter(latitudes, longitudes, c='r', marker=True)
    gmap.draw("heatmap.html") # Generates html file