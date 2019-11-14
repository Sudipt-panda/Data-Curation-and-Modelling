
import numpy as np
import pandas as pd
import logging 
from string import punctuation 

logger1 = logging.getLogger(__name__)

def clean_data(df_raw):
    logger1.info("***********************Data Cleaning started**************************")
    df_preprocessed = df_raw.copy()
    #rename columns
    df_preprocessed.columns = ['User_ID', 'Product_ID', 'Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status','Product_Category_1', 'Product_Category_2', 'Product_Category_3', 'Purchase']
    #drop duplicates
    df_preprocessed.drop_duplicates(subset=['User_ID', 'Product_ID'], keep='first', inplace=True)
    #user_id cleaning
    df_preprocessed["User_ID"].replace({"^^1000008": "1000008","1000022$":"M","1000062?":"1000062","1000062#":"1000062","1000008^^":"1000008","^1000163&":"1000163","1000106#":"1000106",
                                        "1000069##":"1000069","1003261%^":"1003261","1000008AS":"1000008","!1000069!":"1000069"},inplace=True)

    #product_id cleaning
    df_preprocessed["Product_ID"].replace({"<P00042342>": "P00042342","~P00194142":"P00194142","<P00144642>?":"P00144642"},inplace=True)
    #Gender Cleaning
    df_preprocessed['Gender'] = df_preprocessed['Gender'].str.upper()
    df_preprocessed['Gender'].replace('P', np.nan, inplace=True)
    df_preprocessed['Gender'].replace('NULL', np.nan, inplace=True)
    df_preprocessed.dropna(subset=['Gender'], inplace=True) 
    df_preprocessed["Gender"].replace({"FEMALE": "F","MALE":"M"},inplace=True)
    #age Cleaning
    df_preprocessed['Age'] = df_preprocessed['Age'].str.upper()
    df_preprocessed['Age'].replace('NULL', np.nan, inplace=True)
    df_preprocessed.dropna(subset=['Age'], inplace=True)
    df_preprocessed["Age"].replace({"Jun-50": "46-50","Dec-45":"36-45","-36":"26-35",
                                "2":"0-17","3":"0-17","12":"0-17","13":"0-17","15":"0-17","45-17":"0-17",
                                "18":"18-25","23":"18-25","24":"18-25","18/25":"18-25","28-25":"18-25",
                                "34":"26-35","46-35":"26-35","26-45":"36-45","16-45":"36-45","36-46":"36-45","36-89":"36-45","46-45":"36-45","76-45":"36-45",
                                "96-50":"46-50","56":"55+"},inplace=True)
    #Occupation Cleaning
    df_preprocessed['Occupation'].replace('Null', np.nan, inplace=True)
    df_preprocessed.dropna(subset=['Occupation'], inplace=True)
    df_preprocessed["Occupation"].replace({'5W':'5','17##':'17','4@@':'4','7##':'7','^^':'0','$$20':'20','Seven':'7','20!!':'20','0.2':'2','#17':'17','@@':'0','3z++':'3','two':'2'},inplace=True)

    #city category cleaning
    df_preprocessed['City_Category'] = df_preprocessed['City_Category'].str.upper()
    df_preprocessed['City_Category'].replace('NULL', np.nan, inplace=True)
    df_preprocessed.dropna(subset=['City_Category'], inplace=True)
    df_preprocessed['City_Category'] = df_preprocessed['City_Category'].str.strip(punctuation)
    df_preprocessed["City_Category"].replace({"B1":"B","B12":"B","B23":"B","C1":"C","C45":"C"},inplace=True)
    #Stay_In_Current_City_Years cleaning
    df_preprocessed['Stay_In_Current_City_Years'].replace('Null', np.nan, inplace=True)
    df_preprocessed.dropna(subset=['Stay_In_Current_City_Years'], inplace=True)
    df_preprocessed['Stay_In_Current_City_Years'] = df_preprocessed['Stay_In_Current_City_Years'].str.strip(punctuation)
    df_preprocessed["Stay_In_Current_City_Years"].replace({"ZERO":"0","ONE":"1","TWO":"2","2years":"2","One":"1","one":"1","zero":"0","Zero":"0"},inplace=True)

    #Marital_Status
    df_preprocessed['Marital_Status'].replace('Null', np.nan, inplace=True)
    df_preprocessed.dropna(subset=['Marital_Status'], inplace=True)
    df_preprocessed["Marital_Status"].replace({"ZERO":"0","ONE":"1","SINGLE":"0","SIN GLE":"0","MARRIED":"1",
                                            "Married":"1","Single":"0","One":"1","single":"0","married":"1","one":"1","Zero":"0","Sin gle":"0","zero":"0","0^^":"0","1@":"1"},inplace=True)

    #Product_Category_1
    df_preprocessed.dropna(subset=['Product_Category_1'], inplace=True)
    df_preprocessed["Product_Category_1"].replace({"1$":"1","3#":"3","4$":"4","5+":"5","5__":"5","7)":"7","8*":"8","14%%":"14"},inplace=True)

    #Product_Category_2
    df_preprocessed["Product_Category_2"].replace({"-13":"13","1}5":"15","-11":"11","~15":"15","10/":"10","14#":"14","14$":"14","14_":"14","16?":"16","6??":"6","6e":"6", "16\\":"16", "2^%":"2"},inplace=True)

    #Product_Category_3
    df_preprocessed["Product_Category_3"].replace({"5__":"5"},inplace=True)

    #Purchase
    df_preprocessed["Purchase"].replace({"~11859":"11859", "6923""":"6923","11{589":"11589","10{073":"10073","71(77":"7177","5331^^":"5331","()15644":"15644","7920??":"7920","19379""":"19379",
                                        "8014@":"8014","#15585":"15585","2167_)":"2167"},inplace=True)
    logger1.info("***********************Data Cleaning completed**************************")
    return df_preprocessed


def process_data(df_data):
    logger1.info("***********************Preprocessing started**************************")
    data = df_data.copy()
    data = data.fillna(0)
    def map_gender(gender):
        if gender == 'M':
            return 1
        else:
            return 0
    data['Gender'] = data['Gender'].apply(map_gender)
    def map_age(age):
        if age == '0-17':
            return 0
        elif age == '18-25':
            return 1
        elif age == '26-35':
            return 2
        elif age == '36-45':
            return 3
        elif age == '46-50':
            return 4
        elif age == '51-55':
            return 5
        else:
            return 6
    data['Age'] = data['Age'].apply(map_age)
    def map_city_categories(city_category):
        if city_category == 'A':
            return 2
        elif city_category == 'B':
            return 1
        else:
            return 0
    data['City_Category'] = data['City_Category'].apply(map_city_categories)
    def map_stay(stay):
        if stay == '4+':
            return 4
        else:
            return int(stay)
    data['Stay_In_Current_City_Years'] = data['Stay_In_Current_City_Years'].apply(map_stay)
    data.Occupation = pd.to_numeric(data.Occupation)    
    data.Marital_Status = pd.to_numeric(data.Marital_Status)
    data.Purchase = pd.to_numeric(data.Purchase)        
    return data




