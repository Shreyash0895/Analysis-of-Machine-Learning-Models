import pandas as pd

from src.data_validation import validate_dataset
from src.preprocessing import preprocess_data
from src.model_training import get_models
from src.energy_metrics import measure_performance
from src.task_detection import detect_task_type
import os

"""BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "AQI.csv")"""

def run_pipeline(file_path, target_column):

  from src.data_validation import validate_dataframe

def run_pipeline(df, target_column):
    df = validate_dataframe(df, target_column)

    # continue with preprocessing, training, evaluation
    return df





