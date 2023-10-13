from pydantic import BaseModel
from datetime import datetime


class QuizQuestionBase(BaseModel):
    text: str
    answer: str
    time_created: datetime

    class Config:
        orm_mode = True


class QuizQuestion(QuizQuestionBase):
    id: int


class QuestionAmount(BaseModel):
    question_num: int

    class Config:
        orm_mode = True
