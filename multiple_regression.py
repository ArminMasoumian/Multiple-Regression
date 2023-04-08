# Author: Armin Masoumian (masoumian.armin@gmail.com)

import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error

# Load the data
df = pd.read_csv('data.csv')

# Prepare the data
X, y = prepare_data(df)

# Fit the multiple regression model
model = fit_model(X, y)

# Evaluate the model
r2, mse = evaluate_model(model, X, y)

# Print the results
print("R-squared:", r2)
print("Mean squared error:", mse)
print(model.summary())
