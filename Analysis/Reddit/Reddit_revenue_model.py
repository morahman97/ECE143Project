#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def gen_plot():
    
    years = ['2018', '2019', '2020', '2021']
    revenue = [76.9, 119, 181.3, 261.7]

    x = np.arange(len(years))  # the year locations
    width = 0.5  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x , revenue, width)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Million $')
    ax.set_title('Reddit Ad Revenue')
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    #ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(1,0.5),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)

    plt.show()

