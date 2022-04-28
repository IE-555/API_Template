#!/usr/bin/env python
# coding: utf-8

# # VISUALIZATION AND ANALYSIS OF NYC EV FLEET STATION NETWORK
# 
# > **Team Members: Priyanka Rajendra Bhoite, Siva Shankar Paramasivan, Sanath Viswanathan Srinivas, Srikant Jayasankaran** 
# 

# # 1. INTRODUCTION
# 
# ## 1.1 ABOUT THE DATA
# 
# **The data is extracted from NYC Open Data. It contains information about the EV charging station network in NYC.**
# 
# ## 1.2 OBJECTIVE
# 
# **Charging infrastructure expansion is inevitable if the government's goal of a 50% electric car market share in new vehicle registrations by 2030 is to be met. The goal is to analyze the current fleet charging network in New York City and provide insights for future upgrades in EV infrastructure.**
# 
# 

# # 2. SOURCES
# 
# - **Dataset Provider : Department of Citywide Administratie Services (DCAS)**
# 
# - **Dataset Owner    : NYC OpenData**
# 
# - **Source Link      : https://data.cityofnewyork.us/City-Government/NYC-EV-Fleet-Station-Network/fc53-9hrv**
# 
# - **API Endpoint     : https://data.cityofnewyork.us/resource/fc53-9hrv.json**
# 
# *We obtained the source from NYC OpenData. Extracted the data into python from API source given in the website*
# 
# **Note:** Please refer the above link for more detailed description of the data columns and rows. 

#  # 3. PYTHON SCRIPT DESCRIPTION
# 
# 

# In[1]:


#Make sure to intall the following 
#pip install sodapy
#pip install plotly
#pip install folium

#Importing the required python libraries

import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import calendar
import json
import pandas as pd
import numpy as np
import folium
from sodapy import Socrata


# In[2]:



# authenticated client credentials required for importing dataset directly from the website 

# Created a profile in socrato and obtained the following credentials - MyAppToken, username, password

MyAppToken="nV7b3BBToUr5rNMY1hHDOXQzC"
client = Socrata("data.cityofnewyork.us",
                  MyAppToken,
                  username="sureshsanath@gmail.com",
                  password="cat@1200")

# Data returned as JSON from API and converted to Python dictionary by sodapy
results = client.get("fc53-9hrv")

# Converting dictionaries to pandas DataFrame
evfleet_df = pd.DataFrame.from_records(results)

# Data Cleaning - Removed null values using dropna()
evfleet_df = evfleet_df.dropna()

# Converting variable's data types as required
evfleet_df = evfleet_df.astype({'no_of_ports': np.int64})
evfleet_df = evfleet_df.astype({'census_tract': np.int64})

evfleet_df.head()


# ##  3.1 VISUALIZATION
# 
# The data extracted in the previous steps are used to visualize, analyze the Electric Vehicle Fleet stations in New York City

# ### 3.1.1 Analyzing Charging Station location in NYC
# 
# The EV fleet charging stations are densely located in NYC. To understand these locations of charging stations in each borough, a density plot is being plotted. We can analyze if these locations of charging stations are optimally located for effective usage based on population in each borough.

# In[3]:


# plotting location data points of all charging stations as a scatterplot in a map using scattergeo() in plotly library

g1 = go.Figure(go.Scattergeo()) 
fig1 = px.density_mapbox(evfleet_df,lat='latitude',lon='longitude',radius=4,hover_data=["agency","borough"],zoom=9.5,center=dict(lat=40.7,lon=-74),mapbox_style="carto-positron")
fig1.update_layout(margin={"r":0,"t":1,"l":0,"b":0})
fig1.update_layout(title={'text':"DENSITY PLOT FOR CHARGING STATION'S LOCATIONS IN NYC",'y':0.12,'x':0.35,'xanchor':'left','yanchor':'bottom'})
config = dict({'scrollZoom': False}) 
fig1.show(config = config)


# ***Note: Hovering over the points in the above map provides us information of Borough, Agency operating in that borough, the lattitude and longitude of that charging station.***
# 
# From the above density plot, we can infer that most densley located charging stations are located mainly in Queens and Manhattan. These boroughs are highly populated. There is need for increased EV infrastructure to be located in these boroughs for increased service. 
# 
# *code citation: https://plotly.com/python/reference/densitymapbox/*

# ### 3.1.2 Ranking Agencies based on operating size in NYC
# 
# To find the top 5 agencies operating in NYC can be visualized by plotting a bar graph. The graph takes into account the operating size of stations installed in 5 boroughs on New York City by different agencies.  

# In[4]:


# Creating a dataframe by grouping agency with size() 
df = evfleet_df.groupby('agency').size().reset_index(name='Size')

# Sorting Agencies in descending order of size
df=df.sort_values(by='Size',ascending=False).head(5)
values = list(df['Size'])

