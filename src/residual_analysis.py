
import numpy as np

def residual_diagnostics(y_true, predictions):

    for name, pred in predictions.items():
        residuals = y_true[:len(pred)] - pred
        print(name, "Residual mean:", np.mean(residuals))
