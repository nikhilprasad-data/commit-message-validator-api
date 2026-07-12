import os
import joblib

models_dir = os.path.dirname(__file__)

tfidf_vectorizer = joblib.load(os.path.join(models_dir, "tfidf_vectorizer.pkl"))
tfidf_model_svc = joblib.load(os.path.join(models_dir, "toxic_model_svc.pkl"))