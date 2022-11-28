## Building a dynamic histogram that will be places next to the pie chart

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Downloading the data 
data = pd.read_csv("C:/Users/KYershat/Desktop/projects/cause_of_deaths_around_the_world/cause_of_deaths.csv")

# Renaming the column names to shorter versions of them
data.rename(columns = {"Alzheimer's Disease and Other Dementias":"Alzheimer's/Dementia", "Parkinson's Disease":"Parkinson's", "Interpersonal Violence":"Violence", "Drug Use Disorders":"Drugs","Cardiovascular Diseases":"Cardiovascular" }, inplace = True)
data.rename(columns = {"Alcohol Use Disorders":"Alcohol","Environmental Heat and Cold Exposure":"Environmental","Conflict and Terrorism":"Conflict","Chronic Kidney Disease":"Kidney Disease","Cirrhosis and Other Chronic Liver Diseases":"Liver diseases"}, inplace = True)
data.rename(columns = {"Chronic Respiratory Diseases":"Respiratory","Fire, Heat, and Hot Substances":"Hot substances"}, inplace = True)

# Calculating total count of deaths 
data["Total"] = data.iloc[:,3:].sum(axis=1)

## Changing dataset so it only shows the percentage of total deaths in given year
for col in data.columns[3:-1]:
    data[col] /= data["Total"]
    data[col] = round(data[col],6)

labels = []
for i in data:
    labels.append(i)

# Causes dataset contains only disease names
causes = labels[3:-1]


country =  "Zimbabwe"


fig, ax = plt.subplots()


## Getting the data ready
for i,row in data.loc[data["Country/Territory"] == country].iterrows():
    percentage_of_cause = []
    for a in row[3:-1]:
        percentage_of_cause.append(a)

    
    ten_main_causes = sorted(percentage_of_cause,reverse = True)[0:10]

    # Converting the values to whole number for better representability
    ten_main_causes_converted = []  
    for i in ten_main_causes:
        ten_main_causes_converted.append(int(round(i * row["Total"],1))) 
    
   
    location_of_causes = []
    for i in ten_main_causes:
        for a,ind in enumerate(percentage_of_cause):
            if i == ind:
                location_of_causes.append(a)
    
    other = 1 - sum(ten_main_causes)
    # These are the x-axis values

    ten_main_causes_converted.append(round(other*row["Total"],1))

    ten_main_causes_converted = sorted(ten_main_causes_converted,reverse= True)

    # Cause names are the y-axis values
    causes_names= []
    for i in location_of_causes:
        causes_names.append(causes[i])
    
    causes_names.append("Other")

    y_pos = np.arange(len(causes_names))
    colors= ['orange', 'blue', 'green', 'yellow', 'brown','pink','#ff9999','#66b3ff','#99ff99','#ffcc99','#721779']


    # ax.barh(causes_names, ten_main_causes_converted, align='center' )

    # ax.set_yticks(y_pos)
    # ax.invert_yaxis()  # labels read top-to-bottom
    # ax.set_xlabel('Count')
    # ax.set_title('Count of death by cause')

    plt.pause(0.8)
    percentage_of_cause.clear()
    ten_main_causes_converted.clear()
    location_of_causes.clear()
    causes_names.clear()


plt.show()

    

    