# Plotting bar graph- Agencies vs size

plt.bar(df['agency'],df['Size'],color='orange',edgecolor='black')
plt.ylabel('Size')
plt.xlabel('Agencies')
plt.title('Ranking Top 5 Agencies based on Operation Size')

for i in range(0,len(values)):
    a = str(values[i])
    plt.text(i,values[i],a, ha='center',va='bottom')
    
plt.show()


# The goal here is to rank top 5 agencies and hence first the count for each agency is calculated and then sorted in descending order.
# 
# From the above plot, Agency DPR and DSNY contribute significantly for EV charging service in NYC. 
# 
# 
# *code citation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html*

# ### 3.1.3  Visualization of Charging Port Capacity of Each Agency
# 
# The goal here is to visualize how many ports in EV charging stations does each agency in NYC provides

# In[5]:


#Grouping agencies by sum of no_of_ports offered by each agency
#Creating a new pandas data frame
port_count = evfleet_df.groupby(by=['agency'])['no_of_ports'].sum()
port_count = port_count.to_frame().reset_index()
port_count.plot(kind="bar", x="agency",xlabel="AGENCY",ylabel="NUMBER OF PORTS",color='orange',edgecolor='black',legend=False ,figsize=(10,5),title="NUMBER OF PORTS OFFERED BY EACH AGENCY")
countlist=list(port_count["no_of_ports"])

for i in range(0,len(countlist)):
    a = str(countlist[i])
    plt.text(i,countlist[i],a, ha='center',va='bottom',fontsize=9)

plt.show()


# From the above graph, we can infer that DPR provides significantly higher number of charging ports in NYC followed by DSNY and DEP.
# 
# 
# 
# *code citation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html*

# ### 3.1.4 Analysis on number of charging ports
# 
# The transition from internal combustion engines to electric vehicles will need the sufficient charging infrastructure. Each charging station has a different number of ports. Let's take a look at the three criteria of charging station, charging port capacity, and borough to see where we may make improvements in the future.
# 
# **3.1.4.1 Violin Plot**
# 
# The charging stations in each borough, which were grouped by the number of charging ports, were displayed using a violin plot.

# In[6]:


# creating a dataframe that contains columns "boroughs" and "no_of_ports"
sep1 = evfleet_df[['borough','no_of_ports']]
sep1

# creating a violin plot using plotly visualization library
fig = go.Figure()
fig.add_trace(go.Violin(x=sep1['borough'],y=sep1['no_of_ports'],
                            name='borough',
                            box_visible=True,
                            meanline_visible=True))
fig.update_layout(title={'text':"VIOLIN BOX PLOT FOR NO OF PORTS IN EACH STATION IN EACH BOROUGH",'y':0.87,'x':0.5,'xanchor':'center','yanchor':'top'})
fig.show()


# We can observe from the violin plot that the number of stations with one port is higher in all boroughs than the number of stations with two ports. We could immediately see that each station's charging port capacity has to be increased to allow the seamless transition to EVs.
# 
# *code citation: https://plotly.com/python/violin/*

# **3.1.4.2 Mapping using Folium visualization library**
# 
# The charging stations and their locations are projected on a map with color coding according to the station's charging port capacity
# 
# **Folium library** is used to create a map and visualize the related parameters in the previous violin plot.

# In[7]:


loc = 'LOCATION OF STATIONS WITH 1 AND 2 CHARGING PORTS'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)   

#folium.map() from folium library is used to project and differentiate the staions with number of ports offered

m=folium.Map(location=[40.72139, -73.844311],tiles='cartodbpositron',zoom_start=9.5,zoom_control=False,scrollWheelZoom=False,dragging=False)

#Adding markers to the map
i = 0
for index, row in evfleet_df.iterrows():
    if i<len(evfleet_df):
        x,y = row["latitude"], row["longitude"] 
        ports = row['no_of_ports']
        if(int(ports)>1):
            folium.CircleMarker(location=[x,y],radius=4,fill_opacity=1,fill_color='blue',color='blue',tooltip=ports).add_to(m)
        else:
            folium.CircleMarker(location=[x,y],radius=4,tooltip=ports,color="red",fill_color='red',fill_opacity=1).add_to(m)
        i = i+1

        
m.get_root().html.add_child(folium.Element(title_html))

m.save('map-with-title.html')
m


# ***Note: Hovering over the points in the above map provides us information of port capacity in that charging station.***
# 
# 
# 
# We could easily identify the position of charging stations on the above map, with just one charging port indicated in red circles. In heavily populated boroughs like Manhattan, Queens, and Bronx, more attention is needed to these charging stations in order to boost their capacity.
# 
# *code citation: https://gis.stackexchange.com/questions/203062/using-mapbox-tiles-with-folium*

