import requests
import numpy as np
import plotly.graph_objects as go


def plotter(drivers, p1, p2, p3):
    fig = go.Figure()
    fig.add_bar(x=drivers, y=p1, name="First")
    fig.add_bar(x=drivers, y=p2, name="Second")
    fig.add_bar(x=drivers, y=p3, name="Third")
    fig.update_layout(barmode="relative",
                      xaxis_title="Driver", yaxis_title="Number of wins", legend_title="Podium Position",
                      title={'text': "Number of podium wins in F1 (1990-2020) Grand Prix", 'y': 0.9, 'x': 0.5,
                             'xanchor': 'center', 'yanchor': 'top'})
    fig.show()


def grouper(list1, f1, f2, s1, s2, t1, t2):
    # Initiating empty arrays
    drivers = []
    pod_1 = []
    pod_2 = []
    pod_3 = []
    pod_all = []

    # For loop to consolidate individual wins for a specific driver
    for x in list1:
        first = 0
        second = 0
        third = 0
        index1 = np.where(f1 == x)     # Finding index of driver and then using it for other arrays
        index2 = np.where(s1 == x)
        index3 = np.where(t1 == x)

        if (len(index1[0]) > 0):
            first += f2[index1[0][0]]

        if (len(index2[0]) > 0):
            second += s2[index2[0][0]]          # Summing up the podium wins for individual drivers

        if (len(index3[0]) > 0):
            third += t2[index3[0][0]]

        total = first + second + third
        drivers.append(x)
        pod_1.append(first)
        pod_2.append(second)    # Appending the needed values to their own lists
        pod_3.append(third)
        pod_all.append(total)

    np_drivers = np.array(drivers)
    np_pod_1 = np.array(pod_1)
    np_pod_2 = np.array(pod_2)              # Converting regular lists to Numpy arrays
    np_pod_3 = np.array(pod_3)
    np_pod_all = np.array(pod_all)

    sorted_pod = np.argsort(-np_pod_all)
    drivers_final = np_drivers[sorted_pod]
    np_pod_1_final = np_pod_1[sorted_pod]       # Masking all the arrays to sort them in descending order using argsort
    np_pod_2_final = np_pod_2[sorted_pod]
    np_pod_3_final = np_pod_3[sorted_pod]

    return (drivers_final, np_pod_1_final, np_pod_2_final, np_pod_3_final)


def apiCall(year1, year2):
    temp_year = year1
    first_raw = []
    second_raw = []         # Initializing empty arrays to store fetched data
    third_raw = []
    while temp_year <= year2:

        my_base_url = "http://ergast.com/api/f1/" + str(temp_year) + "/1/results.json" # Base URL of our API with the endpoint
        response = requests.get(my_base_url)

        if (response):
            data = response.json()['MRData']['RaceTable']['Races'][0] # If valid , save data to variable
            print(f"Year: {temp_year}, Race: {data['Circuit']['circuitName']}")
            for x in data['Results']:
                if (int(x['position']) == 1):
                    first_raw.append(x['Driver']['givenName'] + ' ' + x['Driver']['familyName'])
                elif (int(x['position']) == 2):
                    second_raw.append(x['Driver']['givenName'] + ' ' + x['Driver']['familyName']) # Seperating different podium winners to different arrays
                elif (int(x['position']) == 3):
                    third_raw.append(x['Driver']['givenName'] + ' ' + x['Driver']['familyName'])
                print(f"{x['position']}.{x['Driver']['givenName']} {x['Driver']['familyName']} ")

        else:
            print(f"Couldn't fetch data for {temp_year}.")

        temp_year += 1

    first = np.array(first_raw)
    second = np.array(second_raw)
    third = np.array(third_raw)

    first_unique, first_counts = np.unique(first, return_counts=True)
    second_unique, second_counts = np.unique(second, return_counts=True)    # Finding unique values to avoid repeats
    third_unique, third_counts = np.unique(third, return_counts=True)

    consolidated = np.unique(np.concatenate((first_unique, second_unique, third_unique)))   # Consolidating all drivers into one and making it unique to avoid repeats

    final_d, final_1, final_2, final_3 = grouper(consolidated, first_unique, first_counts, second_unique, second_counts, # Sending data to grouper function to filter data
                                                 third_unique, third_counts)

    plotter(final_d, final_1, final_2, final_3)  # Sending data to plotter function to plot our graph



"""
 =================================================================================================================
 MAIN CALL FOR PROGRAM 
 Lots of optimizations can be done by consolidating many function calls into one or skipping conversion of lists and arrays
==================================================================================================================
"""

apiCall(1990, 2020)
