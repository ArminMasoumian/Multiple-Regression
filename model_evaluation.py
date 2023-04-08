from sklearn.metrics import r2_score, mean_squared_error

def evaluate_model(model, X, y):
    # Add a constant column to the independent variables
    X = sm.add_constant(X)
    
    # Make predictions with the model
    y_pred = model.predict(X)
    
    # Calculate R-squared and mean squared error
    r2 = r2_score(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    
    return r2, mse
