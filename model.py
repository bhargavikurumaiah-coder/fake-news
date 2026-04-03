import pandas as pd
from utils import clean_text, keyword_score

def load_data():
    return pd.read_csv("data.csv")

def predict(text):
    text = clean_text(text)

    fake_prob, real_prob = keyword_score(text)

    if fake_prob > real_prob:
        return "FAKE", fake_prob, real_prob
    else:
        return "REAL", fake_prob, real_prob