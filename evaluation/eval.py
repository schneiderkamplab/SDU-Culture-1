import pandas as pd
import re
from typing import Tuple

def normalize_text(s: str) -> str:
    """Lower text and remove punctuation, articles and extra whitespace."""
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)  # keep alphanumeric
    return s.strip()

def f1_score(prediction: str, ground_truth: str) -> float:
    """Compute token-level F1."""
    pred_tokens = normalize_text(prediction).split()
    gold_tokens = normalize_text(ground_truth).split()

    common = set(pred_tokens) & set(gold_tokens)
    num_same = sum(min(pred_tokens.count(w), gold_tokens.count(w)) for w in common)
    
    if len(pred_tokens) == 0 or len(gold_tokens) == 0:
        return float(pred_tokens == gold_tokens)
    if num_same == 0:
        return 0.0
    precision = num_same / len(pred_tokens)
    recall = num_same / len(gold_tokens)
    return 2 * precision * recall / (precision + recall)

def exact_match_score(prediction: str, ground_truth: str) -> float:
    """Check if normalized prediction exactly matches normalized ground truth."""
    return float(normalize_text(prediction) == normalize_text(ground_truth))

def qa_score_single(pred: str, gold: str) -> Tuple[float, float]:
    """Return (EM, F1) for a single QA pair."""
    return exact_match_score(pred, gold), f1_score(pred, gold)

def evaluate_dataset(path: str, pred_col: str = "Prediction") -> dict:
    """Evaluate a CSV or Parquet file with columns Question, Answer, Prediction."""
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    elif path.endswith(".parquet"):
        df = pd.read_parquet(path)
    else:
        raise ValueError("File must be .csv or .parquet")

    ems, f1s = [], []
    for _, row in df.iterrows():
        gold = str(row["Answer"])
        pred = str(row[pred_col])
        em, f1 = qa_score_single(pred, gold)
        ems.append(em)
        f1s.append(f1)

    return {
        "EM": sum(ems) / len(ems),
        "F1": sum(f1s) / len(f1s),
    }
