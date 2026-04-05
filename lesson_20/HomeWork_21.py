from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_courses, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary=student_courses, back_populates="courses")

engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print("DB and tables done!")