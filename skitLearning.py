

import pandas as pd

#dataset
stock = {'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
                'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
                'Interest_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
                'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]
                }
#dataframe
df = pd.DataFrame(stock, columns = ['Year', 'Month', 'Interest_Rate', 'Unemployment_Rate', 'Stock_Index_Price'])
print(df)

x = df[['Interest_Rate', 'Unemployment_Rate']].astype(float) # here we have 2 input variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets

y = df['Stock_Index_Price'].astype(float) # output variable (what we are trying to predict)

#1st block to run scikitlearn regression analysis
from sklearn import linear_model

regres = linear_model.LinearRegression()
regres.fit(x,y)
print('Intercept: %.3f\n'%regres.intercept_)
print('Coefficients: \n',regres.coef_)


#2nd block to run STatsmodel regression analysis
import statsmodels.api as sm

x = sm.add_constant(x, prepend = False)

mod = sm.OLS(y, x)
res = mod.fit()
print(res.summary())

#kmeans clustering
from sklearn import cluster

k = 3
clf = cluster.KMeans(init = 'random')
clf.fit(x)

