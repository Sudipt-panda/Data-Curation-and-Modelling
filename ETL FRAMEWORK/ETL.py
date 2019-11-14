import pandas as pd
import numpy as np
import DataCleaning
from string import punctuation 
import matplotlib.pyplot as plt
import seaborn as sns




a = 'Hello'
print('hello is',a)

# df = pd.read_csv(r'/Users/sudiptkumarpanda/Downloads/Data Management 2 - Python Codes-20191110/ProdDim.csv')
# df2 = pd.read_csv(r'/Users/sudiptkumarpanda/Downloads/Data Management 2 - Python Codes-20191110/Product_Categories.csv')

# merged_inner = pd.merge(left=df,right=df2, left_on='Product_Category_1', right_on='Category_ID')

# newdf = merged_inner[['Product_ID','Category_Description','Product_Category_2','Product_Category_3']].copy()
# newdf.columns = ['Product_ID','Product_Category_1','Product_Category_2','Product_Category_3']

# merged_inner = pd.merge(left=newdf,right=df2, left_on='Product_Category_2', right_on='Category_ID')
# newdf = merged_inner[['Product_ID','Product_Category_1','Category_Description','Product_Category_3']].copy()
# newdf.columns = ['Product_ID','Product_Category_1','Product_Category_2','Product_Category_3']

# merged_inner = pd.merge(left=newdf,right=df2, left_on='Product_Category_3', right_on='Category_ID')
# newdf = merged_inner[['Product_ID','Product_Category_1','Product_Category_2','Category_Description']].copy()
# newdf.columns = ['Product_ID','Product_Category_1','Product_Category_2','Product_Category_3']

# print(newdf)