# Visualization of IMDB Data using Python

Authors:  **Aakash Sekar**, **Akshath Dasarathy**, **Meghna Sriram** and **Sureanthar Selvaraj** 



---

## Introduction

IMDb (Internet Movie Database) is an online database that includes cast, production crew, and personal biographies, story summaries, trivia, ratings, and fan and critical reviews for films, television programs, home videos, video games, and streaming entertainment online. IMDb originated as a user-run movie database on the Usenet group "rec.arts.movies," then later, it was brought to the web. IMDb.com, Inc., an Amazon subsidiary, now owns and operates it. We have used this data to make various manipulation and create some meaningful visualizations. 

**Youtube Link:** https://youtu.be/8GHUmIzz-p8
---

## Sources
https://cinemagoer.github.io/

https://www.geeksforgeeks.org/python-programming-language/

https://imdbpy.readthedocs.io/en/latest/

---

## Explanation of the Code
We are using the Cinemagoer API to get data for the Top 250 IMDB movies. With the help of this API we can get data such as Moive Title, ID , Release Year etc
The code begins by importing necessary Python packages like

	
	import seaborn as sns
	import imdb
	import pandas as pd
	import matplotlib.pyplot as plt
	from wordcloud import WordCloud
	


This package does not come pre-installed with anaconda. We used the following syntax to import 
	
	conda install -c anaconda git
 	conda install git pip
	pip install git+https://github.com/cinemagoer/cinemagoer
	conda install -c conda-forge wordcloud
	
	


We then imported top 250 movies data from IMDB API (CinemaGoer) which is stored in 'top'
 	
	top = ia.get_top250_movies()
	

We created an individual list for each movie attribute namely Movie ID, Title, Rank, Ratings, Votes and Year for the Top 250 movies.
 	
	ratings=[]
	for i in range(len(top)):
    	    ratings.append(top[i].data['rating'])

	
Then the above mentioned lists were merged into a DataFrame called top_250. 
	
	top_250['Ratings'] = pd.Series(ratings)
	top_250
	

**Data visualizations** were done on the this

Wordcloud
We created the wordcloud using the titles of top 250 movies from IMDB. The size of each word represents its frequency or relevance in a word cloud, which is a data visualization tool for visualizing text data. The word size is based on the frequency of the reputation of that word in the title. This can be used to find the most used word for the title of the movie in the top 250 movies. 
	
	wordcloud = WordCloud(width = 1000, height = 1000).generate(" ".join(titles))
	

Histogram- Number of movies released per year 
This graph shows that the number of movies released per year among the top 250 movies. We can infer which year has been most successful in terms of producing content. 
	
	sns.histplot(data=top_250['Year'], bins=30,palette='deep',color='red')
	

Line plot
We made a line plot depicting two subplots. 

Subplot 1 : This is a plot of rank vs votes. This plot will explain you how the ranks are plotted with the votes.  If votes are higher in number then usually it will be the most top-ranked but in this case few movies does not follow the same pattern. 

	ax1.plot(top_250['Rank'],top_250['Votes'], color=color)
	
Subplot 2 : This is a plot of rank vs ratings. There is a significant relationship between the ranks and ratings because ratings are one of the highly dependable values for the ranking the movies. 

	ax2.plot(top_250['Rank'], top_250['Ratings'], color=color)
	

For deeper analysis we created a seperate DataFrame consisting of the top 5 movies which contained additional attributes such as Runtime, Country, Language, Gross, Genre.

	top_5['gross']= gross
	top_5['genre']= genre
	

For cleaning the data in the coloumn Gross, we used the following steps to extract the Budget to a seperate coloumn.

	for i in range(len(profit)):
    	    profit[i] = profit[i].split()
	for i in range(len(profit)):
   	    gross_profit[i] = gross_profit[i].split('$')
	

A pie chart was made for this

Pie chart
This pie chart provides the visual representation of the budget of top 5 movies. From this we can infer the production value among the top 5 movies. Among the top 5 movies we can also identify the percentage of budget contribution.

	plt.pie(top_5.Budget,labels = top_5.Titles,autopct='%1.1f%%',explode=[0,0.1,0.2,0.3,0.4],startangle=180)
	

---

## How to Run the Code

1. Open a terminal window.

2. Change directories to where `Assignment#7.py` is saved.

3. Type the following command:
	```
	python Assignment#7.py
	```
---

## Suggestions
If further updates were made available with respect to the API functionalities, we would have been able to extract more attributes of the data which would have helped better vizualization. 
We can further build upon this project by creating an interactive UI for users to play around with.
