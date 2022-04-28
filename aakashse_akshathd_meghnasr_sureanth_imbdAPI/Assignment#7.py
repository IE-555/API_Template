#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Installing git for anaconda
conda install -c anaconda git


# In[ ]:


#Installing git pip
conda install git pip


# In[ ]:


# Installing CinemaGoer API
pip install git+https://github.com/cinemagoer/cinemagoer


# In[ ]:


#Installing WordCloud
conda install -c conda-forge wordcloud


# In[1]:


#Importing Essential Libraries
import seaborn as sns
import imdb
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# In[2]:


#Creating an instance of the cinemagoer class
ia = imdb.Cinemagoer()


# In[3]:


#Getting the Top250 Movie Data
top = ia.get_top250_movies()
top


# In[4]:


# Manipulating the dataset 
titles =[]
x=0
i=0
runtimes=[]
for i in range(250):
    x = top[i]['title']
    titles.append(x)
    i=i+1


# In[5]:


id =[]
for i in range(len(titles)):
    id.append(top[i].getID())


# In[6]:


years=[]
for i in range(len(titles)):
    years.append(top[i].data['year'])


# In[7]:


ratings=[]
for i in range(len(top)):
    ratings.append(top[i].data['rating'])


# In[8]:


votes=[]
for i in range(len(top)):
    votes.append(top[i].data['votes'])


# In[9]:


rank=[]
for i in range(len(top)):
    rank.append(top[i].data['top 250 rank'])


# In[10]:


#Creating the DataSet
top_250 = pd.DataFrame()


# In[11]:


#Manupulating the DataSet
top_250['Movie ID'] = id 


# In[12]:


top_250['Titles'] = pd.Series(titles)


# In[13]:


top_250['Rank'] = pd.Series(rank)


# In[14]:


top_250['Ratings'] = pd.Series(ratings)


# In[15]:


top_250['Votes'] = pd.Series(votes)


# In[16]:


top_250['Year'] = pd.Series(years)


# In[17]:


top_250


# ## Visualization

# In[18]:


#Creating Plots from DataSet - WordCloud
wordcloud = WordCloud(width = 1000, height = 1000).generate(" ".join(titles))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[19]:


#Histogram 
sns.histplot(data=top_250['Year'], bins=30,palette='deep',color='red')
plt.title("Number of movies per Year")
plt.savefig('Wordcloud.png')
plt.show()


# In[20]:


#LinePlot with 2 Subplots
fig, ax1 = plt.subplots(figsize=(15,15))

color = 'tab:red'
ax1.set_xlabel('Ranks')
ax1.set_ylabel('Votes', color=color)
ax1.plot(top_250['Rank'],top_250['Votes'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax1.set_title("Rank Vs Votes Vs Ratings")
color = 'tab:green'
ax2.set_ylabel('Ratings', color=color)  # we already handled the x-label with ax1
ax2.plot(top_250['Rank'], top_250['Ratings'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig("Rank Vs Votes Vs Ratings")
plt.show()


# In[21]:


#Creating DataFrame for Top 5 Movies
top5_id = top_250['Movie ID'].head(5)

code=[]
title=[]
rating=[]
runtimes=[]
country=[]
votes=[]
lang=[]
year=[]
composer=[]
gross=[]
genre=[]

code = "0111161"
  
# getting information
series1 = ia.get_movie(code)
  
# getting rating of the series
rating.append(series1.data['rating'])
  

#print the runtimes
runtimes.append(series1.data['runtimes'])


#print the countries
country.append(series1.data['countries'])


#print the votes
votes.append(series1.data['votes'])


#print the lang
lang.append(series1.data['languages'])


#print the year
year.append(series1.data['year'])


genre.append(series1.data['genres'])


gross.append(series1.data['box office'])


# In[22]:



code = "0068646"
  
# getting information
series1 = ia.get_movie(code)
  
# getting rating of the series
rating.append(series1.data['rating'])
  

#print the runtimes
runtimes.append(series1.data['runtimes'])


#print the countries
country.append(series1.data['countries'])


#print the votes
votes.append(series1.data['votes'])


#print the lang
lang.append(series1.data['languages'])


#print the year
year.append(series1.data['year'])


genre.append(series1.data['genres'])


gross.append(series1.data['box office'])


# In[23]:



code = "0468569"
  
# getting information
series1 = ia.get_movie(code)
  
# getting rating of the series
rating.append(series1.data['rating'])
  

#print the runtimes
runtimes.append(series1.data['runtimes'])


#print the countries
country.append(series1.data['countries'])


#print the votes
votes.append(series1.data['votes'])


#print the lang
lang.append(series1.data['languages'])


#print the year
year.append(series1.data['year'])


genre.append(series1.data['genres'])


gross.append(series1.data['box office'])


# In[24]:



code = "0071562"
  
# getting information
series1 = ia.get_movie(code)
  
# getting rating of the series
rating.append(series1.data['rating'])
  

#print the runtimes
runtimes.append(series1.data['runtimes'])


#print the countries
country.append(series1.data['countries'])


#print the votes
votes.append(series1.data['votes'])


#print the lang
lang.append(series1.data['languages'])


#print the year
year.append(series1.data['year'])


genre.append(series1.data['genres'])


gross.append(series1.data['box office'])


# In[25]:



code = "0050083"
  
# getting information
series1 = ia.get_movie(code)
  
# getting rating of the series
rating.append(series1.data['rating'])
  

#print the runtimes
runtimes.append(series1.data['runtimes'])


#print the countries
country.append(series1.data['countries'])


#print the votes
votes.append(series1.data['votes'])


#print the lang
lang.append(series1.data['languages'])


#print the year
year.append(series1.data['year'])

genre.append(series1.data['genres'])

gross.append(series1.data['box office'])


# In[26]:


#Manipulating the DataFrame
top_5 = pd.DataFrame()


# In[27]:


top_5['Movie ID'] = top5_id


# In[28]:


top_5['Titles'] = top_250['Titles'].head(5)


# In[29]:


top_5['runtimes'] = runtimes


# In[30]:


top_5['Country']= country


# In[31]:


top_5['Votes'] = votes


# In[32]:


top_5['language']= lang


# In[33]:


top_5['year'] = year


# In[34]:


top_5['gross']= gross
top_5['genre']= genre


# In[35]:


top_5


# In[36]:


#Handling the data for the Pychart Visualization
profit=[]
for i in range(len(gross)):
    profit.append(gross[i].get('Budget'))


# In[37]:


for i in range(len(profit)):
    profit[i] = profit[i].split()


# In[38]:


gross_profit=[]
for i in range(len(profit)):    
    gross_profit.append(profit[i][0])


# In[39]:


for i in range(len(profit)):
    gross_profit[i] = gross_profit[i].split('$')


# In[40]:


gp=[]
for i in range(len(gross_profit)):    
    gp.append(gross_profit[i][1].replace(',',''))


# In[41]:


for i in range(len(profit)):
    gp[i]=int(gp[i])


# In[42]:


top_5['Budget'] = gp


# In[43]:


top_5


# In[44]:


#PyChart 
plt.pie(top_5.Budget,labels = top_5.Titles,autopct='%1.1f%%',explode=[0,0.1,0.2,0.3,0.4],startangle=180)
plt.title("Top5 Budget")
plt.axis("equal")
plt.savefig("Top5_Budget.png")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




