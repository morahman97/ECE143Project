#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
intersection.py

Generate a venn diagram of overlap in Reddit and Mastodon populations

Created on Sun Mar  8 1:30:20 2020

@author: Mohammed Rahman
"""
import pandas as pd
import numpy as np
import json
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted

def generate():
    '''
    Generate venn diagram of overlap in Reddit and Mastodon populations
    :return: matplotlib_venn.venn2
    '''
    with open('./Datasets/Mastodon/mastodon_instance_data.json') as json_file:
        myData = json.load(json_file)
        
    # I've coded in Python for 3+ years
    # This is the ugliest block I have ever written
    # I am sorry
    
    userTopicDict = dict()
    for i in myData:
        if 'info' in i.keys():
            if i['info'] and 'topic' in i['info']:
                if i['info']['topic'] not in userTopicDict:
                    if i['info']['topic']:
                        for word in i['info']['topic'].split(', '):
                            for splitComma in word.split(','):
                                for singleWord in splitComma.split():
                                    userTopicDict[singleWord.lower()] = int(i['users'])
                else:
                    if i['info']['topic']:
                        for word in i['info']['topic'].split(', '):
                            for splitComma in word.split(','):
                                for singleWord in splitComma.split():
                                    userTopicDict[singleWord.lower()] += int(i['users'])
    
    c = Counter(userTopicDict)
    userTopicCount = c.most_common()
    userTop30 = userTopicCount[:30]
    
#     topics = []
#     for i in myData:
#         if 'info' in i.keys():
#             if i['info'] and 'topic' in i['info']:
#                 topics.append(i['info']['topic'])
#     stop_words = set(stopwords.words('english'))
#     valid_topics = [i for i in topics if i] 
#     keywords = []
#     for i in valid_topics:
#         words = i.split(", ")
#         for word in words:
#             keywords.append(word.lower())
#     single_keywords = []
#     for i in keywords:
#         words = i.split()
#         for word in words:
#             if word not in stop_words: single_keywords.append(word)
#     singleCounter = Counter(single_keywords)
#     topics = {i[0] : i[1] for i in singleCounter.most_common(30)}
    
#     s1 = set(userTopicDict.keys())
#     s2 = set(singleCounter)
#     mastData = []
#     for i in s1.intersection(s2):
#         mastData.append([i,singleCounter[i],userTopicDict[i]])

    r_user_data = pd.read_csv('./Datasets/Reddit/reddit_data_with_user.csv')
    mast_set = set(i[0] for i in c.most_common()[:30])
    reddit_set = set(r_user_data['Subreddit name'])
    inter_set = mast_set.intersection(reddit_set)
    mast_set_counts = set()
    for i in userTop30:
        mast_set_counts.add(i[1])
        
    mast_set_pop = sum(mast_set_counts)
    mast_inter_pop = mast_set_pop
    reddit_set_pop = r_user_data['Number of subscribers'].sum()
    inter_set_pop = 0
    for i in inter_set:
        entry = r_user_data.loc[r_user_data['Subreddit name'] == i]
        inter_set_pop += int(entry['Number of subscribers'])
        for j in userTop30:
            if i == j[0]:
                inter_set_pop += j[1]
                
    plt.figure(figsize=(8,8))
    v = venn2(subsets=(mast_set_pop//1000, reddit_set_pop//1000, inter_set_pop//1000), set_labels = ('', 'Reddit'))
    v.get_patch_by_id('100').set_alpha(1.0)
    v.get_patch_by_id('100').set_color('pink')
    c = venn2_circles(subsets=(mast_set_pop, reddit_set_pop, inter_set_pop),alpha=0.3)
    plt.title("Intersection of Populations (in Thousands)")
    plt.annotate('Unique to Matsodon', xy=v.get_label_by_id('100').get_position() - np.array([0, 0.05]), xytext=(-70,-70),
                 ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='gray'))
    plt.rcParams.update({'font.size': 16})
    plt.show()
    
    plt.figure(figsize=(8,8))
    v = venn2(subsets=(len(mast_set) - len(mast_set.intersection(reddit_set)), 
                       len(reddit_set) - len(mast_set.intersection(reddit_set)), 
                       len(mast_set.intersection(reddit_set))), set_labels = ('Mastodon', 'Reddit'))
    v.get_patch_by_id('100').set_alpha(1.0)
    v.get_patch_by_id('100').set_color('pink')
    c = venn2_circles(subsets = (len(mast_set) - len(mast_set.intersection(reddit_set)), 
                      len(reddit_set) - len(mast_set.intersection(reddit_set)), 
                      len(mast_set.intersection(reddit_set))),
                      alpha = 0.4)
    plt.title("Intersection of Community Topics");
    plt.rcParams.update({'font.size': 14})
    plt.show()
