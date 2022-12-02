import pandas as pd
import matplotlib.pyplot as plt

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

## In the labels I get all the column names in the dataset
labels = []
for i in data:
    labels.append(i)

# Causes dataset contains only disease names
causes = labels[3:-1]

# Country can be chosen by user 
country = "Russia"




## Animating the pie chart
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# Starting year
start_year = 1979



## labels are not shown when percenatage is lower than 4%, but reappear when it does. 
def my_autopct(pct):
    return ('%1.1f%%' % pct) if pct > 4 else ''


## Loop through each year from 1979 to 2009
for i,row in data.loc[data["Country/Territory"] == country].iterrows():
    ## Contains all percentages 
    percentage_of_cause = []
    for a in row[3:-1]:
        percentage_of_cause.append(a)

    
    ## Getting top 10 diseases that cause most deaths
    ten_main_causes = sorted(percentage_of_cause,reverse = True)[0:10]   

    # By going to percentage_cause and locating the indexes of top 10 diseases , we can get 
    # names of those top 10 diseases
    location_of_causes = []
    for i in ten_main_causes:
        for a,ind in enumerate(percentage_of_cause):
            if i == ind:
                location_of_causes.append(a)

    ## As top 10 causes do not cover all deaths, all the remaining causes are under "other" tag
    other = 1 - sum(ten_main_causes)
    ten_main_causes.append(other)

    # Causes names are being located, related the code in lines 58 to 63
    causes_names= []
    for i in location_of_causes:
        causes_names.append(causes[i])
    
    # Adding remaining percentage label as well.
    causes_names.append("Other")
 

    explode = (0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.2,0.3,0.3,0.31,0.32)
    colors= ['orange', 'blue', 'green', 'yellow', 'brown','pink','#ff9999','#66b3ff','#99ff99','#ffcc99','#721779']
    the_text_on_title = str(country) + " - " + str(start_year)
    ax1.clear()
    plt.text(-0.3, 1.05, the_text_on_title, ha='left', va='top', transform=ax1.transAxes)
    ax1.pie(ten_main_causes, labels=causes_names, autopct=my_autopct, shadow=True, startangle=140,colors = colors, rotatelabels=True)
    start_year+=1
    plt.pause(1)
    percentage_of_cause.clear()
    ten_main_causes.clear()
    location_of_causes.clear()
    causes_names.clear()

plt.draw()





