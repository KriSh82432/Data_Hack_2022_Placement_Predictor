# -*- coding: utf-8 -*-
"""pawankdsh_PLACEMENT_MODEL EVALUATION USING MSLE_Project_DataSciHack_v1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wK3kPOY2M94FQ4VePl-QR7gCP8MWGzU-

# Project 1: Placement Prediction
Data_Science_Hack

---

### Context

The probability of the placement depends on various factors like CGPA, Internships, projects, etc. Change in the mindset of the millennial generation also contributes to ups and down in placement as the young generation is much into cloud Nine  than to owe a placement. Predicting the right questions for the placement is important for aspiring engineers in the corporate business. This makes it very important to come up with proper and smart technique to estimate the true prediction of the placement.

---

---

### Problem Statement


You are willing to get your placement stats. You are not sure about the placement of yours and want to estimate your placement stats. You are provided with the dataset and need to make a prediction model which will help you to get a good estimate of your placement prediction.

---

### Data Description

The **placement** dataset contains the prices and other attributes. There are $2967$ rows and $18$ attributes (features) with a target column (Age). 

Following are the features:  

|Column|Description|
|---:|
Age	
Internships	
CGPA	
HistoryOfBacklogs	
teamWorking	
problemSolvingskills	
techSkillsLevel	
comSkillsLevel	
resumeLevel	
projectsNo	
easyProjects	
mediumProjects	
hardProjects	
advancedProjects	
personalityLevel	
winnerNo	
runnerNo	
participantNo
  **Dataset Link:**  https://docs.google.com/spreadsheets/d/e/2PACX-1vSVwkDCMjC3YqMd3-aGNIB5gGrUhguSyWGTt6G5_mBuDZ6UcwsCDPRUyLnTVBtp4l8bksEJIXHj0qWL/pub?output=csv

---

### Things To Do

1. Explore the placement dataset by creating the following plots:
   - Box plots between each categorical feature and the `Age`.
   - Scatter plots between the numerical features and the `Age`.
   
2. Convert categorical attributes into numerical attributes using feature encoding.

3. Build a linear regression model by selecting the most relevant features to predict the Age of houses.

4. Evaluate the linear regression model by calculating the parameters such as coefficient of determination, MAE, MSE, RMSE, mean of residuals and by checking for homoscedasticity.

---

#### 1. Import Modules and Load Dataset

**Dataset Link:** https://docs.google.com/spreadsheets/d/e/2PACX-1vSVwkDCMjC3YqMd3-aGNIB5gGrUhguSyWGTt6G5_mBuDZ6UcwsCDPRUyLnTVBtp4l8bksEJIXHj0qWL/pub?output=csv
"""

# Import the required modules and load the dataset.
import joblib
from joblib import Parallel, delayed
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_squared_log_error
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from scipy.stats import norm
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
import pickle
warnings.filterwarnings('ignore')
df = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vSVwkDCMjC3YqMd3-aGNIB5gGrUhguSyWGTt6G5_mBuDZ6UcwsCDPRUyLnTVBtp4l8bksEJIXHj0qWL/pub?output=csv')
df
df.head()

# Get the information on DataFrame.
df.info()

# Check if there are any NULL values.
df.isnull().sum()

features = list(df.columns.values)
features.remove('Age')
features

"""---

#### 2. Exploratory Data Analysis

We need to predict the value of `price` variable, using other variables. Thus, `price` is the target or dependent variable and other columns except `price` are the features or the independent variables. 

Perform the following tasks:

- Create Box plots between each **categorical** variable and the target variable `price` to sense the distribution of values.

- Create the Scatter plots between each **numerical** variable and the target variable `price`. Determine which variable(s) shows linear relationship with the target variable `price`. 

- Create a normal distribution curve for the `price`.
"""

# Check categorical attributes
X = df[features]
y = df['Age']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=29)

# Boxplot for 'Age' vs 'techSkillsLevel'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='Age', y='techSkillsLevel', data=df)
plt.show()

# Boxplot for 'teamWorking' vs 'comSkillsLevel'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='teamWorking', y='comSkillsLevel', data=df)
plt.show()

# Boxplot for 'problemSolvingskills' vs 'techSkillsLevel'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='problemSolvingskills', y='techSkillsLevel', data=df)
plt.show()

# Boxplot for 'winnerNo' vs 'techSkillsLevel'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='winnerNo', y='techSkillsLevel', data=df)
plt.show()

# Boxplot for 'CGPA' vs 'techSkillsLevel'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='CGPA', y='techSkillsLevel', data=df)
plt.show()

# Boxplot for 'CGPA' vs 'problemSolvingskills'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='CGPA', y='problemSolvingskills', data=df)
plt.show()

# Boxplot for 'advancedProjects' vs 'techSkillsLevel'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='advancedProjects', y='techSkillsLevel', data=df)
plt.show()

# Boxplot for 'problemSolvingskills' vs 'hardProjects'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='problemSolvingskills', y='hardProjects', data=df)
plt.show()

# Boxplot for 'resumeLevel' vs 'techSkillsLevel'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='resumeLevel', y='techSkillsLevel', data=df)
plt.show()

