#!/usr/bin/env python
# coding: utf-8

# First, as we normally do, we are going to import pandas and numpy
import numpy as np
import pandas as pd

# Thats where we import the function that will generate the ProfileReport
from pandas_profiling import ProfileReport

# Loads the dataset with the admission probability of various students and their
# scores in different tests of knowledge
df = pd.read_csv("Admission_Predict_Ver1.1.csv", encoding = 'unicode_escape')


# Here is the function that generates the report using Pandas-Profiling
profile = ProfileReport(df, title='Graduate Admission', html={'style':{'full_width':True}})

profile.to_notebook_iframe()

# Hint! If you were using a large dataset, set the minimal named argument to True
# profile = ProfileReport(large_dataset, minimal=True)

# It is also recommended to open the report as a html file, in this way Jupyter-Notebook
# does not becames laggy because of the big Jupyter-Notebook cell
profile.to_file(output_file="largeDatasetProfileReport.html")

# The profile report can also be saved as json, just change the file extension in the 
# to_file() call
profile.to_file(output_file="largeDatasetProfileReport.json")
