#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np


movie_data = pd.DataFrame(data=[["Gladiator",8.5,"Russell Crowe"], 
                       ["Pulp Fiction",8.9,"John Travolta"],
                       ["The Godfather",9.2,"Marlon Brando"]], 
                 columns=["movie","imdb_rating","starring"])
print(movie_data)



new_movie = pd.DataFrame(data=[["Uncut Gems",7.6,"Adam Sandler"]], 
                 columns=["movie","imdb_rating","starring"])
print(new_movie)


list_of_DataFrames = movie_data, new_movie
total_movie_data = pd.concat(list_of_DataFrames)
print(total_movie_data)



concatenated_df = pd.concat([movie_data,new_movie], ignore_index=False)
print(concatenated_df)



concatenated_df = pd.concat([movie_data,new_movie] ,ignore_index=True)
print(concatenated_df)


total_movie_data = pd.concat([movie_data, new_movie], axis=0, ignore_index=True)
print(total_movie_data)

oscars = pd.DataFrame(data=[5, 1, 3, 0], columns=["oscars"])
print(oscars)


movie_data_with_new_feature = pd.concat([total_movie_data, oscars], axis=1)
print(movie_data_with_new_feature)


try:
    movie_data_duplicate_data = pd.concat([movie_data, new_movie, new_movie, new_movie], 
                                       ignore_index=True)
    print(movie_data_duplicate_data)
    
except:
    print("There is duplicate data on the concatenation!")    


try:
    movie_data_duplicate_data = pd.concat([movie_data, new_movie, new_movie, new_movie],
                                        verify_integrity=True)
    print(movie_data_duplicate_data)
except Exception as error:
    print("There is duplicate data on the concatenation!")
    print(error)


appended_df = movie_data.append(new_movie, ignore_index=True)
print(appended_df)


print(concatenated_df.reset_index(drop=True) == appended_df.reset_index(drop=True))

movie_data.loc[2] = new_movie.loc[0]
print(movie_data)


from sklearn.datasets import fetch_openml

# Here we use a Sklearn handy fetch_openml function to import the data from OpemMl 
raw_data = fetch_openml("credit-g")

# After fetching it, let's take the name of data features
features = raw_data["feature_names"]

# The name of the data to be predicted
target_name = raw_data["target_names"][0]

# Create a Dataframe with the downloaded data
df = pd.DataFrame(data=raw_data["data"], columns=features)
df[target_name] = raw_data["target"]

# Here we select the first 600 samples of the DataFrame 
# by using the useful pythonic slicing feature
first_survey = df[:600]
print(first_survey)

second_survey = df[-400:]
print(second_survey)


complete_survey_data = pd.concat([first_survey, second_survey], ignore_index=True)
print(complete_survey_data)


complete_survey_data = first_survey.append(second_survey, ignore_index=True)
print(complete_survey_data)



clean_survey_data = first_survey.copy()
clean_survey_data.iloc[-400:] = second_survey.values
print(clean_survey_data)
