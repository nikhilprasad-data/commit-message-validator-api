from fastapi import APIRouter, HTTPException, status
from src.api.schemas import CommentSchema, CommentSchemaResponse
from models import tfidf_vectorizer, tfidf_model_svc
from src.api.utils.text_utils import utils

comment = APIRouter()


@comment.post("/commit-message-validator", response_model=CommentSchemaResponse, status_code=status.HTTP_200_OK)
def check_comment(comment: CommentSchema):
     text = comment.commit_message

     clean_txt = utils(text)

     # 1. Vectorize the cleaned text
     vectorized_text = tfidf_vectorizer.transform([clean_txt])

     # 2. Make prediction
     prediction = tfidf_model_svc.predict(vectorized_text)

     if prediction[0] == 1:
          return {"commit_message": "The commit message is toxic."}  
     else:
          return {"commit_message": "The commit message is constructive."}