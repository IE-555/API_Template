# -*- coding: utf-8 -*-
import pandas as pd
import requests
import json

url = 'https://api.teleport.org/api/urban_areas/'
payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)

urb_area = []
for u in data['_links']['ua:item']:
  urb_area.append(u['name'])
  
slug_urb = []
for u in urb_area:
  u = u.replace(' ','-')
  u = u.replace(',','')
  u = u.replace('.','')
  u = u.lower()
  slug_urb.append(u)

term = 'slug:'+slug_urb[0]
url = 'https://api.teleport.org/api/urban_areas/'+term+'/scores/'
payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)
categories = []
categories.append('Urban Area')
for d in data['categories']:
  categories.append(d['name'])

categories.append('Total City Score')
df = pd.DataFrame(columns = categories)

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

rsdf = df.sort_values(by=['Total City Score'], ascending=False)

new_df = rsdf[:3]
df2 = rsdf[int(len(rsdf)/2)-2:int(len(rsdf)/2)+2]
new_df = new_df.append(df2, ignore_index = True)
df3 = rsdf[-3:]
new_df = new_df.append(df3, ignore_index = True)

import matplotlib.pyplot as plt

plt.bar(new_df['Urban Area'], new_df['Total City Score'])
plt.ylabel('Total City Score (in %)')
plt.xticks(rotation=90)
        
plt.savefig('Total City Score.png')
plt.show()

#Factors chosen: Cost of living, Safety, Travel connectivity, Education, Environmental quality

#Considering safety as priority (in pie chart)

rs1df = df.sort_values(by=['Safety'], ascending=False)
newdf = rs1df[:5]

df2 = pd.DataFrame(newdf['Total City Score'].tolist(), index = newdf['Urban Area'].tolist(), columns = ['Total City Score'])
print (df2)

perc = (newdf['Total City Score']/sum(newdf['Total City Score']))*360
perc = perc.tolist()
print (perc)
areas = newdf['Urban Area'].tolist()
print (areas)


df2.plot(kind='pie',y='Total City Score', autopct='%1.0f%%', figsize= (16,8))
plt.savefig('Safety & Total City Score.png')
plt.show()

#Considering environmental quality as priority (in horizontal clustered bar graph)
rs1df = df.sort_values(by=['Environmental Quality'], ascending=False)
newdf = rs1df[:10]
newdf['Environmental Quality'] = newdf['Environmental Quality']*10
newdf['Total City Score'] = (newdf['Total City Score']/170)*100
newdf.plot(x="Urban Area", y=['Environmental Quality','Total City Score'], kind="barh", figsize= (14,8))
for index,value in enumerate(newdf['Total City Score']):
   value = round(value,2)
   plt.text(value, index, str(value))
plt.savefig('Environment Quality & Total City Score.png')
plt.show()

#Considering cost of living as priority (in horizontal clustered bar graph)

rs1df = df.sort_values(by=['Cost of Living'], ascending=False)
newdf = rs1df[:10]
newdf['Cost of Living'] = newdf['Cost of Living']*10

newdf.plot(x="Urban Area", y=['Cost of Living','Total City Score'], kind="barh", figsize= (10,8))
for index, value in enumerate(newdf['Total City Score']):
    value = round(value,2)
    plt.text(value, index, str(value))

plt.savefig('Cost of Living & Total City Score.png')
plt.show()

#Considering education as priority (in pie chart)

rs1df = df.sort_values(by=['Education'], ascending=False)
newdf = rs1df[:5]

df2 = pd.DataFrame(newdf['Total City Score'].tolist(), index = newdf['Urban Area'].tolist(), columns = ['Total City Score'])
print (df2)

perc = (newdf['Total City Score']/sum(newdf['Total City Score']))*360
perc = perc.tolist()
print (perc)
areas = newdf['Urban Area'].tolist()
print (areas)


df2.plot(kind='pie',y='Total City Score', autopct='%1.0f%%', figsize= (16,8))

plt.savefig('Education & Total City Score.png')
plt.show()

#Considering travel connectivity as priority (in horizontal clustered bar graph)

rs1df = df.sort_values(by=['Travel Connectivity'], ascending=False)
newdf = rs1df[:10]
newdf['Travel Connectivity'] = newdf['Travel Connectivity']*10

newdf.plot(x="Urban Area", y=['Travel Connectivity','Total City Score'], kind="barh", figsize= (10,8))
for index, value in enumerate(newdf['Total City Score']):
    value = round(value,2)
    plt.text(value, index, str(value))
    
plt.savefig('Travel Connectivity & Total City Score.png')
plt.show()

