#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:58:31 2021

@author: catalinadiaz
"""

import pandas as pd
import numpy as np


'Cleaning Atlantic CSV'
# =============================================================================
# df = pd.read_csv('./atlantic.csv', usecols={0,1,2,3,4,5,6,7,8})
# 
# #cleaning these two because there is no data here
# col_label =['Name', 'ID', 'Event']
# df.drop(col_label, inplace=True, axis=1)
# 
# print(df)
# 
# df.to_csv('atlantic-clean.csv')
# =============================================================================

'Cleaning Pacific CSV'

# =============================================================================
# 
# df = pd.read_csv('./pacific.csv',  usecols={0,1,2,3,4,5,6,7,8})
# 
# 
# #cleaning these two because there is no data here
# col_label =['Name', 'ID', 'Event']
# df.drop(col_label, inplace=True, axis=1)
# 
# print(df)
#  
# df.to_csv('pacific-clean.csv')
# 
# =============================================================================

'Cleaning us-hurricanes...'


# =============================================================================
# df = pd.read_csv('./us-hurricanes.csv',)
# 
# col_label =['Name']
# df.drop(col_label, inplace=True, axis=1)
# 
# 
# print(df)
#  
# df.to_csv('us-hurricane-clean.csv')
# =============================================================================
