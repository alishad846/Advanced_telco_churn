import joblib
import pandas as pd

def preprocess_input(df):
    df = df.copy()
    binary_map = {'Yes': 1, 'No': 0}
    for col in ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']:
        df[col] = df[col].map(binary_map)

    df = pd.get_dummies(df)
    feature_cols = joblib.load('models/feature_columns.pkl')

    for col in feature_cols:
        if col not in df.columns:
            df[col] = 0
    df = df[feature_cols]
    return df