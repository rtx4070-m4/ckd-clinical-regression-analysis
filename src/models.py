
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV
from sklearn.model_selection import train_test_split

def train_models(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {}
    predictions = {}

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    predictions["Linear"] = lr.predict(X_test)

    lasso = LassoCV(cv=5)
    lasso.fit(X_train, y_train)
    predictions["LASSO"] = lasso.predict(X_test)

    ridge = RidgeCV(alphas=[0.1,1,10])
    ridge.fit(X_train, y_train)
    predictions["Ridge"] = ridge.predict(X_test)

    return models, predictions
