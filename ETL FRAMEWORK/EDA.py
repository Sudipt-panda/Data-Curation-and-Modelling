#test file


import pandas as pd
import numpy as np
import warnings
import logging
import matplotlib.pyplot as plt
import seaborn as sns

warnings.simplefilter(action='ignore', category=FutureWarning)

logger3 = logging.getLogger(__name__)

def EDA(df_preprocessed):
    logger3.info("EDA started")
    data = df_preprocessed
    #Co-relation between gender and purchase
    cols = ['User_ID','Product_ID']
    data.drop(cols, inplace = True, axis =1)
    data[['Gender','Purchase']].groupby('Gender').mean().plot.bar()
    sns.barplot('Gender', 'Purchase', data = data)
    plt.show()
    #Co-relation between Age and purchase
    data[['Age','Purchase']].groupby('Age').mean().plot.bar()
    sns.barplot('Age', 'Purchase', data = data)
    plt.show()
    sns.boxplot('Age','Purchase', data = data)
    plt.show()
    #Co-relation between city_category and purchase
    data[['City_Category','Purchase']].groupby('City_Category').mean().plot.bar()
    sns.barplot('City_Category', 'Purchase', data = data)
    plt.show()
    #heat-map to show co-relation between all variables
    corrmat = data.corr()
    fig,ax = plt.subplots(figsize = (12,9))
    sns.heatmap(corrmat, vmax=.8, square=True)
    logger3.info("EDA ended")
