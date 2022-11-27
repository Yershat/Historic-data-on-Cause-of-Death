import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:/Users/KYershat/Desktop/projects/cause_of_deaths_around_the_world/cause_of_deaths.csv")

# I want to get top 10 causes of death data for each year and each country(country should be avaible as a choice)


data["Total"] = data.iloc[:,3:].sum(axis=1)

for col in data.columns[3:-1]:
    data[col] /= data["Total"]
    data[col] = round(data[col],3)

labels = []
for i in data:
    labels.append(i)

causes = labels[3:-1]


percentage_of_cause = []
for i in data.iloc[1,3:-1]:
    percentage_of_cause.append(i)

ten_main_causes = sorted(percentage_of_cause,reverse = True)[0:10]

## Location of diseases with highest percentage in the original row
location_of_causes = []
for i in ten_main_causes:
    for a,ind in enumerate(percentage_of_cause):
        if i ==ind:
            location_of_causes.append(a)

## Adding the remaining causes as other 
other = 1 - sum(ten_main_causes)
ten_main_causes.append(other)
## Identifying the main diseases names from original row
causes_names= []
for i in location_of_causes:
    causes_names.append(causes[i])
causes_names.append("Other")
explode = (0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.2,0.3,0.3,0.2,0.2)
colors= ['red', 'orange', 'blue', 'white', 'green', 'yellow', 'brown','pink','#ff9999','#66b3ff','#99ff99','#ffcc99']

country = "Zimbabwe"

## How to go over each row with country and year above it?

for i,row in data.loc[data["Country/Territory"] == country].iterrows():
    a = data.loc[i]
    print(a.iloc[1,3:-1])

# plt.pie(ten_main_causes, labels = causes_names,autopct='%1.1f%%',explode=explode,colors = colors)
# plt.show() 



   
