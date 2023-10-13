from fastapi import APIRouter, FastAPI, Depends
import httpx
from sqlalchemy.orm import Session

from crud import create_quiz, get_last_question, get_question_by_text
from database import SessionLocal, engine
import models
import schemas

app = FastAPI(title="QuizAPI")
quiz_callback_router = APIRouter()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/questions/', response_model=schemas.QuizQuestionBase)
def create_question(
    questions: schemas.QuestionAmount,
    db: Session = Depends(get_db),
):
    """
    Endpoint requests from the jservice API quiz questions
    saving them to db and returns last question from db
    """
    while True:
        response = httpx.get(
            f"https://jservice.io/api/random?count={questions.question_num}"
        )
        data = response.json()
        for quiz_data in data:
            response_quiz_text = quiz_data['question']
            if not get_question_by_text(db=db, text=response_quiz_text):
                create_quiz(db=db, quiz_data=quiz_data)
        return get_last_question(db=db)
