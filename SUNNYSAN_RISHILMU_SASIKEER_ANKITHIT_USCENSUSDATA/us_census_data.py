import matplotlib.pyplot as plt
import requests
import pandas as pd

# function to perform API call and return the JSON data.
def get_data(url):
    response = requests.get(url)
    data = response.json()['data']
    return pd.DataFrame(data)

# make the get request
nation_wide_population = get_data('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
state_wise_population = get_data('https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest')
state_wise_house_ownership = get_data('https://datausa.io/api/data?drilldowns=State&measures=Household Ownership&year=latest')
state_wise_average_income = get_data('https://datausa.io/api/data?drilldowns=State&measures=Average Income&year=latest')

# Yearwise population increase
nation_wide_population = nation_wide_population.sort_values(by=['Year'])
plt.plot(nation_wide_population['Year'], nation_wide_population['Population'])
plt.ticklabel_format(style = 'plain', axis='y')
plt.title("US Population Growth")
plt.show()

# Average Income
plt.boxplot(state_wise_average_income['Average Income'])
plt.title("Boxplot of Average Income")
plt.show()

# State with most house ownership
state_wise_house_ownership = state_wise_house_ownership.sort_values(by=['Household Ownership'], ascending = False).head(5)
plt.bar(state_wise_house_ownership['State'], state_wise_house_ownership['Household Ownership'], color="orange")
plt.xticks(rotation=45)
plt.ticklabel_format(style = 'plain', axis='y')
plt.title("States with most House Ownership")
plt.show()

# State with least population
state_wise_population = state_wise_population.sort_values(by=['Population'], ascending = True).head(5)
plt.bar(state_wise_population['State'], state_wise_population['Population'],  color="red")
plt.ticklabel_format(style = 'plain', axis='y')
plt.xticks(rotation=45)
plt.title("States with least Population")
plt.show()

