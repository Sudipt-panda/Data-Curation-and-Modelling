from sklearn.linear_model import LinearRegression , Ridge
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold

from sklearn import  metrics


import pandas as pd
import numpy as np
import  logging
from pathlib import Path

logger4 = logging.getLogger(__name__)
base_path = Path(__file__).parent

def Analysis(df_preprocessed):
    logger4.info("Machine Learning started")
    data = df_preprocessed.copy()
    # cols = ['User_ID','Product_ID']
    # data.drop(cols, inplace = True, axis =1)
    # b = ['Product_Category_2','Product_Category_3']
    # for i in b:
    #     exec("data.%s.fillna(data.%s.value_counts().idxmax(), inplace=True)" %(i,i))
    # #Train Data
    # X = data.drop(["Purchase"], axis=1)
    # #Encoding and converting to numeral
    # X.Gender = pd.to_numeric(X.Gender)
    # X.Age = pd.to_numeric(X.Age)
    # X.Occupation = pd.to_numeric(X.Occupation)
    # X.City_Category = pd.to_numeric(X.City_Category)
    # X.Stay_In_Current_City_Years = pd.to_numeric(X.Stay_In_Current_City_Years)
    # X.Marital_Status = pd.to_numeric(X.Marital_Status)
    # X.Product_Category_1 = pd.to_numeric(X.Product_Category_1)
    # X.Product_Category_2.replace({"16//":"16"},inplace=True )
    # X.Product_Category_2 = pd.to_numeric(X.Product_Category_2)
    # X.Product_Category_3 = pd.to_numeric(X.Product_Category_3)
    # LE = LabelEncoder()
    # X = X.apply(LE.fit_transform)
    # X.dropna(inplace=True)
    # #Test Data
    # Y = data["Purchase"]
    # SS = StandardScaler()
    # Xs = SS.fit_transform(X)
    # pc = PCA(4)
    # principalComponents = pc.fit_transform(X)
    # principalDf = pd.DataFrame(data = principalComponents, columns = ["component 1", "component 2", "component 3", "component 4"])
    # #Splitting the Data
    # kf = KFold(20)
    # for a,b in kf.split(principalDf):
    #     X_train, X_test = Xs[a],Xs[b]
    #     y_train, y_test = Y[a],Y[b]

    # #Training different models
    # lr = LinearRegression()
    # dtr = DecisionTreeRegressor()
    # rfr = RandomForestRegressor()
    # gbr = GradientBoostingRegressor()

    
    # fit1 = lr.fit(X_train,y_train)
    # fit2 = dtr.fit(X_train,y_train)
    # fit3 = rfr.fit(X_train,y_train)
    # fit4 = gbr.fit(X_train,y_train)

    # print("Accuracy Score of Linear regression on train set",fit1.score(X_train,y_train)*100)
    # print("Accuracy Score of Decision Tree on train set",fit2.score(X_train,y_train)*100)
    # print("Accuracy Score of Random Forests on train set",fit3.score(X_train,y_train)*100)
    # print("Accuracy Score of Gradient Boosting on train set",fit4.score(X_train,y_train)*100)

    # print("Accuracy Score of Linear regression on test set",fit1.score(X_test,y_test)*100)
    # print("Accuracy Score of Decision Tree on test set",fit2.score(X_test,y_test)*100)
    # print("Accuracy Score of Random Forests on test set",fit3.score(X_test,y_test)*100)
    # print("Accuracy Score of Gradient Boosting on testset",fit4.score(X_test,y_test)*100)


    msk = np.random.rand(len(data)) < 0.8

    train_df = data[msk]

    test_df = data[~msk]

#Define target and ID columns:
    target = 'Purchase'
    IDcol = ['User_ID','Product_ID']
    def modelfit(alg, dtrain, dtest, predictors, target, IDcol,filename,modelname):
        
        alg_file_path = (base_path / filename).resolve()
        #Fit the algorithm on the data
        alg.fit(dtrain[predictors], dtrain[target])
        
        #Predict training set:
        dtrain_predictions = alg.predict(dtrain[predictors])
        #Perform cross-validation:
        # cv_score = cross_validate.cross_val_score(alg, dtrain[predictors],(dtrain[target]) , cv=20, scoring='neg_mean_squared_error')
        # cv_score = np.sqrt(np.abs(cv_score))
    
        #Print model report:
        print('\nModel Name is',modelname)
        print("\nModel Report")
        print("RMSE : %.4g" % np.sqrt(metrics.mean_squared_error((dtrain[target]).values, dtrain_predictions)))
        #print("CV Score : Mean - %.4g | Std - %.4g | Min - %.4g | Max - %.4g" % (np.mean(cv_score),np.std(cv_score),np.min(cv_score),np.max(cv_score)))
    
        #Predict on testing data:
        dtest[target] = alg.predict(dtest[predictors])
    
        #Export submission file:
        IDcol.append(target)
        submission = pd.DataFrame({ x: dtest[x] for x in IDcol})
        submission.to_csv(alg_file_path, header=True,index=False)

    LR = LinearRegression(normalize=True)
    predictors = train_df.columns.drop(['Purchase','Product_ID','User_ID'])
    modelfit(LR, train_df, test_df, predictors, target, IDcol,'LR.csv','Linear Regression')
    coef1 = pd.Series(LR.coef_, predictors).sort_values()
    coef1.plot(kind='bar', title='Model Coefficients')

    RR = Ridge(alpha=0.05,normalize=True)
    modelfit(RR, train_df, test_df, predictors, target, IDcol,'RR.csv','Ridge Regression')

    DT = DecisionTreeRegressor(max_depth=15, min_samples_leaf=100)
    modelfit(DT, train_df, test_df, predictors, target, IDcol,'DT.csv','Decision Tree')

    RF = RandomForestClassifier(max_depth=8, min_samples_leaf=150)
    modelfit(RF, train_df, test_df, predictors, target, IDcol,'RF.csv','Random Forest')



    logger4.info("Machine Learning completed")

