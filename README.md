# Write a Brief Descriptive Title Here

Authors:  Somit Desai , Sumanth Reddy, Vineeth Reddy Tati and Anirudh Varma

---


---

## Introduction
*The purpose of this section is to provide some information about the data you're exploring.  For example, you should*
- We import F1 race data in .JSON format. 
- The data is fetched using requests from [F1 MRD Repo](http://ergast.com/mrd/)  
- This data is very recent and is updated every race.

---

## Sources
*In this section, provide links to your references.  For example:*
- The code retrieves data from [F1 MRD Repo](http://ergast.com/mrd/)
- Numpy documentation [Documentation](https://numpy.org/doc/stable/index.html)
- Plotly documentation [Documentation](https://plotly.com/python/)

---

## Explanation of the Code
*In this section you should provide a more detailed explanation of what, exactly, the above code actually does.  Your classmates should be able to read your explanation and understand what is happening in the code.*

The code, `vineethr_syeruva_somitdes_apenumet_f1data.py`, begins by importing necessary Python packages:
```
import requests
import numpy as np
import plotly.graph_objects as go
```

Plotly can be installed through PIP with the following command:
```
pip install plotly
```

We then import data from [insert name of data source].  We print the data to allow us to verify what we've imported:
```
x = [1, 3, 4, 7]
y = [2, 5, 1, 6]

for i in range(0,len(x)):
	print "x[%d] = %f" % (i, x[i])		
```
- *NOTE 1:  This sample code doesn't actually import anything.  You'll need your code to grab live data from an online source.*  
- *NOTE 2:  You will probably also need to clean/filter/re-structure the raw data.  Be sure to include that step.*

We then use requests to fetch data from the online data repo:
```
my_base_url = "http://ergast.com/api/f1/" + str(temp_year) + "/1/results.json"
response = requests.get(my_base_url)
data = response.json()['MRData']['RaceTable']['Races'][0]
```

The data then needs to be filtered and sepearated into useful data before we start visualizing it. This is done with the help of 
Numpy:

```

first = np.array(first_raw)
second = np.array(second_raw)
third = np.array(third_raw)

first_unique, first_counts = np.unique(first, return_counts=True)
second_unique, second_counts = np.unique(second, return_counts=True)    
third_unique, third_counts = np.unique(third, return_counts=True)
```

Finally, we visualize the data.  We save our plot as a `.png` image:
```
plt.plot(x, y)
plt.savefig('samplefigure.png')	
plt.show()
```

The output from this code is shown below:

![Image of Plot](images/graph.png)

---

## How to Run the Code
*Provide step-by-step instructions for running the code.  For example, I like to run code from the terminal:*
1. Open a terminal window.

2. Change directories to where `vineethr_syeruva_somitdes_apenumet_f1data.py` is saved.

3. Type the following command:
	```
	python vineethr_syeruva_somitdes_apenumet_f1data.py
	```

- *NOTE: You are welcome to provide instructions using Anaconda or IPython.*

---

## Suggestions
*Finally, you should suggest any additional features that would be useful/interesting.  For example, what else could you do with these data?  How might you want to modify the plot to be more descriptive?  What summary statistics might you want to calculate with these data?*
