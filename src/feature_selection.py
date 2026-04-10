
from sklearn.linear_model import LassoCV

def run_feature_selection(df):
    X = df.drop("GFR", axis=1)
    y = df["GFR"]

    lasso = LassoCV(cv=5)
    lasso.fit(X, y)

    selected = X.columns[(lasso.coef_ != 0)]
    X_selected = X[selected]

    return X_selected, y
