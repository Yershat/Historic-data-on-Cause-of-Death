# Show the highest proportion country for each cause of death from 1979 to 2009

import pandas as pd
import matplotlib.pyplot as plt

# Downloading the data 
data = pd.read_csv("C:/Users/KYershat/Desktop/projects/cause_of_deaths_around_the_world/cause_of_deaths.csv")

print(data)
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


## In the labels I get all the column names in the dataset
labels = []
for i in data:
    labels.append(i)

# Causes dataset contains only disease names
causes = labels[3:-1]



