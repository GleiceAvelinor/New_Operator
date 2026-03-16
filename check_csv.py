import pandas as pd
import os

DATA_PATH = r"c:\Users\ednar\OneDrive\Imagens\recog_system\gesture_dataset.csv"

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    print(f"Columns: {df.columns.tolist()[:5]}")
    print(f"First row: {df.iloc[0].values[:5]}")
else:
    print("File not found")
