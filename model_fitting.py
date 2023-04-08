import statsmodels.api as sm

def fit_model(X, y):
    # Add a constant column to the independent variables
    X = sm.add_constant(X)
    
    # Fit the multiple regression model
    model = sm.OLS(y, X).fit()
    
    return model
