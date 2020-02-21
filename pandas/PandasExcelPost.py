#!/usr/bin/env python
# coding: utf-8

import pandas as pd

dataframe = pd.read_excel("The-Ramen-Rater-The-Big-List-1-3400-Current-As-Of-Jan-25-2020.xlsx")


dataframe = pd.read_excel("The-Ramen-Rater-The-Big-List-1-3400-Current-As-Of-Jan-25-2020.xlsx", 
                          sheet_name="Reviewed")




# Sort all of the reviews by the review number
dataframe_sorted = dataframe.sort_values("Review #")
# The drop parameter removes the old index, since it is created by default as a new column
dataframe_sorted = dataframe_sorted.reset_index(drop=True) 


# First we cast the Stars column as float32, so we can create the new column with it
# The dataset column Stars need some cleaning because it contains invalid values
from numpy import nan
def clearFloat(string):
    try:
        return float(string)
    except:
        return nan
    
# Now every valid float number is a number and every invalid entry in the Stars column in None
dataframe_sorted["Stars"] = dataframe_sorted["Stars"].apply(clearFloat)
# Now we drop every row that has invalid data
print("Size of the unclean dataset:", len(dataframe_sorted))
dataframe_sorted = dataframe_sorted.dropna()
print("Size of the clean dataset:", len(dataframe_sorted))


# And create a new column for the 0 to 10 rating
dataframe_sorted["Rating"] = dataframe_sorted["Stars"] * 2
dataframe_sorted.head()


dataframe_sorted.to_excel("ramen-ratings-clean.xlsx")
dataframe_sorted.to_excel("ramen-ratings-clean.xlsx", sheet_name="Ramen-ratings", index=False)
writer = pd.ExcelWriter('ramem-by-country-analytics.xlsx', engine="openpyxl", index=False)

dataframe_sorted.to_excel(writer, "World Data", index=False)

# Since the group by returns a tuple with the name of the country and the country dataset
# let's create some useful variables to access it
tuple_name = 0 # Used to access the name of the tuple, eg. Australia
tuple_dataframe = 1 # Used to access the Dataframe that represents some country, eg. Ramen ratings of Australia

analytics = pd.DataFrame(columns=["Country","Number of Reviews","Average Stars","Average Rating", "Rating Standard Deviation"])

def generate_analytics(analytics_dataframe, country_name, country_dataframe):
    # Take the length of the DataFrame as the number of reviews     
    number_of_reviews = len(country_dataframe)
    # Calculate the average number of stars given to a country ramen
    average_stars = country_dataframe["Stars"].mean()
    # Calculate the average rating given to a country ramen
    average_rating = country_dataframe["Rating"].mean()
    # Calculate the rating standard deviation of the country    
    rating_std = country_dataframe["Rating"].std()
    

    # Append the analysis of one country to the Analytics Dataframe     
    analytics_dataframe = analytics_dataframe.append({"Country": country_name,"Number of Reviews": number_of_reviews,
                      "Average Stars": average_stars,"Average Rating": average_rating, 
                      "Rating Standard Deviation": rating_std}, ignore_index=True)
    
    return analytics_dataframe
    

for country_ramen_data in dataframe_sorted.groupby("Country"):
#     print(country_ramen_data[tuple_data])
    country_name = country_ramen_data[tuple_name]
    country_dataframe = country_ramen_data[tuple_dataframe]
    
    # Now every country dataframe is being saved on the Excel file     
    country_dataframe.to_excel(writer, country_name, index=False)
    analytics = generate_analytics(analytics, country_name, country_dataframe)

# Let's substitute the nan values from the standard deviation of countries with only one review
# We will change it to zero on the whole dataframe using the fillna() method
analytics = analytics.fillna(0)

analytics.to_excel(writer, "Analytics", index=False)

writer.close()


writer = pd.ExcelWriter('ramem-by-country-analytics.xlsx', engine="openpyxl", index=False
                       , mode="a") # a stands for append

analytics = pd.DataFrame(columns=["Country","Number of Reviews","Average Stars","Average Rating", "Rating Standard Deviation"])

old_analytics = pd.read_excel("ramem-by-country-analytics.xlsx", "Analytics")
new_analytics = old_analytics.append({"Country": "Zimbabwe","Number of Reviews": 1,
                      "Average Stars": 4,"Average Rating": 4.5, 
                      "Rating Standard Deviation": 0}, ignore_index=True)
new_analytics.to_excel(writer, "Analytics Updated", index=False)
writer.close()
