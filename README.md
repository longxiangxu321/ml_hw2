# GEO5017 Assignment 2

## Introduction

The project is to classify point cloud into 5 classes: 'building', 'car', 'fence', 'pole', 'tree' using Support Vector Machine (SVM) and Random Forest (RF)



## Author

- *Longxiang* *Xu* 5722918
- *Bingshiuan* *Tsai* 5511464



## Folder Structure

```
└── hw2/
    ├── data/
    │   ├── pcs/
    │   │   ├── 000.xyz
    │   │   ├── xxx.xyz
    │   │   └── 499.xyz
    │   └── params_test/
    │       ├── result.csv
    │       └── result1.csv
    └── src/
        ├── classification.py
        ├── grid_search_rf.py
        ├── grid_search_svm.py
        ├── refit_strategy.py
        ├── hyperparams_test.py
        └── README.md

```

## Features Engineering

- height
- length
- width
- bbox volume
- eigen value1
- eigen value 2



## Run

The code is tested using python 3.8.

Requirements:

- numpy 1.21.2
- matplotlib 3.5.3
- sckit-learn 1.1.3
- pandas 1.4.3



### classification.py

Run ***classification.py*** to classify the point cloud.



### Optional

#### grid_search_rf.py/grid_search_svm.py 

Run ***grid_search_rf.py*** and ***grid_search_svm.py*** to apply grid search to find the optimal hyperparameters.

The hyperparameters in ***classification.py*** is selected from the two grid search results. The grid search strategies are defined in ***refit_strategy.py***.



The results for ***grid_search_svm.py*** are shown like follows:

```
The selected final model is the fastest to predict out of the previously
selected subset of best models based on OA and mA.
Its scoring time is:

mean_score_time                                      0.000597
mean_test_balanced_accuracy                          0.906856
std_test_balanced_accuracy                           0.031676
mean_test_accuracy                                   0.906667
std_test_accuracy                                     0.03266
rank_test_balanced_accuracy                                 4
rank_test_accuracy                                          4
params                         {'C': 100, 'kernel': 'linear'}
Name: 10, dtype: object

{'C': 100, 'kernel': 'linear'}

Process finished with exit code 0

```



The results for ***grid_search_rf.py*** are shown like follows:

```
The selected final model is the fastest to predict out of the previously
selected subset of best models based on OA and mA.
Its scoring time is:

mean_score_time                                                         0.010267
mean_test_balanced_accuracy                                             0.937731
std_test_balanced_accuracy                                               0.02029
mean_test_accuracy                                                      0.936667
std_test_accuracy                                                       0.019437
rank_test_balanced_accuracy                                                    1
rank_test_accuracy                                                             1
params                         {'max_depth': 10, 'min_samples_leaf': 2, 'min_...
Name: 94, dtype: object
{'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}

Process finished with exit code 0

```



#### hyperparams_test.py

Run the program to apply significant test of hyperparameters of different models. The output should be like:

```
                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:     mean_test_balanced_accuracy   R-squared:                       0.106
Model:                                     OLS   Adj. R-squared:                 -0.342
Method:                          Least Squares   F-statistic:                    0.2360
Date:                         Wed, 29 Mar 2023   Prob (F-statistic):              0.675
Time:                                 19:53:27   Log-Likelihood:                 14.333
No. Observations:                            4   AIC:                            -24.67
Df Residuals:                                2   BIC:                            -25.89
Df Model:                                    1                                         
Covariance Type:                     nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.9134      0.006    160.107      0.000       0.889       0.938
param_C    -5.516e-06   1.14e-05     -0.486      0.675   -5.44e-05    4.33e-05
==============================================================================
Omnibus:                          nan   Durbin-Watson:                   2.188
Prob(Omnibus):                    nan   Jarque-Bera (JB):                0.273
Skew:                          -0.383   Prob(JB):                        0.873
Kurtosis:                       1.975   Cond. No.                         603.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Process finished with exit code 0

```

