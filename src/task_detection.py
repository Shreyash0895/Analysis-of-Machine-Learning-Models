def detect_task_type(df, target_column):
    """
    Automatically detect whether the problem is
    regression or classification.
    """

    unique_values = df[target_column].nunique()
    dtype = df[target_column].dtype

    # Classification: few unique values or categorical
    if unique_values <= 10 or dtype == "object":
        return "classification"

    # Otherwise regression
    return "regression"
