#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json
import urllib.request
import matplotlib.pyplot as plt 


# In[2]:


with urllib.request.urlopen("https://data.cityofnewyork.us/resource/k397-673e.json") as url:
    payroll_info_data = json.loads(url.read().decode())
payroll_info_data


# In[3]:


df = pd.read_json("https://data.cityofnewyork.us/resource/k397-673e.json")
df


# grouping by year of starting agency 

# In[5]:


df['agency_start_date'] = pd.to_datetime(df['agency_start_date']).dt.year
df['agency_start_date']

starting_year = df.groupby(['agency_start_date']).size()
starting_year


# In[4]:


df 


# In[5]:


borough_salary = df.groupby(['work_location_borough','base_salary']).size()
borough_salary


# In[6]:


#base salary

borough_salary_avg_base = df.groupby(['work_location_borough'])['base_salary'].mean()
borough_salary_avg_base


# In[7]:


# gross pay 

borough_salary_avg_gross = df.groupby(['work_location_borough'])['regular_gross_paid'].mean()
borough_salary_avg_gross


# In[8]:


boro = list(df['work_location_borough'].unique())
boro


# In[9]:


cl = ['blue','green','yellow','red','black']

borough_salary_avg_base.plot.bar(color = cl)


# In[16]:


title_des = list(df['title_description'].unique())
title_des


# In[29]:


# base pay
borough_salary_base = df.groupby(['work_location_borough'])['base_salary'].describe()
borough_salary_base


# In[30]:


# gross pay 

borough_salary_gross = df.groupby(['work_location_borough'])['regular_gross_paid'].describe()
borough_salary_gross


# In[31]:


cl = ['blue','green','yellow','red','black', 'brown', 'pink', 'gray']

borough_salary_gross.plot.bar(color = cl)#, ylabel = 'Salary', title = 'General Information for Each Borough')


# In[32]:


cl = ['blue','green','yellow','red','black', 'brown', 'pink', 'gray']

borough_salary_gross['mean'].plot.bar(color = cl), #ylabel = 'Salary', xlabel = ' ', title = 'Average Salary per Borough')


# In[33]:


borough_salary_gross.head()


# In[35]:


plt.boxplot(borough_salary_gross)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
plt.title('Salary Information')
plt.xlabel('General Statistics')
plt.ylabel('Salary')


# In[36]:


x = df.groupby(['work_location_borough'])['regular_gross_paid'].mean()
plt.boxplot(x)
plt.xticks([1], ['Mean'])
plt.title('Salary Information')
plt.xlabel('General Statistics')
plt.ylabel('Salary')


# In[37]:


cl = ['blue','green','yellow','red','black']

borough_salary_gross['mean'].plot.bar(color = cl) #xlabel = 'Borough', ylabel = 'Gross Salary', title = 'Gross Salary in Each Borough')


# In[50]:


jobs_description = df.groupby(['title_description'])['base_salary'].describe()
jobs_description.head()


# In[51]:


del jobs_description['count']
del jobs_description['std']
plt.boxplot(jobs_description)
plt.xticks([1, 2, 3, 4, 5, 6], ['mean', 'min', '25%', '50%', '75%', 'max' ])
plt.title('Jobs Information')
plt.xlabel('General Statistics')
plt.ylabel('Salary')


# In[40]:


jobs_description['mean'].nlargest(n=3)


# In[41]:


jobs_description['mean'].nsmallest(n=3)


# In[42]:


df['ot_rate'] = df['total_ot_paid']/df['ot_hours']
df['ot_rate']


# In[43]:


ot1 = df['ot_rate'].dropna(0)
df['ot_replace'] = df['ot_rate'].replace([np.inf,-np.inf],np.nan)
df['ot_replace']


# In[44]:


df['ot_replace'].mean()


# In[45]:


df.groupby(['work_location_borough'])['ot_replace'].mean()


# In[46]:


df.groupby(['work_location_borough'])['ot_replace'].max()


# In[47]:


u = df.groupby(['title_description'])['ot_replace'].mean()
u.nlargest(n=5)


# In[48]:


t  = df.groupby(['title_description'])['ot_replace'].max()
t.nlargest(n=5)


# In[ ]:




