from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from database import Base


class QuizQuestion(Base):
    __tablename__ = 'quiz_questions'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    answer = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
