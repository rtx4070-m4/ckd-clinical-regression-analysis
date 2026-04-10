
import numpy as np

def mad_outlier_removal(df):
    predictors = [c for c in df.columns if c != "GFR"]

    mask = np.zeros(len(df), dtype=bool)

    for col in predictors:
        median = np.median(df[col])
        mad = np.median(abs(df[col] - median))
        lower = median - 3*mad
        upper = median + 3*mad
        mask |= (df[col] < lower) | (df[col] > upper)

    return df[~mask]
