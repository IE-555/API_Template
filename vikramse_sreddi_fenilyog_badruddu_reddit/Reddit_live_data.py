#!/usr/bin/env python
# coding: utf-8

# In[1]:


import praw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1)the first thing is go to reddit and create a reddit account
#https://www.reddit.com/
#2) create a reddit app. Make sure you're signed in to your reddit account,then go to the app page
#From here, click on the "create an app" button. Make sure that you've selected the "script" option in the checkbox,
#fill in a name and description. 
#For the two URL fields, it doesn't really matter what you put.
#https://ssl.reddit.com/prefs/apps/


# In[2]:


#To pull down some real, live reddit posts ,we need some information from our app. 
#Reddit uses this information to keep track of who is accessing their data, and in what ways they're accessing it.
#In code,enter client_id,client_secret,username in order to collect data. 
ID = 'hiXdCt4qu-t4LOSYPQbOeg'
user_name = "Certain_Extension734"
API = 'dTismPVgY7H3fttQnRWYuHLEDhEP-w'


# In[3]:


# This line calls a function in the praw library.
# That function sets up to easily make calls to the reddit API moving without
# having to enter this information every time we make a call
reddit = praw.Reddit(client_id=ID,client_secret=API,user_agent=user_name)


# In[4]:


#To test if instance is working
print(reddit.read_only) # Output: True


# In[79]:


#Random post from subreddit "AskReddit"
# Make sure to use the subreddit name correctly,it should be same name,format as in reddit app
random_post = reddit.subreddit("AskReddit").random()
print(random_post.title)


# In[80]:


#Top 10 posts in  fron the subreddit "Buffalo"
for posts in reddit.subreddit("Buffalo").hot(limit=10):
    print(posts.title)


# In[82]:


#Graph of total number of comments for 10 posts in each subreddit, 
#subreddits=['Python','Cooking','Onepiece','Damnthatsinteresting','programming']
a1=0
for submission in reddit.subreddit("Python").top('year',limit=10):
    a1=submission.num_comments+a1
# Make sure to use the num_comments name as it is to get the number of comments
     
a2=0
for submission in reddit.subreddit("Cooking").top('year',limit=10):
    a2=submission.num_comments+a2

     
a3=0
for submission in reddit.subreddit("Onepiece").top('year',limit=10):
    a3=submission.num_comments+a3
     
a4=0
for submission in reddit.subreddit("Damnthatsinteresting").top('year',limit=10):
    a4=submission.num_comments+a4
     
a5=0
for submission in reddit.subreddit("programming").top('year',limit=10):
    a5=submission.num_comments+a5
     
a6=0
for submission in reddit.subreddit("CryptoCurrency").top('year',limit=1):
    a6=submission.num_comments+a6
     

x1=[a1,a2,a3,a4,a5,a6]
x2=['Python','Cooking','Onepiece','Damnthatsinteresting','programming','CryptoCurrency']

plt.bar(x2, x1)
plt.ylabel('Total Number of comments')
plt.xticks(rotation = 45,verticalalignment='top',horizontalalignment='right')
plt.text(x2[0],a1,a1,ha="center",va="bottom")
plt.text(x2[1],a2,a2,ha="center",va="bottom")
plt.text(x2[2],a3,a3,ha="center",va="bottom")
plt.text(x2[3],a4,a4,ha="center",va="bottom")
plt.text(x2[4],a5,a5,ha="center",va="bottom")
plt.text(x2[5],a6,a6,ha="center",va="bottom")
plt.show()


# In[55]:


#'subreddit_subscribers'
subreddits = ['Jokes','Onepiece', 'travel', 'books',  'gaming']
l =[]
for sr in subreddits:
    a1 = 0
    for post in reddit.subreddit(sr).top('year',limit=1):
        a1=post.subreddit_subscribers

# Make sure to use the subreddit_subscribers name as it is to get the number of subscribers
    l.append(a1)
plt.bar(subreddits, l)
plt.ylabel('Total Number of Subscribers')
plt.xlabel('subreddits')
plt.xticks(rotation = 45,verticalalignment='top',horizontalalignment='center')
for i in range(5):
    plt.text(subreddits[i],l[i],l[i],ha="center",va="bottom")
plt.show()


# 

# In[106]:


subreddits = ['Jokes','Onepiece', 'travel', 'books',  'gaming']


s =[]
for sr in subreddits:

    for submission in reddit.subreddit(sr).top('year',limit=5):
        s.append([submission.title,submission.url,submission.subreddit_name_prefixed,submission.selftext,submission.over_18,
                  submission.subreddit_subscribers,submission.ups,submission.num_comments,
                  submission.upvote_ratio,submission.total_awards_received,submission.author.name])
# we put number of posts limit =5 , because it takes time to run code
# the other data we can get = [ 'created_utc', 
                     #'is_crosspostable', 'is_self', 'is_video', 'locked', 'media_only', 'over_18',
                     #'subreddit_id', 'subreddit_name_prefixed', 'subreddit_subscribers', 
                     #'title', 'permalink', 
                     #'total_awards_received', 'downs','gilded','num_comments', 'num_crossposts', 'num_reports', 
                     #'ups']
# Make sure to use the title,ups,url,subreddit_name_prefixed,subreddit_name_prefixed,num_comments.....
#.....all names exactly as mentioned in above comment
s = pd.DataFrame(s,columns=['title',  'url','subreddit_name_prefixed','body','Over 18',
                            'subreddit_subscribers','Upvotes','num_comments','upvote_ratio','Awards',
                             'author_name'])

s


# In[107]:


s.corr()
#corel
#The correlation coefficient is a statistical measure of the strength of the relationship between 
#the relative movements of two variables. The values range between -1.0 and 1.0
#A value of exactly 1.0 means there is a perfect positive relationship between the two variables.
#For a positive increase in one variable, there is also a positive increase in the second variable.
#A value of -1.0 means there is a perfect negative relationship between the two variables.
#This shows that the variables move in opposite directions—for a positive increase in one variable, there is a decrease in the second variable. 
#The strength of the relationship varies in degree based on the value of the correlation coefficient. 
#Analysts in some fields of study do not consider correlations important until the value surpasses at least 0.8.


# In[108]:


corr = s.corr()
#A heatmap is a graphical representation of data where each value of a matrix is represented as a color. 
f, ax = plt.subplots(figsize=(11, 9))
sns.heatmap(corr)


# In[86]:


#
x3=[]
x4=[]
for submission in reddit.subreddit("Python").top('year'):
    x3.append(submission.score)
for submission in reddit.subreddit("Python").top('year'):
    x4.append(submission.num_comments)
plt.ylabel('Number of comments in posts')
plt.xlabel('Score of posts')

sns.scatterplot(x=x3,y=x4)
plt.show()


# In[ ]:




