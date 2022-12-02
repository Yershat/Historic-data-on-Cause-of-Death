import pandas as pd
import matplotlib.pyplot as plt


# Downloading the data. Origin of data: https://www.kaggle.com/datasets/iamsouravbanerjee/cause-of-deaths-around-the-world
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
    data[col] = round(data[col],10)

    
## In the labels I get all the column names in the dataset
labels = []
for i in data:
    labels.append(i)

# Causes dataset contains only disease names
causes = labels[3:-1]



# Cause can be chosen by the user
cause = "Alzheimer's/Dementia"

## Filtering the data where the data contains data only on the specific disease
df1 = data.loc[:,["Country/Territory","Year",cause]]

# start year
start_year = df1["Year"][0]

last_year = df1["Year"].iat[-1]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


# Filtering data for each year
for i, row in df1.iterrows():   
    if start_year == last_year:
        break
    else:
        df2 = df1.loc[df1["Year"] == start_year]

    ## all country names given a year in order
        all_country_names = []
        for i in df2["Country/Territory"]:
            all_country_names.append(i)

    # List with percentages for each country
        all_country_percentage = []
        for i in df2[cause]:
            all_country_percentage.append(i)

    # Getting ten main causes
        ten_main_causes = sorted(all_country_percentage,reverse = True)[0:10]  

        new_ten_main_causes = []


        for i in ten_main_causes:
            if i not in  new_ten_main_causes:
                new_ten_main_causes.append(i)
            else:
                new_ten_main_causes.append(i + 0.0000000001)

    # Locating the countries
        location_of_countries = []
        for i in new_ten_main_causes:
            for a,ind in enumerate(all_country_percentage):
                if i == ind:
                    location_of_countries.append(a)

        country_names= []
        for i in location_of_countries:
            country_names.append(all_country_names[i])
  
        the_text_on_title = str(cause) + " - " + str(start_year)
        ax1.clear()
        plt.title(the_text_on_title)

        plt.bar(country_names,new_ten_main_causes)
        
        plt.xticks(rotation = 90)
        plt.pause(1)
    
        all_country_names.clear()
        all_country_percentage.clear()
        ten_main_causes.clear()
        location_of_countries.clear()
        country_names.clear()
    start_year+=1

    
    



