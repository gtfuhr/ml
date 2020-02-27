#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import pandas_log
df = pd.read_csv("vgsales.csv")

print(df.head())

with pandas_log.enable():
    df.head()

old_nintendo = df.copy().query("Year<2000").query("Rank<100").query("Publisher=='Nlntendo'")
print(old_nintendo)


with pandas_log.enable():
    old_nintendo = df.copy().query("Year<2000").query("Rank<100").query("Publisher=='Nlntendo'")

old_nintendo = df.copy().query("Year<2000").query("Rank<100").query("Publisher=='Nintendo'")
print(old_nintendo)


df.query("Platform=='PS2'").query("Genre=='Sports'").nlargest(10,"NA_Sales")

with pandas_log.enable():
    df.query("Platform=='PS2'").query("Genre=='Sports'").nlargest(10,"NA_Sales")

# Set if the program will show the Pandas-Log output while doing a query
# verbosity = False
verbosity = True

dataframe = pd.read_csv("vgsales.csv")

# Execute two important queries asked by the client
# When the client wants to be assured of the results, he would set the verbosity to 1
if(verbosity):
    with pandas_log.enable():
        top_five_take_two_games = dataframe.query("Publisher=='Take-Two Interactive'").nsmallest(5,"Rank")
else:
    top_five_take_two_games = dataframe.query("Publisher=='Take-Two Interactive'").nsmallest(5,"Rank")

print(top_five_take_two_games)


if(verbosity):
    with pandas_log.enable():
        top_five_sony_games = dataframe.query("Publisher=='Sony Computer Entertainment'").nsmallest(5,"Rank")
else:
    top_five_sony_games = dataframe.query("Publisher=='Sony Computer Entertainment'").nsmallest(5,"Rank")

print(top_five_sony_games)


