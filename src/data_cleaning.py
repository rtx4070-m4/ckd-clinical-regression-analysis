
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_clean(path):
    df = pd.read_csv(path)

    for col in ["id","ID","patient_id","Patient_ID","record_id"]:
        if col in df.columns:
            df = df.drop(columns=[col])

    for col in df.select_dtypes(include="number"):
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].fillna(df[col].mode()[0])

    scaler = StandardScaler()
    numeric = df.select_dtypes(include="number").columns.drop("GFR", errors="ignore")
    df[numeric] = scaler.fit_transform(df[numeric])

    return df
