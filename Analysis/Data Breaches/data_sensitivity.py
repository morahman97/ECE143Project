#Data Sensitivity
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

vk_w = (0,0,4,0,0,0)
linkedin_w = (1,0,1,0,0,2)
fb_w = (0,2,0,0,2,2)
twitter_w = (0,1,0,0,1,0)
sc_w = (0,2,0,1,0,0)
insta_w = (0,0,0,1,0,1)

def zero_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    return [float('nan') if x==0 else x for x in values]

vk = zero_to_nan(vk_w)
linkedin = zero_to_nan(linkedin_w)
fb = zero_to_nan(fb_w)
twitter = zero_to_nan(twitter_w)
sc = zero_to_nan(sc_w)
insta = zero_to_nan(insta_w)

vk_r = (0,0,1005.44934,0,0,0)
linkedin_r = (80,0,1265,0,0,3800)
fb_r = (0,60,0,0,790,4190)
twitter_r = (0,2.5,0,0,3300,0)
sc_r = (0,47,0,17,0,0)
insta_r = (0,0,0,60,0,490)


ind = np.arange(len(order))    # the x locations for the groups


# p1 = ax1.plot(ind, vk_w)
# p2 = ax1.plot(ind, linkedin_w)
# p3 = ax1.plot(ind, fb_w)
# p4 = ax1.plot(ind, twitter_w)
# p5 = ax1.plot(ind, sc_w)
# p6 = ax1.plot(ind, insta_w)

p1_p = ax1.scatter(ind, vk,s=list(vk_r), label = 'VK')
p2_p = ax1.scatter(ind, linkedin,s=list(linkedin_r), label = 'LinkedIn')
p3_p = ax1.scatter(ind, fb,s = list(fb_r), label = 'Facebook')
p4_p = ax1.scatter(ind, twitter,s = list(twitter_r), label = 'Twitter')
p5_p = ax1.scatter(ind, sc,s = list(sc_r), label = 'Snapchat')
p6_p = ax1.scatter(ind, insta,s = list(insta_r), label = 'Instagram')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot([1, 5/3, 2, 1, 4/3, 5/3],'--')


ax1.set_ylabel('Sensitivity of Data',fontsize = 11)
ax1.set_xlabel('Years',fontsize = 11)
ax1.set_title('Data Sensitivity of Data Breached',fontsize = 20)
ax2.set_ylabel('Average Data Sensitivity')
plt.xticks(ind,order)
ax1.set_yticks(np.arange(0, 6, 1))
ax2.set_yticks(np.arange(0, 6, 1))

# plt.gcf().set_size_inches((8, 5))    



# ax1.legend(labelspacing = 4,loc='center left', bbox_to_anchor=(1.1, 0.5))
# ax1.legend((p1[0], p2[0],p3[0], p4[0],p5[0], p6[0]), ('VK', 'LinkedIn','Facebook', 'Twitter','Snapchat', 'Instagram'))
plt.show()

