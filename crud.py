from sqlalchemy.orm import Session

import models


def commit_to_db(db: Session, db_model: models.Base) -> None:
    """Commiting to db function"""
    db.add(db_model)
    db.commit()
    db.refresh(db_model)


def create_quiz(
    db: Session,
    quiz_data: dict,
) -> models.QuizQuestion:
    """Creating question in db"""
    db_quiz_question = models.QuizQuestion(
        text=quiz_data['question'],
        answer=quiz_data['answer']
    )
    commit_to_db(db=db, db_model=db_quiz_question)
    return db_quiz_question


def get_question_by_text(text: str, db: Session):
    """Function that gets qestion from db by text"""
    return db.query(models.QuizQuestion).filter(
                models.QuizQuestion.text == text).first()


def get_last_question(db: Session):
    """Function that gets last question from db"""
    return db.query(models.QuizQuestion).order_by(
            models.QuizQuestion.time_created.desc()).first()
