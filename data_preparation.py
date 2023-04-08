import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def prepare_data(df):
    # Split the data into independent and dependent variables
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    
    # Scale the independent variables
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y
