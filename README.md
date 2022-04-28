# Reddit Application API 

Authors:  **Vikram Segaran**, **Sai Krishna Reddi**, **Fenil**, **Badru**

---

---

## Introduction
- We are using live data from the application called Reddit.
- Reddit is an American social news aggregation, web content rating, and discussion website. Registered members submit content to the site such as links, text posts,   images, and videos, which are then voted up or down by other members
- We are collecting and saving reddit data using reddit API through praw library
- https://praw.readthedocs.io/en/stable/#getting-started
- The data is updated every time 30 seconds

---

## Sources
- The Praw library website : https://praw.readthedocs.io/en/stable/#getting-started
- We took references from few websites: 
- https://www.geeksforgeeks.org/python-praw-python-reddit-api-wrapper/
- https://www.youtube.com/watch?v=NRgfgtzIhBQ
- https://seaborn.pydata.org/index.html

---

## Explanation of the Code

The code, `reddit_live_data.py`, begins by importing necessary Python packages:
```
import praw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

-Since Praw library does not come preinstalled, we go to command prompt and type - pip install praw

- To test if the instance is running correctly, we type in this code, if it returns true, we are getting live data from reddit

```
reddit = praw.Reddit(client_id=ID,client_secret=API,user_agent=user_name)
print(reddit.read_only)
```

### Exploratory Data Analysis
(Exploratory Data Analysis refers to the process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations)

1. In this graph, we can see the total number of comments in the last year in six different subreddits

![image](https://user-images.githubusercontent.com/98961650/165673261-a83f5694-9799-47b0-8213-922d5222a812.png)


2. Here, we see a scatter plot of the top posts' total number of upvotes and comments in the past year.
This is a subreddit of Python where the majority of the posts range from 750-1000 comments but there are some outliers like a post with around 800 comments, or 2800 likes

![image](https://user-images.githubusercontent.com/98961650/165672794-48d0f15c-6a3c-4229-a604-9c54183cecca.png)

3. In this bar graph, we compare different subreddits based on their current subscriber count

![image](https://user-images.githubusercontent.com/98961650/165673350-db03fabb-8cd2-46d0-8a4f-3ad959173355.png)

4. Importing an instance of live data to a pandas dataframe

![image](https://user-images.githubusercontent.com/98961650/165689590-3f35603f-b7ad-457f-bb95-09c9dbee1b48.png)


5. This is a heatmap of a dataframe containing an instance of live data including subscriber count, upvotes, number of comments etc for a few subreddits
The heatmap shows data correlation, 
For example, we can see that the number of upvotes is positively correlated to awards, meaning, the higher the number of upvotes, the higher the number of awards

![image](https://user-images.githubusercontent.com/98961650/165681155-3936fdc3-a335-4161-a4a9-b075b97cfdfb.png)

## How to Run the Code
- We run the code with ipynb file in a jupyter notebook
- To pull down some real, live reddit posts ,we need create an account and setup credentials
- Once setup, we request API credentials, Reddit uses this information to keep track of who is accessing their data, and in what ways they're accessing it.
- In code,enter client_id,client_secret,username in order to collect data. 

![image](https://user-images.githubusercontent.com/98961650/165678215-4dcf472f-aeaf-4d99-a7d9-d703eecd295f.png)

### Praw Library
To collect, compare, visualize the data, we use praw library.
The Praw library enables us to use various functions to access different data elements in the reddit app.

---

## Suggestions

- With this data, we can predict if a comment is negative or positive using keywords and block the comment
- From the praw library, we can use almost all the features that the app provides, like send a message, ban a person or create a post etc.
- With these features, we can create bots which can automate tasks like sending welcome messages to a subreddit or sending automatic replies

