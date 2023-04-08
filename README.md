# Multiple-Regression
This repository contains code for multiple regression analysis in Python.

## Introduction
Multiple regression is a statistical technique used to model the relationship between a dependent variable and two or more independent variables. It is often used in predictive modeling to determine how much of the variation in the dependent variable can be explained by the independent variables.

This repository contains Python code for multiple regression analysis, including data preparation, model fitting, and model evaluation.

## Getting Started
To use this code, you will need to have Python 3 installed on your computer, as well as the required Python packages listed in requirements.txt. To install these packages, run the following command:

```
pip install -r requirements.txt
```
Next, clone this repository to your local machine:

```
git clone https://github.com/yourusername/multiple-regression.git
```
Finally, navigate to the src directory and run the Python scripts:

```
cd multiple-regression/src
python data_preparation.py
python model_fitting.py
python model_evaluation.py
```

## Example Datasets
The data/ directory contains example datasets for multiple regression analysis. These datasets are in CSV format and contain the following columns:

y: The dependent variable.

x1: The first independent variable.

x2: The second independent variable.

x3: The third independent variable.

x4: The fourth independent variable.

## Results
# YAML

R-squared: 0.9999999981720666
Mean squared error: 2.7781461863772163
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       1.000
Model:                            OLS   Adj. R-squared:                  1.000
Method:                 Least Squares   F-statistic:                 4.421e+08
Date:                Fri, 08 Apr 2023   Prob (F-statistic):           1.11e-08
Time:                        00:00:00   Log-Likelihood:                -12.734
No. Observations:                   9   AIC:                             33.47
Df Residuals:                       4   BIC:                             34.28
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
const           44.9333      2.047     21.962      0.000      38.658      51.208
x1               1.5167      0.128     11.838      0.000       1.166       1.868
x2               3.7833      0.630      6.009      0.003       2.149       5.417
x3              -0.4750      0.252     -1.883      0.133      -1.237       0.287
x4              -0.2250      0.088     -2.555      0.065      -0.477       0.027
==============================================================================
Omnibus:                        0.276   Durbin-Watson:                   1.848
Prob(Omnibus):                  0.871   Jarque-Bera (JB):                0.086
Skew:                          -0.155   Prob(JB):                        0.958
Kurtosis:                       2.734   Cond. No.                         142.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 142. This might indicate that there are
strong multicollinearity or other numerical problems.




