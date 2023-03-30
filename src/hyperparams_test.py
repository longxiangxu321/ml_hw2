import pandas as pd
import statsmodels.api as sm


def significant_test(path, mode):
    # Load the data into a pandas dataframe
    data = pd.read_csv(path)


    # Split the data into dependent and independent variables
    if mode == "RF":
        X = data[['param_max_depth', 'param_min_samples_leaf', 'param_min_samples_split', 'param_n_estimators', 'param_criterion']]
        mapping = {'gini': 1, 'entropy': -1}
        X['param_criterion'] = X['param_criterion'].replace(mapping)
        y = data['mean_test_balanced_accuracy']
        model = sm.OLS(y, sm.add_constant(X)).fit()
        print(model.summary())

    elif mode == "SVM":
        X_rbf = data[data['param_kernel'] == 'rbf'][['param_C', 'param_gamma']]
        y_rbf = data[data['param_kernel'] == 'rbf'][['mean_test_balanced_accuracy']]

        X_poly = data[data['param_kernel'] == 'poly'][['param_C', 'param_degree']]
        y_poly = data[data['param_kernel'] == 'poly']['mean_test_balanced_accuracy']

        X_linear = data[data['param_kernel'] == 'linear'][['param_C']]
        y_linear = data[data['param_kernel'] == 'linear'][['mean_test_balanced_accuracy']]


        model1 = sm.OLS(y_rbf, sm.add_constant(X_rbf)).fit()
        model2 = sm.OLS(y_poly, sm.add_constant(X_poly)).fit()
        model3 = sm.OLS(y_linear, sm.add_constant(X_linear)).fit()

        print(model1.summary())
        print(model2.summary())
        print(model3.summary())
    # Fit the regression model

    # Print the coefficient estimates and p-values for each independent variable


def main():
    rf = "../data/params_test/result_RF.csv"
    svm = "../data/params_test/result_SVM.csv"

    print("Significant test for hyperparameters of RF:")
    significant_test(rf, mode="RF")

    print("Significant test for hyperparameters of SVM:")
    significant_test(svm, mode="SVM")


if __name__ == '__main__':
    main()
