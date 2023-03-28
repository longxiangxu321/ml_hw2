# Features

- heightest elevation
  - cars and fences have lower values
- relative height
  - cars and fences have lower values
- bbox volume
  - houses have larger values
  - cars have lower values

- eigen value1
- eigen value 2
- eigen value 3





- height/length
  - poles have higher values, fence have lower values
  - houses have lower values
- height/width
  - houses have lower values
- Squareness(width/length)
  - cars and houses have higher values



```
starting grid search
All grid-search results:
accuracy: 0.633 (±0.042), balanced accuracy: 0.635 (±0.046), for {'C': 1, 'gamma': 0.001, 'kernel': 'rbf'}
accuracy: 0.560 (±0.050), balanced accuracy: 0.557 (±0.059), for {'C': 1, 'gamma': 0.0001, 'kernel': 'rbf'}
accuracy: 0.723 (±0.031), balanced accuracy: 0.726 (±0.030), for {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
accuracy: 0.723 (±0.044), balanced accuracy: 0.725 (±0.049), for {'C': 10, 'gamma': 0.0001, 'kernel': 'rbf'}
accuracy: 0.720 (±0.032), balanced accuracy: 0.722 (±0.032), for {'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}
accuracy: 0.787 (±0.041), balanced accuracy: 0.790 (±0.041), for {'C': 100, 'gamma': 0.0001, 'kernel': 'rbf'}
accuracy: 0.720 (±0.032), balanced accuracy: 0.722 (±0.032), for {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}
accuracy: 0.813 (±0.032), balanced accuracy: 0.814 (±0.034), for {'C': 1000, 'gamma': 0.0001, 'kernel': 'rbf'}
accuracy: 0.917 (±0.032), balanced accuracy: 0.917 (±0.033), for {'C': 1, 'kernel': 'linear'}
accuracy: 0.917 (±0.026), balanced accuracy: 0.917 (±0.024), for {'C': 10, 'kernel': 'linear'}
accuracy: 0.907 (±0.033), balanced accuracy: 0.907 (±0.032), for {'C': 100, 'kernel': 'linear'}
accuracy: 0.917 (±0.030), balanced accuracy: 0.916 (±0.029), for {'C': 1000, 'kernel': 'linear'}

Models with an accuracy higher than 0.8:
accuracy: 0.813 (±0.032), balanced accuracy: 0.814 (±0.034), for {'C': 1000, 'gamma': 0.0001, 'kernel': 'rbf'}
accuracy: 0.917 (±0.032), balanced accuracy: 0.917 (±0.033), for {'C': 1, 'kernel': 'linear'}
accuracy: 0.917 (±0.026), balanced accuracy: 0.917 (±0.024), for {'C': 10, 'kernel': 'linear'}
accuracy: 0.907 (±0.033), balanced accuracy: 0.907 (±0.032), for {'C': 100, 'kernel': 'linear'}
accuracy: 0.917 (±0.030), balanced accuracy: 0.916 (±0.029), for {'C': 1000, 'kernel': 'linear'}

Out of the previously selected high accuracy models, we keep all the
the models within one standard deviation of the highest balanced accuracy model:
accuracy: 0.917 (±0.032), balanced accuracy: 0.917 (±0.033), for {'C': 1, 'kernel': 'linear'}
accuracy: 0.917 (±0.026), balanced accuracy: 0.917 (±0.024), for {'C': 10, 'kernel': 'linear'}
accuracy: 0.907 (±0.033), balanced accuracy: 0.907 (±0.032), for {'C': 100, 'kernel': 'linear'}
accuracy: 0.917 (±0.030), balanced accuracy: 0.916 (±0.029), for {'C': 1000, 'kernel': 'linear'}


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

Process finished with exit code 0

```



```
All grid-search results:
accuracy: 0.920 (±0.016), balanced accuracy: 0.921 (±0.019), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.923 (±0.023), balanced accuracy: 0.926 (±0.024), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.016), balanced accuracy: 0.924 (±0.014), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.929 (±0.024), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.023), balanced accuracy: 0.910 (±0.020), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.930 (±0.019), balanced accuracy: 0.933 (±0.020), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.913 (±0.019), balanced accuracy: 0.916 (±0.020), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.923 (±0.034), balanced accuracy: 0.925 (±0.034), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.027), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.917 (±0.030), balanced accuracy: 0.920 (±0.030), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.907 (±0.029), balanced accuracy: 0.910 (±0.026), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.031), balanced accuracy: 0.909 (±0.029), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.917 (±0.026), balanced accuracy: 0.919 (±0.025), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.903 (±0.012), balanced accuracy: 0.905 (±0.012), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.917 (±0.028), balanced accuracy: 0.920 (±0.028), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.913 (±0.024), balanced accuracy: 0.916 (±0.024), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.910 (±0.031), balanced accuracy: 0.914 (±0.030), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.024), balanced accuracy: 0.903 (±0.024), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.923 (±0.020), balanced accuracy: 0.927 (±0.019), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.920 (±0.022), balanced accuracy: 0.924 (±0.021), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.900 (±0.038), balanced accuracy: 0.904 (±0.036), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.917 (±0.035), balanced accuracy: 0.920 (±0.033), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.023), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.923 (±0.023), balanced accuracy: 0.927 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.920 (±0.019), balanced accuracy: 0.923 (±0.019), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.917 (±0.030), balanced accuracy: 0.920 (±0.029), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.916 (±0.037), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.917 (±0.035), balanced accuracy: 0.920 (±0.035), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.033), balanced accuracy: 0.904 (±0.032), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.903 (±0.034), balanced accuracy: 0.908 (±0.033), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.913 (±0.027), balanced accuracy: 0.917 (±0.026), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.923 (±0.023), balanced accuracy: 0.927 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.031), balanced accuracy: 0.911 (±0.028), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.903 (±0.036), balanced accuracy: 0.908 (±0.034), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.913 (±0.027), balanced accuracy: 0.917 (±0.025), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.023), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.917 (±0.018), balanced accuracy: 0.918 (±0.017), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.026), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.883 (±0.024), balanced accuracy: 0.886 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.900 (±0.042), balanced accuracy: 0.904 (±0.041), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.907 (±0.040), balanced accuracy: 0.910 (±0.039), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.917 (±0.035), balanced accuracy: 0.920 (±0.034), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.883 (±0.024), balanced accuracy: 0.886 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.900 (±0.042), balanced accuracy: 0.904 (±0.041), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.907 (±0.040), balanced accuracy: 0.910 (±0.039), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.917 (±0.035), balanced accuracy: 0.920 (±0.034), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.900 (±0.011), balanced accuracy: 0.901 (±0.010), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.910 (±0.036), balanced accuracy: 0.914 (±0.035), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.910 (±0.029), balanced accuracy: 0.913 (±0.028), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.907 (±0.034), balanced accuracy: 0.911 (±0.033), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.920 (±0.016), balanced accuracy: 0.921 (±0.019), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.923 (±0.023), balanced accuracy: 0.926 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.016), balanced accuracy: 0.924 (±0.014), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.929 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.023), balanced accuracy: 0.910 (±0.020), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.930 (±0.019), balanced accuracy: 0.933 (±0.020), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.913 (±0.019), balanced accuracy: 0.916 (±0.020), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.923 (±0.034), balanced accuracy: 0.925 (±0.034), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.027), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.917 (±0.030), balanced accuracy: 0.920 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.907 (±0.029), balanced accuracy: 0.910 (±0.026), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.031), balanced accuracy: 0.909 (±0.029), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.917 (±0.026), balanced accuracy: 0.919 (±0.025), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.903 (±0.012), balanced accuracy: 0.905 (±0.012), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.917 (±0.028), balanced accuracy: 0.920 (±0.028), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.913 (±0.024), balanced accuracy: 0.916 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.910 (±0.031), balanced accuracy: 0.914 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.920 (±0.016), balanced accuracy: 0.921 (±0.019), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.923 (±0.023), balanced accuracy: 0.926 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.016), balanced accuracy: 0.924 (±0.014), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.929 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.023), balanced accuracy: 0.910 (±0.020), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.930 (±0.019), balanced accuracy: 0.933 (±0.020), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.913 (±0.019), balanced accuracy: 0.916 (±0.020), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.923 (±0.034), balanced accuracy: 0.925 (±0.034), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.027), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.917 (±0.030), balanced accuracy: 0.920 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.907 (±0.029), balanced accuracy: 0.910 (±0.026), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.031), balanced accuracy: 0.909 (±0.029), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.917 (±0.026), balanced accuracy: 0.919 (±0.025), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.903 (±0.012), balanced accuracy: 0.905 (±0.012), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.917 (±0.028), balanced accuracy: 0.920 (±0.028), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.913 (±0.024), balanced accuracy: 0.916 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.910 (±0.031), balanced accuracy: 0.914 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 500}

Models with an accuracy higher than 0.8:
accuracy: 0.920 (±0.016), balanced accuracy: 0.921 (±0.019), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.923 (±0.023), balanced accuracy: 0.926 (±0.024), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.016), balanced accuracy: 0.924 (±0.014), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.929 (±0.024), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.023), balanced accuracy: 0.910 (±0.020), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.930 (±0.019), balanced accuracy: 0.933 (±0.020), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.913 (±0.019), balanced accuracy: 0.916 (±0.020), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.923 (±0.034), balanced accuracy: 0.925 (±0.034), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.027), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.917 (±0.030), balanced accuracy: 0.920 (±0.030), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.907 (±0.029), balanced accuracy: 0.910 (±0.026), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.031), balanced accuracy: 0.909 (±0.029), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.917 (±0.026), balanced accuracy: 0.919 (±0.025), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.903 (±0.012), balanced accuracy: 0.905 (±0.012), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.917 (±0.028), balanced accuracy: 0.920 (±0.028), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.913 (±0.024), balanced accuracy: 0.916 (±0.024), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.910 (±0.031), balanced accuracy: 0.914 (±0.030), for {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.024), balanced accuracy: 0.903 (±0.024), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.923 (±0.020), balanced accuracy: 0.927 (±0.019), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.920 (±0.022), balanced accuracy: 0.924 (±0.021), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.900 (±0.038), balanced accuracy: 0.904 (±0.036), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.917 (±0.035), balanced accuracy: 0.920 (±0.033), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.023), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.923 (±0.023), balanced accuracy: 0.927 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.920 (±0.019), balanced accuracy: 0.923 (±0.019), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.917 (±0.030), balanced accuracy: 0.920 (±0.029), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.916 (±0.037), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.917 (±0.035), balanced accuracy: 0.920 (±0.035), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.033), balanced accuracy: 0.904 (±0.032), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.903 (±0.034), balanced accuracy: 0.908 (±0.033), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.913 (±0.027), balanced accuracy: 0.917 (±0.026), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.923 (±0.023), balanced accuracy: 0.927 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.031), balanced accuracy: 0.911 (±0.028), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.903 (±0.036), balanced accuracy: 0.908 (±0.034), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.913 (±0.027), balanced accuracy: 0.917 (±0.025), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.023), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.917 (±0.018), balanced accuracy: 0.918 (±0.017), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.026), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.883 (±0.024), balanced accuracy: 0.886 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.900 (±0.042), balanced accuracy: 0.904 (±0.041), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.907 (±0.040), balanced accuracy: 0.910 (±0.039), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.917 (±0.035), balanced accuracy: 0.920 (±0.034), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.883 (±0.024), balanced accuracy: 0.886 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.900 (±0.042), balanced accuracy: 0.904 (±0.041), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.907 (±0.040), balanced accuracy: 0.910 (±0.039), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.917 (±0.035), balanced accuracy: 0.920 (±0.034), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.900 (±0.011), balanced accuracy: 0.901 (±0.010), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.910 (±0.036), balanced accuracy: 0.914 (±0.035), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.910 (±0.029), balanced accuracy: 0.913 (±0.028), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.907 (±0.034), balanced accuracy: 0.911 (±0.033), for {'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.920 (±0.016), balanced accuracy: 0.921 (±0.019), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.923 (±0.023), balanced accuracy: 0.926 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.016), balanced accuracy: 0.924 (±0.014), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.929 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.023), balanced accuracy: 0.910 (±0.020), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.930 (±0.019), balanced accuracy: 0.933 (±0.020), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.913 (±0.019), balanced accuracy: 0.916 (±0.020), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.923 (±0.034), balanced accuracy: 0.925 (±0.034), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.027), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.917 (±0.030), balanced accuracy: 0.920 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.907 (±0.029), balanced accuracy: 0.910 (±0.026), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.031), balanced accuracy: 0.909 (±0.029), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.917 (±0.026), balanced accuracy: 0.919 (±0.025), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.903 (±0.012), balanced accuracy: 0.905 (±0.012), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.917 (±0.028), balanced accuracy: 0.920 (±0.028), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.913 (±0.024), balanced accuracy: 0.916 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.910 (±0.031), balanced accuracy: 0.914 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.920 (±0.016), balanced accuracy: 0.921 (±0.019), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.923 (±0.023), balanced accuracy: 0.926 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.016), balanced accuracy: 0.924 (±0.014), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.929 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.023), balanced accuracy: 0.910 (±0.020), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.930 (±0.019), balanced accuracy: 0.933 (±0.020), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.913 (±0.019), balanced accuracy: 0.916 (±0.020), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.923 (±0.034), balanced accuracy: 0.925 (±0.034), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.027), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.917 (±0.030), balanced accuracy: 0.920 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.907 (±0.029), balanced accuracy: 0.910 (±0.026), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.907 (±0.031), balanced accuracy: 0.909 (±0.029), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.917 (±0.024), balanced accuracy: 0.921 (±0.022), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.917 (±0.026), balanced accuracy: 0.919 (±0.025), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.024), balanced accuracy: 0.923 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.900 (±0.021), balanced accuracy: 0.902 (±0.021), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 10}
accuracy: 0.910 (±0.043), balanced accuracy: 0.913 (±0.042), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.913 (±0.039), balanced accuracy: 0.917 (±0.037), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.913 (±0.027), balanced accuracy: 0.918 (±0.025), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.903 (±0.012), balanced accuracy: 0.905 (±0.012), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 10}
accuracy: 0.917 (±0.028), balanced accuracy: 0.920 (±0.028), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.913 (±0.024), balanced accuracy: 0.916 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.910 (±0.031), balanced accuracy: 0.914 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 500}

Out of the previously selected high accuracy models, we keep all the
the models within one standard deviation of the highest balanced accuracy model:
accuracy: 0.923 (±0.023), balanced accuracy: 0.926 (±0.024), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.927 (±0.023), balanced accuracy: 0.929 (±0.024), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.930 (±0.019), balanced accuracy: 0.933 (±0.020), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.923 (±0.034), balanced accuracy: 0.925 (±0.034), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.027), for {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.923 (±0.020), balanced accuracy: 0.927 (±0.019), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.920 (±0.022), balanced accuracy: 0.924 (±0.021), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.923 (±0.023), balanced accuracy: 0.927 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.923 (±0.023), balanced accuracy: 0.927 (±0.022), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.026), for {'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.923 (±0.023), balanced accuracy: 0.926 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.927 (±0.023), balanced accuracy: 0.929 (±0.024), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.930 (±0.019), balanced accuracy: 0.933 (±0.020), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.923 (±0.034), balanced accuracy: 0.925 (±0.034), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.027), for {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.923 (±0.023), balanced accuracy: 0.926 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}
accuracy: 0.927 (±0.023), balanced accuracy: 0.929 (±0.024), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.923 (±0.017), balanced accuracy: 0.927 (±0.016), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 50}
accuracy: 0.930 (±0.019), balanced accuracy: 0.933 (±0.020), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.923 (±0.034), balanced accuracy: 0.925 (±0.034), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.923 (±0.027), balanced accuracy: 0.926 (±0.027), for {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 500}
accuracy: 0.920 (±0.019), balanced accuracy: 0.924 (±0.018), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}
accuracy: 0.927 (±0.023), balanced accuracy: 0.930 (±0.023), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 500}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 50}
accuracy: 0.927 (±0.031), balanced accuracy: 0.929 (±0.030), for {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 100}


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

