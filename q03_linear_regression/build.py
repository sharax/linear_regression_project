# %load q03_linear_regression/build.py
# Default Imports
from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression


# Load the package for linear regression and use load_data() and data_splitter() function
df = load_data('data/house_prices_multivariate.csv')
X, y = data_splitter(df)

def linear_regression(X,y):
    reg=LinearRegression()
    lm=reg.fit(X,y)
    return lm

#type(linear_regression(X,y))
# Your code here
