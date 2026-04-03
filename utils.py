import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def keyword_score(text):
    fake_words = ["alien", "miracle", "instant", "shocking", "unbelievable", "secret"]
    real_words = ["government", "official", "report", "confirmed", "data", "news"]

    fake_score = sum(1 for w in fake_words if w in text)
    real_score = sum(1 for w in real_words if w in text)

    total = fake_score + real_score + 1e-5

    return fake_score/total, real_score/total