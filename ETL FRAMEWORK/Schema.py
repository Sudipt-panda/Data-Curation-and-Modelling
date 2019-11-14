import pandas as pd
import numpy as np
import logging
import sys

logger2 = logging.getLogger(__name__)
def create_star_schema(df_pre_processed,**kwargs):
    logger2.info("***********************Creating star schema started**************************")
    try:
       
        # Dimension tables
        
        # User dimension
        df_user = df_pre_processed.loc[ : , ['User_ID', 'Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status' ]]
  

        # Product dimension
        df_prod = df_pre_processed.loc[ : , ['Product_ID','Product_Category_1', 'Product_Category_2', 'Product_Category_3'] ]


        # Fact tables

        # Item_outlet fact  
        df_fact = df_pre_processed.loc[ : , ['User_ID','Product_ID','Purchase'] ]
  

        # Unique ids for the dimension tables

        # Sort the df_prod dataframe in ascending order based on User_ID and remove duplicates
        df_user.drop_duplicates(subset=['User_ID'], keep='first', inplace=True)


        # Sort the df_prod dataframe in ascending order based on Product_ID and remove duplicates
        df_prod.drop_duplicates(subset=['Product_ID'], keep='first', inplace=True)


        # check if any composite key ['User_ID', 'Product_ID'] is getting repeated 
        df_fact.drop_duplicates(subset=['User_ID', 'Product_ID'], keep='first', inplace=True)

        # Export the Star Schema and save them as .csv files
        df_fact.to_csv(kwargs["fact_output"], header=True,index=False)
        df_user.to_csv(kwargs["cust_dim_output"], header=True,index=False)
        df_prod.to_csv(kwargs["prod_dim_output"], header=True,index=False)

        logger2.info("***********************Creating star schema completed**************************")
    except Exception as e:
        logger2.error(e.with_traceback())
        print(e)



 
