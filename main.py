
from src.data_cleaning import load_and_clean
from src.mad_outlier import mad_outlier_removal
from src.feature_selection import run_feature_selection
from src.models import train_models
from src.evaluation import evaluate_models
from src.residual_analysis import residual_diagnostics

def main():
    df = load_and_clean("data/ckd_dataset.csv")
    df = mad_outlier_removal(df)
    X, y = run_feature_selection(df)
    models, predictions = train_models(X, y)
    results = evaluate_models(y, predictions)
    residual_diagnostics(y, predictions)
    print(results)

if __name__ == "__main__":
    main()