# Boxplot for 'techSkillsLevel' vs 'participantNo'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='techSkillsLevel', y='participantNo', data=df)
plt.show()

# Boxplot for 'techSkillsLevel' vs 'runnerNo'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='techSkillsLevel', y='runnerNo', data=df)
plt.show()

# Boxplot for 'advancedProjects' vs 'winnerNo'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='advancedProjects', y='winnerNo', data=df)
plt.show()

# Boxplot for 'advancedProjects' vs 'runnerNo'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='advancedProjects', y='runnerNo', data=df)
plt.show()

# Boxplot for 'techSkillsLevel' vs 'winnerNo'
plt.style.use("dark_background")
plt.figure(figsize=(18, 6))
sns.boxplot(x='techSkillsLevel', y='winnerNo', data=df)
plt.show()

#  scatter plot with 'mediumProjects' on X-axis and 'techSkillsLevel' on Y-axis
plt.figure(figsize=(18, 6))
plt.scatter(x='mediumProjects', y='techSkillsLevel', data=df)
plt.show()

#scatter plot with 'advancedProjects' on X-axis and 'winnerNo' on Y-axis
plt.figure(figsize=(18, 6))
plt.scatter(x='advancedProjects', y='winnerNo', data=df)
plt.show()

#  scatter plot with 'Age' on X-axis and 'personalityLevel' on Y-axis
plt.figure(figsize=(18, 6))
plt.scatter(x='Age', y='personalityLevel', data=df)
plt.show()

# scatter plot with 'easyProjects' on X-axis and 'Internships' on Y-axis
plt.figure(figsize=(18, 6))
plt.scatter(x='easyProjects', y='Internships', data=df)
plt.show()

# Create scatter plot with 'CGPA' on X-axis and 'HistoryOfBacklogs' on Y-axis
plt.figure(figsize=(18, 6))
plt.scatter(x='CGPA', y='HistoryOfBacklogs', data=df)
plt.show()

# Create a normal distribution curve for the 'Internships'.
plt.style.use('ggplot')
plt.figure(figsize=(15, 5))
plt.title('normal distribution curve for the Internships')
sns.distplot(df['Internships'], bins='sturges', hist=False)
plt.grid()
plt.show()
# Create a probablity density function for plotting the normal distribution


# Plot the normal distribution curve using plt.scatter()


features = list(df.columns.values)
features.remove('Age')
features


def myfunc(val, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(val - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

map_out = myfunc(r2_score, 0, 1, 3, 20)


# Create data frames for the features and target again and also split them into the train and test sets.
X = df[features]
y = df['Age']

# Test set will have 33% of the values.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42)

# Add a constant to get an intercept
X_train_sm = sm.add_constant(X_train)

# Fit the regression line using 'OLS'
lr = sm.OLS(y_train, X_train_sm).fit()

# Print the parameters, i.e. the intercept and the slope of the regression line fitted
lr.params

print(lr.summary())

"""---

#### 3. Feature encoding 

Perform feature encoding using `map()` function and one-hot encoding.

---

#### 4. Model Building and Evaluation 

Build a multiple linear regression model using the `statsmodels.api` module.
"""

# Split the 'df' Dataframe into the train and test sets.
train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)
features = list(df.columns)
features.remove('Age')

#separate data-frames for the feature and target variables for both the train and test sets.
X_train = train_df[features]
y_train = train_df['Age']
X_test = test_df[features]
y_test = test_df['Age']

X_train[X_train.columns[:16]] = X_train[X_train.columns[:16]]
X_test[X_test.columns[:16]] = X_test[X_test.columns[:16]]

# Build a linear regression model using all the features to predict placement.

X_train_sm = sm.add_constant(X_train)
lin_reg = sm.OLS(y_train, X_train_sm).fit()


# calculate N and p-values.
num_rows = X_train.shape[0]  # Number of rows or instances
# Number of columns or feature (or independent) variables
num_predictors = X_train.shape[1]
print("Number of rows (N):", num_rows)
print("Number of predictors (p):", num_predictors)


def mean_sq_model(X, y_actual):
    y_pred = lin_reg.predict(X)
    sq_model = (y_pred - y_actual.mean()) ** 2
    msm = sq_model.sum() / (num_predictors - 1)
    return msm


def mean_sq_error(X, y_actual):
    y_pred = lin_reg.predict(X)
    sq_error = (y_actual - y_pred) ** 2
    mse = sq_error.sum() / (num_rows - num_predictors)
    return mse


# Calculate the p-value
f_statistic = mean_sq_model(X_train_sm, y_train) / \
    mean_sq_error(X_train_sm, y_train)
f_statistic

pvalue = (2 * (1 - norm.cdf(abs(f_statistic))))
pvalue

#Find adjusted r squared
num_rows = X_train.shape[0]  # Number of rows or instances
# Number of columns or feature (or independent) variables
num_predictors = X_train.shape[1]
# R-squared (or coefficient of determination) value
r2_score = lin_reg.rsquared
adj_r2_score = 1 - ((1 - r2_score) * (num_rows - 1)) / \
    (num_rows - num_predictors - 1)  # Adjusted R-squared calculation
adj_r2_score

"""**Q:** What is the  adjusted r-squared value?

**A:** -0.0009

---

#### 5. Model Evaluation

Build a multiple linear regression model  using `sklearn` module. Also, evaluate the model by calculating $R^2$, MSE, RMSE, and MAE values.
"""

# Build multiple linear regression model using all the features
X = df[features]
y = df['Age']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)


y_train_reshaped = y_train.values.reshape(-1, 1)
y_test_reshaped = y_test.values.reshape(-1, 1)


sklearn_lin_reg = LinearRegression()
sklearn_lin_reg.fit(X_train, y_train_reshaped)


print("\nConstant".ljust(15, " "), f"{sklearn_lin_reg.intercept_[0]:.6f}")


for item in list(zip(X.columns.values, sklearn_lin_reg.coef_[0])):
  print(f"{item[0]}".ljust(15, " "), f"{item[1]:.6f}")

# Evaluate the linear regression model using the 'r2_score', 'mean_squared_error' & 'mean_absolute_error' functions of the 'sklearn' module.
y_train_predict = sklearn_lin_reg.predict(X_train)
y_test_predict = sklearn_lin_reg.predict(X_test)

#r2_score = r2_score(y_train, y_train_predict)
mean_squared_error = mean_squared_error(y_train, y_train_predict)
mean_absolute_error = mean_absolute_error(y_train, y_train_predict)
print(mean_squared_error, mean_absolute_error)

"""---

#### 6. Recursive Feature Elimination

Find out the best features out of all features using RFE and evaluate the model again.
"""

#  a Python dictionary storing the moderately to highly correlated features with techSkillsLevel and the corresponding correlation values.
#  correlation threshold to be 0.2
major_features = {}
for f in features:
  corr_coef = np.corrcoef(df['techSkillsLevel'], df[f])[0, 1]
  if (corr_coef >= 0.2) or (corr_coef <= -0.2):
    major_features[f] = corr_coef

print("Number of features moderately to highly correlated with techSkillsLevel =",
      len(major_features), "\n")
major_features

#Build multiple linear regression model using all the features selected after RFE
#Split the DataFrame into the train and test sets such that test set has 33% of the values.
#Split the DataFrame into the train and test sets such that test set has 33% of the values.

X = df[features]
y = df['Age']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)


y_train_reshaped = y_train.values.reshape(-1, 1)
y_test_reshaped = y_test.values.reshape(-1, 1)

# Build linear regression model using the 'sklearn.linear_model' module.

sklearn_lin_reg = LinearRegression()
sklearn_lin_reg.fit(X_train, y_train_reshaped)


print("\nConstant".ljust(15, " "), f"{sklearn_lin_reg.intercept_[0]:.6f}")

# Print the names of the features along with the values of their corresponding coefficients.

for item in list(zip(X.columns.values, sklearn_lin_reg.coef_[0])):
  print(f"{item[0]}".ljust(15, " "), f"{item[1]:.6f}")

# Evaluate the linear regression model using the 'r2_score', 'mean_squared_error' & 'mean_absolute_error' functions of the 'sklearn' module.
y_train_pred = sklearn_lin_reg.predict(X_train)
y_test_pred = sklearn_lin_reg.predict(X_test)

print(f"Train Set\n{'-' * 50}")
#print(f"R-squared: {r2_score(y_train_reshaped, y_train_pred):.3f}")
print(
    f"Mean Squared Error: {mean_squared_error(y_train_reshaped, y_train_pred):.3f}")
print(
    f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_train_reshaped, y_train_pred)):.3f}")
print(
    f"Mean Absolute Error: {mean_absolute_error(y_train_reshaped, y_train_pred):.3f}")

"""---

#### 7. Residual (Error) Analysis

Perform residual analysis to check if the residuals (errors) are normally distributed or not. For this, plot the  histogram of the residuals.
"""

# a histogram for the errors obtained in the predicted values for the train set.
train_error = y_train_pred
plt.figure(figsize=(15, 6))
sns.distplot(train_error, bins='sturges')
plt.axvline(x=np.mean(train_error), color='purple')
plt.show()

#  a histogram for the errors obtained in the predicted values for the test set.
test_error = y_test_pred
plt.figure(figsize=(15, 6))
sns.distplot(train_error, bins='sturges')
plt.axvline(x=np.mean(train_error), color='purple')
plt.show()

"""---

8.  Homoscedasticity 

We can Check for Homoscedasticity (constant variance) by creating a scatter plot between the errors and the target variable. Determine whether there is some kind of relationship between the error and the target variable.
"""

#  a scatter plot between the errors and the dependent variable for the train set.
plt.figure(figsize=(15, 7))
plt.scatter(y_train, train_error)
plt.axhline(y=np.mean(train_error), color='red')
plt.show()

"""---

---
"""


# Save the model as a pickle in a file
joblib.dump(sklearn_lin_reg, 'filename.pkl')

# Load the model from the file
knn_from_joblib = joblib.load('filename.pkl')

# Use the loaded model to make predictions
knn_from_joblib.predict(X_test)
