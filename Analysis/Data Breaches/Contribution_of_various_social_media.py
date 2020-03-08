#Contribution of various social media platforms to data breaches
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig, ax1 = plt.subplots()

Entity_info = pd.read_excel('sensitivityandyearofbreach.xlsx')['Entity']
Year_info = pd.read_excel('sensitivityandyearofbreach.xlsx')['YEAR']
Records_lost = pd.read_excel('sensitivityandyearofbreach.xlsx')['records lost']
total_records = [sum(Records_lost[Entity_info == 'Facebook']) , sum(Records_lost[Entity_info == 'Instagram']) , sum(Records_lost[Entity_info == "VK"]) ,sum(Records_lost[Entity_info == 'Twitter']),sum(Records_lost[Entity_info == 'LinkedIn']),sum(Records_lost[Entity_info == 'SnapChat'])]
total_records = [i/100000 for i in total_records]

order = ['2012','2013','2016','2017','2018','2019']

vk = (0,0,1005.44934,0,0,0)
linkedin = (80,0,1265,0,0,3800)
fb = (0,60,0,0,790,4190)
twitter = (0,2.5,0,0,3300,0)
sc = (0,47,0,17,0,0)
insta = (0,0,0,60,0,490)


ind = np.arange(len(order))    # the x locations for the groups

p1 = ax1.bar(ind, vk)
p2 = ax1.bar(ind, linkedin, bottom=vk)
p3 = ax1.bar(ind, fb, bottom=(np.array(vk)+np.array(linkedin)))
p4 = ax1.bar(ind, twitter, bottom=(np.array(vk)+np.array(linkedin)+ np.array(fb)))
p5 = ax1.bar(ind, sc, bottom=(np.array(vk)+np.array(linkedin)+ np.array(fb) + np.array(twitter)))
p6 = ax1.bar(ind, insta, bottom=(np.array(vk)+np.array(linkedin)+ np.array(fb) + np.array(twitter)+ np.array(sc)))

# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# ax2.plot([1, 5/3, 0,0, 2, 1, 4/3, 5/3],'--')


ax1.set_ylabel('Records lost in hundred thousands',fontsize = 11)
ax1.set_xlabel('Years',fontsize = 11)
ax1.set_title('Year-wise data breaches distribution',fontsize = 20)
# ax2.set_ylabel('Average Data Sensitivity')
plt.xticks(ind,order)
ax1.set_yticks(np.arange(0, 8480, 1000))
ax1.legend((p1[0], p2[0],p3[0], p4[0],p5[0], p6[0]), ('VK', 'LinkedIn','Facebook', 'Twitter','Snapchat', 'Instagram'),labelspacing = 2,loc='center left', bbox_to_anchor=(1, 0.5),fontsize = 11)
plt.show()

