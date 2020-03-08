#Contribution of various social media platforms to data breaches
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


Entity_info = pd.read_excel('sensitivityandyearofbreach.xlsx')['Entity']
Year_info = pd.read_excel('sensitivityandyearofbreach.xlsx')['YEAR']
Records_lost = pd.read_excel('sensitivityandyearofbreach.xlsx')['records lost']
N = len(set(list(Entity_info)))
total_records = [sum(Records_lost[Entity_info == 'Facebook']) , sum(Records_lost[Entity_info == 'Instagram']) , sum(Records_lost[Entity_info == "VK"]) ,sum(Records_lost[Entity_info == 'Twitter']),sum(Records_lost[Entity_info == 'LinkedIn']),sum(Records_lost[Entity_info == 'SnapChat'])]
total_records = [i/100000 for i in total_records]

order = ['VK','LinkedIn','Facebook','Twitter','SnapChat','Instagram']
year_2012 = (0, 80, 0, 0, 0,0)
year_2013 = (0, 0, 60, 2.5, 47, 0)
year_2014 = (0, 0, 0, 0, 0, 0)
year_2015 = (0, 0, 0, 0, 0, 0)
year_2016 = (1005.44934, 1265, 0, 0, 0,0)
year_2017 = (0, 0, 0, 0, 17, 60)
year_2018 = (0, 0,790, 3300, 0, 0)
year_2019 = (0, 3800,4190, 0, 0, 490)


ind = np.arange(N)    # the x locations for the groups
# width = N       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, year_2012)
p2 = plt.bar(ind, year_2013, bottom=year_2012)
p3 = plt.bar(ind, year_2014, bottom=(np.array(year_2012)+np.array(year_2013)))
p4 = plt.bar(ind, year_2015, bottom=(np.array(year_2012)+np.array(year_2013)+ np.array(year_2014)))
p5 = plt.bar(ind, year_2016, bottom=(np.array(year_2012)+np.array(year_2013)+ np.array(year_2014) + np.array(year_2015)))
p6 = plt.bar(ind, year_2017, bottom=(np.array(year_2012)+np.array(year_2013)+ np.array(year_2014) + np.array(year_2015)+ np.array(year_2016)))
p7 = plt.bar(ind, year_2018, bottom=(np.array(year_2012)+np.array(year_2013)+ np.array(year_2014) + np.array(year_2015)+ np.array(year_2016) + np.array(year_2017)))
p8 = plt.bar(ind, year_2019, bottom=(np.array(year_2012)+np.array(year_2013)+ np.array(year_2014) + np.array(year_2015)+ np.array(year_2016) + np.array(year_2017)+ np.array(year_2018)))




plt.ylabel('Records lost in hundred thousands')
plt.title('Contribution of various social media platforms to data breaches from 2012 to 2019')
plt.xticks(ind, order)
plt.yticks(np.arange(0, max(total_records), 1000))
plt.legend((p1[0], p2[0],p3[0], p4[0],p5[0], p6[0],p7[0], p8[0]), ('Year 2012', 'Year 2013','Year 2014', 'Year 2015','Year 2016', 'Year 2017','Year 2018', 'Year 2019'))
plt.show()