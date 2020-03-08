#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
popular_topics.py

Generate a bar chart of most popular topics of Mastodon's 30 largest instances

Created on Sat Mar  7 15:21:10 2020

@author: Mohammed Rahman
"""

import json
import matplotlib.pyplot as plt
from nltk.corpus import stopwords 
from collections import Counter

def produce_topics():
    '''
    Plots frequency of most common topic words in largest Mastodon communities
    :return: matplotlib.pychart.barh
    '''
    stop_words = set(stopwords.words('english'))
    with open('./Datasets/Mastodon/mastodon_instance_data.json') as json_file:
        myData = json.load(json_file)
    topics = []
    for i in myData:
        if 'info' in i.keys():
            if i['info'] and 'topic' in i['info']:
                topics.append(i['info']['topic'])
    valid_topics = [i for i in topics if i] 
    keywords = []
    for i in valid_topics:
        words = i.split(", ")
        for word in words:
            keywords.append(word.lower())
    single_keywords = []
    for i in keywords:
        words = i.split()
        for word in words:
            if word not in stop_words: single_keywords.append(word)
    singleCounter = Counter(single_keywords)
    topics = {i[0] : i[1] for i in singleCounter.most_common(30)}
    topicCategory = {
        'Other': int(topics['/']) + int(topics['science']) + int(topics['politics']) + int(topics['queer']) + int(topics['&']) + int(topics['-']) + int(topics['security']),
        'Gaming': int(topics['gaming']) + int(topics['games']),
        'NSFW': int(topics['furry']) + int(topics['porn']),
        'Software': int(topics['software']) + int(topics['development']) + int(topics['web']) + int(topics['programming']),
        'IT': int(topics['tech']) + int(topics['technology']) + int(topics['computer']),
        'General': int(topics['general']) + int(topics['generalistic']) + int(topics['social']) + int(topics['instance']) + int(topics['open']),
        'Media': int(topics['art']) + int(topics['anime']) + int(topics['music']) + int(topics['design']) + int(topics['books'])
    }
    f, ax = plt.subplots(figsize=(8,6)) # set the size that you'd like (width, height)
    plt.barh(*zip(*topicCategory.items()))
    plt.title("Common Mastodon Instance Topics");
    plt.xlabel("Number of instances")
    plt.ylabel("Instance Topics")
    plt.show()