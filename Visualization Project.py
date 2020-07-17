#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_excel('data.xlsx', sheet_name='Total')
data.head()


# In[3]:


#Chart 1 - Percentage of Total ED Visits vs Week
fig=plt.figure(figsize=(15, 5), dpi= 80, facecolor='w')


x1 = data["Week"].astype(str)
y1 = data["Percent_of_Total_Visits_for_CLI"]*100
y2 = data["Percent_of_Total_Visits_for_ILI"]*100        
plt.plot(x1, y1, label = "Percent_of_Total_Visits_for_CLI", marker='o', color='b')
plt.plot(x1, y2, label = "Percent_of_Total_Visits_for_ILI", marker='o', color='orange')

plt.title('Comparsion for Percentage of Visit - CLI vs ILI')
plt.ylabel('Percentage of Total ED Visit')
plt.xlabel('Year / Week')
plt.legend(bbox_to_anchor=(0.65, -0.25))
plt.xticks(x1[::5], rotation=45)

plt.axes().yaxis.grid()


# In[13]:


wdc = pd.read_csv('Weekly_Data_Counts.csv')
wdc.head()


# In[42]:


#Chart 2 - Associated Hospitalization By Age vs Count of Cases

fig=plt.figure(figsize=(15, 5), dpi= 80, facecolor='w')


x1 = wdc["WEEK_NUMBER"]
ind = [x for x, _ in enumerate(x1)]

A = wdc["0-4 YR"]
B = wdc["5-17 YR"]
C = wdc["18-49 YR"]
D = wdc["50-64 YR"]
E = wdc["65+ YR"]

plt.bar(ind, A, width=0.8, label='0-4 YR', color='#CD853F', bottom=B+C+D+E)
plt.bar(ind, B, width=0.8, label='5-17 YR', color='purple', bottom=C+D+E)
plt.bar(ind, C, width=0.8, label='18-49 YR', color='lightskyblue', bottom=D+E)
plt.bar(ind, D, width=0.8, label='50-64 YR', color='royalblue', bottom=E)
plt.bar(ind, E, width=0.8, label='65+ YR', color='indianred')

plt.xticks(ind, wdc["xlabel"], rotation=30)
plt.ylabel("Count of Cases")
plt.xlabel("Calendar Week End (MMWR Week No.)")
plt.legend(loc="upper right")
plt.title("Associated Hospitalization By Age")


plt.show()


# In[59]:


mortality = pd.read_excel('mortality.xlsx')
mortality.head()


# In[ ]:




