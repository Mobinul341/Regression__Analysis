# Regression__Analysis
This is the program from the course ASDS04 - Introduction to Data science with Python.

#Goriber_Try


This program is about Linear regression with 2 popular libraries on python. First library is ScikitLearn. We called Linear_model from scikitlearn by importing this,

from sklearn import linear_model

By importing this, we have used Linear_model's Ordinary least squares features. To study more of it, visit this
https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares

Here we have used LinearRegression(), fit(), coef_, intercept_ functions. You will find details of this functions from this URL
https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares

Next we have used Statsmodel library with api methods as 

import statsmodels.api as sm

If someone face the problem on importing the library, it means you don't have this in Anaconda (Mine wasn't). Then you need to download and install the library by writing this in CMD / Powershell, the command is - 

conda install -c conda-forge statsmodels

This program has used add__constant(), OLS(), fit(), summary() - these methods. To study in details, visit the URL-
https://www.statsmodels.org/stable/gettingstarted.html

Run only the portions of 1st block and 2nd block by pressing F9 button. What is 1st block and 2nd block, see the code comment please. 

Also check the comments inside the program to understand why here is used multiple regression and how to analyze single regression.
Hope it helps, happy pythonning

