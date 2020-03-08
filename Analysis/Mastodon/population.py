#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
population.py

Generate plot of Mastodon instance growth over time

Created on Sat Mar  7 23:39:10 2020

@author: Mohammed Rahman
"""

import requests
from bs4 import BeautifulSoup
from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)
import matplotlib.pyplot as plt
import numpy as np
from dateutil import parser
import datetime
from matplotlib import pyplot

def generate():
    '''
    Scrapes user population from Dec21 - Feb21 and plots population over time range
    :return: matplotlib.pyplot
    '''
    page = requests.get("https://mastodon.social/@usercount")
    
    # Jan21 - Feb21 
    month_urls = [
        'https://mastodon.social/@usercount?max_id=103694602390963966', 
        'https://mastodon.social/@usercount?max_id=103689883780924791', 
        'https://mastodon.social/@usercount?max_id=103685165214555680', 
        'https://mastodon.social/@usercount?max_id=103680446602988688', 
        'https://mastodon.social/@usercount?max_id=103675492099901149',
        'https://mastodon.social/@usercount?max_id=103670773457462282',
        'https://mastodon.social/@usercount?max_id=103665818984532218',
        'https://mastodon.social/@usercount?max_id=103661100381532409',
        'https://mastodon.social/@usercount?max_id=103656381810918254',
        'https://mastodon.social/@usercount?max_id=103651663207328027',
        'https://mastodon.social/@usercount?max_id=103646944569160563',
        'https://mastodon.social/@usercount?max_id=103642226011790681',
        'https://mastodon.social/@usercount?max_id=103637507390557970',
        'https://mastodon.social/@usercount?max_id=103632788848087295',
        'https://mastodon.social/@usercount?max_id=103628070266274910',
        'https://mastodon.social/@usercount?max_id=103623351614453166',
        'https://mastodon.social/@usercount?max_id=103618633048451426',
        'https://mastodon.social/@usercount?max_id=103613914411443822',
        'https://mastodon.social/@usercount?max_id=103609195839722046',
        'https://mastodon.social/@usercount?max_id=103604241330671845',
        'https://mastodon.social/@usercount?max_id=103599050875028816',
        'https://mastodon.social/@usercount?max_id=103594332292470206',
        'https://mastodon.social/@usercount?max_id=103589613735618922',
        'https://mastodon.social/@usercount?max_id=103584895148913786',
        'https://mastodon.social/@usercount?max_id=103580176685813564',
        'https://mastodon.social/@usercount?max_id=103575457912066306',
        'https://mastodon.social/@usercount?max_id=103570739323126823',
        'https://mastodon.social/@usercount?max_id=103566020762437502',
        'https://mastodon.social/@usercount?max_id=103556347599400212',
        'https://mastodon.social/@usercount?max_id=103551629057326510',
        'https://mastodon.social/@usercount?max_id=103546910469697398',
        'https://mastodon.social/@usercount?max_id=103541955959677959',
        'https://mastodon.social/@usercount?max_id=103537237303648108',
        'https://mastodon.social/@usercount?max_id=103532518968270971',
        'https://mastodon.social/@usercount?max_id=103527564196419894',
        'https://mastodon.social/@usercount?max_id=103522845670962649'
     ]
    
    arr = []
    for url in month_urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        arr += soup.find_all('p')[1:-2]
        
    temp = str(arr[0])[3:-21]
    temp = temp.replace(',', '')
    temp = temp.replace('<br/>+', ' ')
    temp = temp.split()
    res = []
    x = []
    for word in temp:
        if word.isnumeric():
            x.append(int(word))
    res.append(x)
    
    counts = []
    for i in arr:
        entry = str(i)[3:-21].replace(',', '')
        entry = entry.replace('<br/>+', ' ')
        entry = entry.split()
        temp = []
        for word in entry:
            if word.isnumeric():
                temp.append(int(word))
        counts.append(temp)
    #Dec21 - Jan21
    dec_jan_urls = [
        'https://mastodon.social/@usercount?max_id=103522845670962649',
        'https://mastodon.social/@usercount?max_id=103517891083944382',
        'https://mastodon.social/@usercount?max_id=103513172496945696',
        'https://mastodon.social/@usercount?max_id=103508453936400100',
        'https://mastodon.social/@usercount?max_id=103503499415286071',
        'https://mastodon.social/@usercount?max_id=103498780821465892',
        'https://mastodon.social/@usercount?max_id=103494062225838069',
        'https://mastodon.social/@usercount?max_id=103489343599910800',
        'https://mastodon.social/@usercount?max_id=103484625011715090',
        'https://mastodon.social/@usercount?max_id=103479906459695269',
        'https://mastodon.social/@usercount?max_id=103475187846964433',
        'https://mastodon.social/@usercount?max_id=103470469243620824',
        'https://mastodon.social/@usercount?max_id=103465750640808664',
        'https://mastodon.social/@usercount?max_id=103461032085887721',
        'https://mastodon.social/@usercount?max_id=103456313502859063',
        'https://mastodon.social/@usercount?max_id=103451594934745362',
        'https://mastodon.social/@usercount?max_id=103446876294897222',
        'https://mastodon.social/@usercount?max_id=103442157713396205',
        'https://mastodon.social/@usercount?max_id=103437439186473594',
        'https://mastodon.social/@usercount?max_id=103432720511291588',
        'https://mastodon.social/@usercount?max_id=103428001901455306',
        'https://mastodon.social/@usercount?max_id=103423283343841182',
        'https://mastodon.social/@usercount?max_id=103418564770079031',
        'https://mastodon.social/@usercount?max_id=103413138335868183',
        'https://mastodon.social/@usercount?max_id=103408419828131732',
        'https://mastodon.social/@usercount?max_id=103403701200460375',
        'https://mastodon.social/@usercount?max_id=103398982621428080',
        'https://mastodon.social/@usercount?max_id=103394263978263940',
        'https://mastodon.social/@usercount?max_id=103389309506827003',
        'https://mastodon.social/@usercount?max_id=103384590885970418',
        'https://mastodon.social/@usercount?max_id=103379872271920210',
        'https://mastodon.social/@usercount?max_id=103375153656722454',
        'https://mastodon.social/@usercount?max_id=103370435135227696',
        'https://mastodon.social/@usercount?max_id=103365716550863840',
        'https://mastodon.social/@usercount?max_id=103360997919900014',
        'https://mastodon.social/@usercount?max_id=103356279350899309',
        'https://mastodon.social/@usercount?max_id=103351560703587696'
    ]
    counts = counts[::-1]
    dj_arr = []
    for url in dec_jan_urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        dj_arr += soup.find_all('p')[1:-2]
    temp = str(arr[0])[3:-21]
    temp = temp.replace(',', '')
    temp = temp.replace('<br/>+', ' ')
    temp = temp.split()
    res = []
    x = []
    for word in temp:
        if word.isnumeric():
            x.append(int(word))
    res.append(x)
    dj_counts = []
    for i in dj_arr:
        entry = str(i)[3:-21].replace(',', '')
        entry = entry.replace('<br/>+', ' ')
        entry = entry.split()
        temp = []
        for word in entry:
            if word.isnumeric():
                temp.append(int(word))
        dj_counts.append(temp)
    dj_counts = dj_counts[::-1]
    
    y = [j[0] for j in dj_counts] + [i[0] for i in counts]
    x = np.arange(0,len(y),1)
    x = [i/24 for i in x]
    xDays = []
    yDays = []
    i = 0
    while i < len(y):
        xDays.append(int(i/24))
        yDays.append(y[i])
        i += 24
    yDays = [i/1000 for i in yDays]
    start = datetime.datetime.strptime("21-12-2019", "%d-%m-%Y")
    end = datetime.datetime.strptime("20-02-2020", "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
    formatter = DateFormatter('%m/%d/%y')
    fig, ax = plt.subplots(figsize=(8,6))
    ax.xaxis.set_tick_params(rotation=30, labelsize=10)
    plt.title("Mastodon Population Size over Time");
    plt.rcParams.update({'font.size': 14})
    plt.xlabel("Time in Weeks")
    plt.ylabel("Population in Thousands")
    plt.plot_date(date_generated, yDays)
    plt.show()