from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVR, SVC


def get_models(task_type):
    """
    Returns models based on task type.
    """

    if task_type == "regression":
        return {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(max_depth=10, random_state=42),
            "Random Forest": RandomForestRegressor(n_estimators=50, random_state=42),
            "SVR": SVR()
        }

    else:  # classification
        return {
            "Logistic Regression": LogisticRegression(max_iter=1000),
            "Decision Tree": DecisionTreeClassifier(max_depth=10, random_state=42),
            "Random Forest": RandomForestClassifier(n_estimators=50, random_state=42),
            "SVM": SVC()
        }
