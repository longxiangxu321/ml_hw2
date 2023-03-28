# GEO5017 Assignment 2

## Introduction

The project is to classify point cloud into 5 classes: 'building', 'car', 'fence', 'pole', 'tree' using Support Vector Machine (SVM) and Random Forest (RF)



## Author

- *Longxiang* *Xu* 5722918
- *Bingshiuan* *Tsai* 5511464



## Folder Structure

```
hw2/
├─ data/
│  ├─ 000.xyz/
│  ├─ 499.xyz
├─ src/
│  ├─ classification.py
│  ├─ grid_search_rf.py
│  ├─ grid_search_svm.py
│  ├─ refit_strategy.py
├─ README.md

```

## Features Engineering

- heightest elevation
  - cars and fences have lower values
- relative height
  - cars and fences have lower values
- length
- width
- bbox volume
  - houses have larger values
  - cars have lower values
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



### grid_search_rf.py/grid_search_svm.py (Optional)

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

mean_score_time                                                         0.002408
mean_test_balanced_accuracy                                             0.926422
std_test_balanced_accuracy                                               0.02374
mean_test_accuracy                                                      0.923333
std_test_accuracy                                                       0.022608
rank_test_balanced_accuracy                                                   29
rank_test_accuracy                                                            22
params                         {'max_depth': 20, 'min_samples_leaf': 1, 'min_...
Name: 109, dtype: object

{'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}

Process finished with exit code 0

```

