                                      Quality of Life in Urban Areas

Authors: Abdul Aziz, Parth Dilip Parmar, Shaunak Shripad Thuse, Swapnil Sanjiv Bambale

Introduction
When it comes to relocating to a new location, there are a few things that everyone considers before leaving their current residence. For some, factors such as quality of education is essential, while for others, safety or a pollution-free environment could be of greater importance.

In order to find those aspects in the given cities (urban areas), we used a data set that includes a list of factors with scores out of 10 and a variable that is a summation of individual score factors and displays the total city score. On this data set, we used visualization techniques and analyzed it for easier decision-making based on certain factors. We felt that these factors were more important for selecting a particular city for relocation. 

Dataset Summary

As we have 17 factors in our data set, our total score is out of 170.
To provide a glimpse of the overall range of urban areas, our first graph depicts ten areas with varying scores. The first three bins represent urban areas with the highest total score, where we see that Singapore tops the list. The next four bins represent the cities with the median total score, and the last three bins represent the areas with the lowest total score, Gibraltar being the lowest.

 

We can use this dataset to select the urban area based on our primary factor of interest, and then select the area with the highest total score to ensure a higher overall quality of living.
Aspect #1 Education 
According to the 'Education Score' Pie Chart, Hong Kong, London, Los Angeles, Boston, and the San Francisco Bay Area are the top five educational destinations. London has the highest total score of these top five cities and is the most desirable city to live in.
 
Aspect #2 Environment Quality 
According to the Clustered Bar Chart of 'Environmental Quality Score' and 'Total City Score,' Fort-Collins, Boulder, Wellington, Madison, and Tartu are the top 5 cities to live in if environmental quality is the most important factor. Boulder has the highest overall score of any of these cities.

 


Sources
The source code came from: Teleport API Explorer
The code retrieves data from: Teleport Public APIS

Explanation of the Code

The code quality_of_life.py begins by importing the following necessary Python packages. 

import pandas as pd
import requests
import json

Instructions for installing packages:
●	Open Command Prompt app 
●	Enter the command “pip install pandas” on the terminal. This should launch the pip installer. The required files will be downloaded
●	Similarly, install requests package using the commands “pip install requests”

The data is then imported from Teleport API Explorer, restructured, and filtered so that we can create the data frame by selecting relevant columns from the available online data set. Total city scores, city names (urban areas), and 17 quality of life factors were the columns of interest. After that, the clean data set was displayed so that its contents could be verified and visually analyzed. 

The following codes were used to implement the above-mentioned:

for s in slug_urb:
  vals = []
  term = 'slug:'+s
  url = 'https://api.teleport.org/api/urban_areas/'+term+'/scores/'
  payload={}
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)
  data = json.loads(response.text)
  try:
    vals.append(s)
    for dd in data['categories']:
      vals.append(dd['score_out_of_10'])

    vals.append(data['teleport_city_score'])
    df.loc[len(df)] = vals
  except KeyError:
    print (s+' not pulled')
    continue

display (df)

Finally, we visualized the data by creating plots focusing on top cities, with a primary focus on safety, environmental quality, cost of living, education, and travel connectivity. Following that, we saved our plot as .png image.

How to Run the Code

1.	Open a terminal window.
2.	Change directories to where quality_of_life.py is saved.
3.	Type the following command:
python quality_of_life.py
Suggestions

The dataset can be used to analyze and identify the most desirable urban areas in terms of quality of life factors. In this assignment, we visualized and used the data set to determine the desirable urban area based on our factor of interest. This dataset in future could also be used to analyze the most suited urban area based on factors such as housing, startups, venture capital, commute, business freedom, safety, healthcare, economy, taxation, internet access, leisure & culture, tolerance, and outdoor space.

YouTube Link

https://youtu.be/ToGTbkj7cK8



