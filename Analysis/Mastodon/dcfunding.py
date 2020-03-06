#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decentralized_funding.py

Module can be used to analyze funding data saved as a CSV file with similar
format as mastodon_gold_sponsors.csv and mastodon_patreon.csv

Created on Thu Mar  5 11:22:17 2020

@author: Lucas Lin
"""

def ind_platgold(co_sponsors,plotName=None):
    '''Separates company sponsors dataframe into platinum and gold sponsors.
    If plotName, shows and saves stacked hbar as plotName.png.
    
    :param co_sponsors: Dataframe containing companies (follow co_sponsors.csv
                        format)
    :type co_sponsors: pd.DataFrame
    
    :param plotName: Name of hbar plot to be saved.
    :type plotName: str
    
    :return: Industry breakdown of company sponsors
    :rtype: pd.DataFrame
    '''
    import pandas as pd
    import matplotlib.pyplot as plt
    
    assert isinstance(co_sponsors,pd.DataFrame)
    
    gold = co_sponsors.loc[co_sponsors['gp'] == 'g']
    gold = gold['Industry'].value_counts().to_frame()
    gold = gold.rename_axis('Industry')
    gold = gold.rename(columns={'Industry':'gold'})

    platinum = co_sponsors.loc[co_sponsors['gp'] == 'p']
    platinum = platinum['Industry'].value_counts().to_frame()
    platinum = platinum.rename_axis('Industry')
    platinum = platinum.rename(columns={'Industry':'platinum'})

    ind_co_sponsors = gold.join(platinum,how='outer').fillna(0).sort_values(by='platinum',ascending=False).astype(int)
    
    if plotName:
        assert isinstance(plotName,str)
        plt.rc('font', size=20)
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.barh(ind_co_sponsors.index,ind_co_sponsors.gold+ind_co_sponsors.platinum, align='center',color='goldenrod')
        ax.barh(ind_co_sponsors.index,ind_co_sponsors.platinum, align='center',color='lightslategrey')
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Number of sponsors')
        ax.set_title('Mastodon Platinum & Gold Sponsors')
        ax.set_xticks(range(max(ind_co_sponsors.gold+ind_co_sponsors.platinum)+1))
        ax.set_xticklabels(range(max(ind_co_sponsors.gold+ind_co_sponsors.platinum)+1))
        ax.figure.savefig(plotName+'.png')
        plt.show()
    
    return(ind_co_sponsors)

def calc_donations(patrons,total_patrons):
    '''Updates the patrons dataframe to fill in the number of Every Dollar
    Counts Sponsors based on the total number of sponsors and adds a column
    calculating the lower bound of donations for each sponsor level.
    
    :param patrons: dataframe containing data from file formatted like
                    mastodon_patreon.csv
    :type patrons: pd.DataFrame
    
    :param total_patrons: total number of patrons
    :type total_patrons: int
    
    :return: patrons with inserted total_donations column 
                and filled in EDCS
    :rtype: pd.DataFrame
    '''
    
    import pandas as pd
    assert isinstance(patrons,pd.DataFrame)
    assert isinstance(total_patrons,int)
    
    assert total_patrons - patrons['count'].sum() >= 0
    patrons.at[0,'count'] = total_patrons - patrons['count'].sum() #calc number of 'Every dollar counts' patrons
    patrons['count'] = patrons['count'].astype(int) #cast to int
    
    # add column of min donations from each donation level
    patrons['total_donations'] = patrons['min_donation'].multiply(patrons['count'])

    donations_lb = patrons['total_donations'].sum()
    print('total donations per month (lower bound):',donations_lb,sep=' ')
    return(patrons)