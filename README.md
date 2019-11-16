# Data-Curation-and-Modelling
University Project to create a Data Pipeline implementing ETL worflow and then Doing some ML Analysis and Predictions

The whole pipeline is made in python and the generated files (stageed data, dimension and fact tables, also the prediction model outputs) are stored locally in .csv format.
Black friday dataset is a .xlsx file, which is then cleaned and pre-processed using the DataCleaning.py files. Then Exploratory Data Analysis is done in the EDA.py file which is used to find co-relation between different variables. Then the prediction models are run in MachineLearning.py file. Four different algorithms are used for prediction i.e. Linear Regression, Ridge Regression, Decision Tree and Random Forest. It is found that Linear Regression and Ridge Regression return the same accuracy, also the best accuracy from all the models.
All the operations, creation of pipeline (calling the above mentioned files) and log-keeping is done in the ETLPipeline.py file.
The files are stored locally which can be made generic by inserting the files in a database, (for example mysql Db) with the use of python-sql connectors.
