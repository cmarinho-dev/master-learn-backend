from sqlalchemy.orm import Session
from .models import Course

def get_courses(db: Session):
    return db.query(Course).all()

def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

def create_course(db: Session, name: str, description: str, author: str):
    db_course = Course(name=name, description=description, author=author)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, name: str, description: str, author: str):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        return
    db_course.name = name
    db_course.description = description
    db_course.author = author
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        return
    db.delete(db_course)
    db.commit()
    return {"detail": "Course deleted"}