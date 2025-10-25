from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, Course
from .crud import get_course, get_courses, create_course, update_course, delete_course

app = FastAPI(title=("Courses API: with FastAPI and MySQL"))

# Create tables in the database
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/courses/")
async def create_course_endpoint(name: str, description: str, author: str, db: Session = Depends(get_db)):
    return create_course(db, name, description, author)

@app.get("/courses/{course_id}")
async def get_course_endpoint(course_id: int, db: Session = Depends(get_db)):
    course = get_course(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detal="Course not found")
    return course

@app.put("/courses/{course_id}")
async def update_course_endpoint(course_id: int, name: str, description: str, author: str, db: Session = Depends(get_db)):
    course = update_course(db, course_id, name, description, author)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.delete("/courses/{course_id}")
async def delete_course_endpoint(course_id: int, db: Session = Depends(get_db)):
    response = delete_course(db, course_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return  response

@app.get("/courses/")
def list_courses_endpoint(db: Session = Depends(get_db)):
    courses = get_courses(db)
    if courses is None:
        raise HTTPException(status_code=204, detail="Courses dont exists")
    return courses