# ### 3.1.6 Charging Port, Station Capacity in Boroughs
# To understand the EV infrastructure in each borough, we are proceeding to visualize the charging port and charging station capacity in each burrow, by constructing a radar chart.
# 

# The no of ports are first grouped according to the boroughs in the dataframe. The plotly express line polar function is then utilized to arrive at the chart. Similarly, we a grouping the boroughs according to the station, to understand the station capacity in each borough and analyse their EV infrastructure capabilities.

# In[8]:


# Using groupby function to sort the data for total sum of ports in each borough
port_count = evfleet_df.groupby(by=['borough'])['no_of_ports'].sum()
port_count= port_count.to_frame().reset_index()

# Applying the plotly express line polar function to visualize the radar chart
fig2 = px.line_polar(port_count, r='no_of_ports', theta='borough', line_close=True,title="")

# Assigning a title to the radar chart along with the alignment
fig2.update_layout(
    title={
           'text': "Borough vs No of Charging Ports",
           'y':0.99,
           'x':0.5,
           'xanchor': 'center',
           'yanchor': 'top'})

fig2.show()

# Using groupby function to sort the data for total no of stations in each borough
station_count = evfleet_df.groupby(by=['borough'])['station_name'].count()
station_count= station_count.to_frame().reset_index()

# Applying the plotly express line polar function to visualize the radar chart
fig1 = px.line_polar(station_count, r='station_name', theta='borough', line_close=True)
fig1.update_layout(
    title={
        'text': "Borough vs No of Charging stations",
        'y':0.99,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig1.show()


# From the radar chart above we understand that Queens is best equipped to handle the EV needs for charging. They lead in both the maximum number of charging ports and stations followed by Brooklyn. We understand that the EV infrastructure is lacking in Bronx, Manhattan ,Staten Island and need to increase the station and port capacity
# 
# *code citation: https://plotly.com/python/radar-chart/*

# ### 3.1.7 Vehicles Operating in each Borough
# We can see in the Radar Chart that Queens has the most developed EV Infrastructure. This makes us want to understand which borough has the highest census count.
# 
# For this purpose, we are using the groupby function for the boroughs in reference to the census_tract and plotting a horizontal bar chart using the matplotlib package. The X-axis represents the census and the Y-axis represents the 5 boroughs 

# In[9]:


# Utilizing groupby function to group the total census_tract according to each borough
# Also utilizing the drop_duplicates function to avaoid repetition
census_count = evfleet_df.drop_duplicates().groupby(by=['borough'])['census_tract'].sum()
census_count = census_count.to_frame().reset_index()
census_count

# Plotting a horizontal bar chart using matplotlib package
census_count.plot(x="borough",y='census_tract',kind="barh",legend=False,ec="black",
                       color=['steelblue','darkorange','forestgreen','r','mediumpurple'],
                       figsize=(15,7))

# Labelling and titles
plt.ylabel("BOROUGHS")
plt.xlabel("VEHICLE CENSUS")
plt.title("VEHICLE CENSUS IN EACH BOROUGH")

plt.show()


# From the above graph, we understand that Queens has the highest census count operating within, compared to other boroughs. Since the census count in Queens is high, this would mean that Queens would need to have the strongest EV Infrastructure, which is synonymous with our inference from the Radar chart that Queens is best equipped with lots of charging stations and ports.
# 
# *code citation: https://datatofish.com/horizontal-bar-chart-matplotlib/*

# ### 3.1.8 Agency Operation in Boroughs
# Here we are trying to visualize the number of agencies that are operating in each borough using a pie chart.
# 
# Firstly, we are grouping the agnecies according to the boroughs they operate in using the pandas groupby function. We are then utilizing the Seaborn visualization library to create a pie chart. It should be noted that we are displaying only the absolute values in the pie chart and not the percentages.

# In[10]:


# Using groupby function to sort the data for agencies in each borough
agency_count= evfleet_df.groupby(by=['borough'])['agency'].nunique()
agency_count=agency_count.to_frame().reset_index()
agency_count

# Define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:5]
explode = [0.04,0.04,0.04,0.04,0.04]

# Writing a function to display actual values in the pie chart 
def  absolute_value(val):
    a = np.round(val/100.*agency_count['agency'].sum(),0)
    return int(a)

#create pie chart using seaborn and matplotlib library 
plt.pie(agency_count['agency'], labels = agency_count['borough'], colors = colors, autopct=absolute_value, explode=explode,radius=2)
plt.title("Number of Agencies Operating in each Borough",x=0.5,y=1.6, bbox={'facecolor':'0.8', 'pad':5})
plt.show()


# From the above pie-chart we understand that queens is the most operation friendly borough as the highest no of agencies operate in Queens. We can see that Bronx has the lowest count. This could be due to the lower population count in Bronx compared to the other boroughs.
# 
# 
# *code citation: https://www.statology.org/seaborn-pie-chart/*

# In[ ]:




