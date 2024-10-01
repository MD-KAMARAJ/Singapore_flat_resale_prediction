# Singapore_flat_resale_prediction
Machine Learning Project
This project helps you to Machine Learning predict the Resale flat price of flats in singapore, just by entering the required inputs like Year of prediction, Floor area sqm, Remaining lease, Mid Storey,Flat type and Town in which that flat is located.
# Data collection:
  The Datasets are taken from the Housing Development Borad of Singapore government from the year 1990 till 1st September 2024.
# Data Cleaning:
  The remaining lease is calculated by subtracting 99years from the data of commencement of lease, Mid Storey is calculated by taking the average of storey range
# EDA:
  Skewness is removed by log transformation and also Univariate and Bivariate analysis also made for selecting the feature.
# Outlier Detection:
  Outliers are detected and filtered using IQR method
# Encoding:
  The selected features are year, flat type, town, remaining lease, mid storey and floor area sqm. The categorical features are like flat type and town are mapped from 1 to 7 and 1 to 27
# Sclaing:
  Used Standard Scaler for scaling Features and saved in a variable scaler
  Used Standard Scaler for scaling target feature and saved in a variable scaler_target.
# Model Selection:
  A sample of 20% of total data is taken for model selection and model like Linear Regression, lasso regression, Rigid Regression, Non-Elastic regression, Random forest regression, Decision Tree regression, Gradient boosting regression are tried and Random forest is selected as gives the higher R_Square of 0.9667
# Model Training:
  Now all the data's are splitted using Train-test-split and trained with RandomForestRegressor without target column, and prediction is done with these features for predicting our target feature Resale Price.
# Model Export:
  Now the trianed model is exported using joblib.
# Model Load:
  A new Py file is created and the exported model is loaded and the model and scaler used there are used in this py file for the inputs given by the customer and the prediction of resale flat price is made and shown in the seperate container.
