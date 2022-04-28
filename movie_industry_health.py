#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
api = KaggleApi()
api.authenticate()

api.dataset_download_files('danielgrijalvas/movies')

zf = ZipFile('movies.zip')
zf.extractall()
zf.close()

data=pd.read_csv('movies.csv')

data.dropna(subset=['budget', 'gross'], inplace = True)
data


# In[9]:


m=data.groupby('year', as_index=False)['score'].mean()
mean_rating=m['score']
imdbavg = data.groupby(['year']).score.mean()
grossavg = data.groupby(['year']).gross.mean()
genrescore = data.groupby(['genre'], as_index=False).score.mean()
genrelist = data['genre'].unique()
votesavg = data.groupby(['year']).votes.mean()
genregross = data.groupby(['genre'], as_index=False).gross.mean()


# In[10]:


mean_rating=m['score']


# In[11]:


sns.set_theme(style="darkgrid")
plt.figure(figsize=(12,8))
sns.lineplot(data=grossavg)
plt.title('Annual Box Office Gross Revenue',fontsize=15)
plt.xlabel('Year of release',fontsize=15)
plt.ylabel('Gross Revenue In Millions (USD)',fontsize=15)


# In[12]:


plt.figure(figsize=(12,8))
sns.barplot(data=genregross,x="gross",y="genre",palette='rocket')
plt.savefig('RevPerGenre.png')
plt.title('Genre Vs Gross Box Office Revenue',fontsize=15)
plt.xlabel('Gross Revenue In Millions (USD)',fontsize=15)
plt.ylabel('Genre',fontsize=15)


# 
# 

# In[13]:


plt.figure(figsize=(12,8))
sns.kdeplot(data=data, x="year", hue="genre", multiple="stack")
plt.title('Genre Density Plot',fontsize=15)
plt.xlabel('Year',fontsize=15)
plt.ylabel('Density',fontsize=15)


# In[14]:


plt.figure(figsize=(12,8))
sns.relplot(data=data, x="year", y="gross", hue="budget", kind="scatter",height=8,aspect=1.5)
plt.title('Gross Vs Year Relationship Plot',fontsize=15)
plt.xlabel('Year',fontsize=15)
plt.ylabel('Gross Revenue In Billions (USD)',fontsize=15)


# In[15]:


plt.figure(figsize=(12,8))
sns.lineplot(data=votesavg)
plt.savefig('IMDBVotesPerYear.png')
plt.title('Casted Votes Over The Period',fontsize=15)
plt.xlabel('Year',fontsize=15)
plt.ylabel('Votes',fontsize=15)


# In[ ]:




