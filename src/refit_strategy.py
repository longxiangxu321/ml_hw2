import pandas as pd
import os

def print_dataframe(filtered_cv_results):
    """Pretty print for filtered dataframe"""
    for mean_accuracy, std_accuracy, mean_balanced_accuracy, std_balanced_accuracy, params in zip(
        filtered_cv_results["mean_test_accuracy"],
        filtered_cv_results["std_test_accuracy"],
        filtered_cv_results["mean_test_balanced_accuracy"],
        filtered_cv_results["std_test_balanced_accuracy"],
        filtered_cv_results["params"],
    ):

        print(
            f"accuracy: {mean_accuracy:0.3f} (±{std_accuracy:0.03f}),"
            f" balanced accuracy: {mean_balanced_accuracy:0.3f} (±{std_balanced_accuracy:0.03f}),"
            f" for {params}"
        )
    print()


def refit_strategy(cv_results):
    """Define the strategy to select the best estimator.

    The strategy defined here is to filter-out all results below an accuracy threshold
    of 0.8, rank the remaining by balanced accuracy and keep all models with one standard
    deviation of the best by balanced accuracy. Once these models are selected, we can select the
    fastest model to predict.

    Parameters
    ----------
    cv_results : dict of numpy (masked) ndarrays
        CV results as returned by the `GridSearchCV`.

    Returns
    -------
    best_index : int
        The index of the best estimator as it appears in `cv_results`.
    """
    # print the info about the grid-search for the different scores
    accuracy_threshold = 0.90

    cv_results_ = pd.DataFrame(cv_results)
    print("All grid-search results:")
    print_dataframe(cv_results_)

    if os.path.isfile("../data/params_test/result.csv"):
        cv_results_.to_csv("../data/params_test/result1.csv")
    else:
        cv_results_.to_csv("../data/params_test/result.csv")

    # Filter-out all results below the threshold
    high_accuracy_cv_results = cv_results_[
        cv_results_["mean_test_accuracy"] > accuracy_threshold
    ]

    print(f"Models with an accuracy higher than {accuracy_threshold}:")
    print_dataframe(high_accuracy_cv_results)

    high_accuracy_cv_results = high_accuracy_cv_results[
        [
            "mean_score_time",
            "mean_test_balanced_accuracy",
            "std_test_balanced_accuracy",
            "mean_test_accuracy",
            "std_test_accuracy",
            "rank_test_balanced_accuracy",
            "rank_test_accuracy",
            "params",
        ]
    ]

    # Select the most performant models in terms of balanced accuracy
    # (within 1 sigma from the best)
    best_balanced_accuracy_std = high_accuracy_cv_results["mean_test_balanced_accuracy"].std()
    best_balanced_accuracy = high_accuracy_cv_results["mean_test_balanced_accuracy"].max()
    best_balanced_accuracy_threshold = best_balanced_accuracy - best_balanced_accuracy_std

    high_balanced_accuracy_cv_results = high_accuracy_cv_results[
        high_accuracy_cv_results["mean_test_balanced_accuracy"] > best_balanced_accuracy_threshold
    ]
    print(
        "Out of the previously selected high accuracy models, we keep all the\n"
        "the models within one standard deviation of the highest balanced accuracy model:"
    )
    print_dataframe(high_balanced_accuracy_cv_results)

    # From the best candidates, select the fastest model to predict
    fastest_top_balanced_accuracy_high_accuracy_index = high_balanced_accuracy_cv_results[
        "mean_score_time"
    ].idxmin()

    selected_model = high_balanced_accuracy_cv_results.loc[fastest_top_balanced_accuracy_high_accuracy_index]
    hyperparameters = selected_model["params"]

    print(
        "\nThe selected final model is the fastest to predict out of the previously\n"
        "selected subset of best models based on OA and mA.\n"
        "Its scoring time is:\n\n"
        f"{selected_model}"
    )

    print(hyperparameters)


    return fastest_top_balanced_accuracy_high_accuracy_index