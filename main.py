import pandas as pd

from src.data_validation import validate_dataset
from src.preprocessing import preprocess_data
from src.model_training import get_models
from src.energy_metrics import measure_performance
from src.task_detection import detect_task_type
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "AQI.csv")

def run_pipeline(file_path, target_column):

    # 1️⃣ Load & validate dataset
    df = validate_dataset(file_path, target_column)

    # 2️⃣ Detect task type
    task_type = detect_task_type(df, target_column)
    print(f"Detected task type: {task_type}")

    # 3️⃣ Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(df, target_column)

    # 4️⃣ Load task-specific models
    models = get_models(task_type)

    results = []

    for name, model in models.items():
        print(f"Training {name}...")

        metrics = measure_performance(
            model,
            X_train, y_train,
            X_test, y_test,
            task_type
        )
        metrics["Model"] = name
        results.append(metrics)

    return pd.DataFrame(results)


# Run directly
if __name__ == "__main__":
    FILE_PATH = "data/raw/user_dataset.csv"
    TARGET_COLUMN = "AQI"   # user-selected

    results_df = run_pipeline(FILE_PATH, TARGET_COLUMN)
    print(results_df)

