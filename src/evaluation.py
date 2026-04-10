
import numpy as np
from sklearn.metrics import r2_score

def evaluate_models(y_true, predictions):

    results = {}

    for name, pred in predictions.items():
        sse = np.sum((y_true[:len(pred)] - pred)**2)
        r2 = r2_score(y_true[:len(pred)], pred)
        results[name] = {"SSE": sse, "R2": r2}

    return results
