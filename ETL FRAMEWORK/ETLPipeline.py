import pandas as  pd
import DataCleaning
import Schema
import EDA
import MachineLearning
import logging
from pathlib import Path

base_path = Path(__file__).parent
# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=(base_path / "../myapp.log").resolve(),
                    filemode='w')

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)


#####################################
#           extract                 #
#####################################

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('*******************Extracting********************')

fact_output = (base_path / "../blackfridayFact.csv")
cust_dim_output = (base_path / "../CustDim.csv")
prod_dim_output = (base_path / "../ProdDim.csv")
staged_output = (base_path / "../StagedData.csv")

df = pd.read_excel(r'/Users/sudiptkumarpanda/Downloads/Black_Friday-2.xlsx')

if __name__ == "__main__":

    #####################################
    #       staging/transform area      #
    #####################################

    # preprocess the data
    df_cleaned = DataCleaning.clean_data(df)
    df_preprocessed = DataCleaning.process_data(df_cleaned)

    df_preprocessed.to_csv(staged_output, header=True,index=False)
    #####################################
    #        transform & load           #
    #####################################

    # Create star schema and load to destination
    Schema.create_star_schema(df_cleaned, **{ 
                                "fact_output": fact_output, "cust_dim_output": cust_dim_output, "prod_dim_output": prod_dim_output})


    #Extended Star Schema
    print('Creating an Extended Star Schema, by joining with external Data Sources')
    #User and Occupation
    df_U = pd.read_csv(r'/Users/sudiptkumarpanda/Downloads/Data Management 2 - Python Codes-20191110/CustDim.csv')
    df_O = pd.read_csv(r'/Users/sudiptkumarpanda/Downloads/Data Management 2 - Python Codes-20191110/ETL FRAMEWORK/data/External/Occupation_Categories.csv')

    merged_inner_cust = pd.merge(left=df_U,right=df_O, left_on='Occupation', right_on='Occupation_ID')
    print(merged_inner_cust)

    #Product and Product_Category
    df_P = pd.read_csv(r'/Users/sudiptkumarpanda/Downloads/Data Management 2 - Python Codes-20191110/ProdDim.csv')
    df_PC = pd.read_csv(r'/Users/sudiptkumarpanda/Downloads/Data Management 2 - Python Codes-20191110/ETL FRAMEWORK/data/External/Product_Categories.csv')

    merged_inner = pd.merge(left=df_P,right=df_PC, left_on='Product_Category_1', right_on='Category_ID')

    newdf = merged_inner[['Product_ID','Category_Description','Product_Category_2','Product_Category_3']].copy()
    newdf.columns = ['Product_ID','Product_Category_1','Product_Category_2','Product_Category_3']

    merged_inner = pd.merge(left=newdf,right=df_PC, left_on='Product_Category_2', right_on='Category_ID')
    newdf = merged_inner[['Product_ID','Product_Category_1','Category_Description','Product_Category_3']].copy()
    newdf.columns = ['Product_ID','Product_Category_1','Product_Category_2','Product_Category_3']

    merged_inner = pd.merge(left=newdf,right=df_PC, left_on='Product_Category_3', right_on='Category_ID')
    newdf = merged_inner[['Product_ID','Product_Category_1','Product_Category_2','Category_Description']].copy()
    newdf.columns = ['Product_ID','Product_Category_1','Product_Category_2','Product_Category_3']
    print(newdf)



    #####################################
    #   Exploratory Data Analysis(EDA)  #
    #####################################

    # Analyse the Data
    EDA.EDA(df_preprocessed)

    #####################################
    #   Machine Learning/Prediction     #
    #####################################

    df_ML = pd.read_csv(r'/Users/sudiptkumarpanda/Downloads/Data Management 2 - Python Codes-20191110/StagedData.csv')
    # Predict the Data
    MachineLearning.Analysis(df_ML)

logging.info('*******************Thank You********************')

