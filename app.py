#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 23:25:34 2021

@author: catalinadiaz
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Hurricane Data')

#df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
DATA_URL = ('/Users/catalinadiaz/Documents/Data Science/project-datasets/cleaned-data/us-hurricanes.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.write(data)

df = pd.DataFrame(data, columns=['year'])

st.line_chart(df)