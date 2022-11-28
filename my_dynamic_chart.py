import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("C:/Users/KYershat/Desktop/projects/cause_of_deaths_around_the_world/cause_of_deaths.csv")

# I want to get top 10 causes of death data for each year and each country(country should be avaible as a choice)


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
country = "Zimbabwe"



## Animating the pie chart
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# Starting year
start_year = 1979



## labels are not shown when percenatage is lower than 5%, but reappear when it does. 
def my_autopct(pct):
    return ('%1.1f%%' % pct) if pct > 5 else ''


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
 

    explode = (0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.2,0.3,0.3,0.2,0.2)
    colors= ['orange', 'blue', 'green', 'yellow', 'brown','pink','#ff9999','#66b3ff','#99ff99','#ffcc99','#721779']
    the_text_on_title = str(country) + " - " + str(start_year)
    ax1.clear()
    ax1.title.set_text(the_text_on_title)

    ax1.pie(ten_main_causes, labels=causes_names, autopct=my_autopct, shadow=True, startangle=140,colors = colors)
    start_year+=1
    plt.pause(0.5)
    percentage_of_cause.clear()
    ten_main_causes.clear()
    location_of_causes.clear()
    causes_names.clear()

plt.draw()




# countries = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 
#        'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
#        'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',        
#        'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 
#        'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
#        'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',        
#        'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
#        'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',  
#        'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 
#        'Croatia', 'Cuba', 'Cyprus', 'Czechia',
#        'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 
#        'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
#        'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 
#        'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
#        'Germany', 'Ghana', 'Greece', 'Greenland', 'Grenada', 'Guam',      
#        'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
#        'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',    
#        'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
#        'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos',     
#        'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania',       
#        'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
#        'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius',        
#        'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',
#        'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
#        'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua',
#        'Niger', 'Nigeria', 'Niue', 'North Korea', 'North Macedonia',
#        'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',     
#        'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
#        'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
#        'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis',
#        'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
#        'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',      
#        'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia',       
#        'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
#        'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan',
#        'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
#        'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tokelau',      
#        'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
#        'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
#        'United Arab Emirates', 'United Kingdom', 'United States',
#        'United States Virgin Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu',    
#        'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']





   
