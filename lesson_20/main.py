import random
from HomeWork_21 import session, Student, Course

def add_student_to_course(student_name, course_id):
    new_student = Student(name=student_name)
    course = session.query(Course).get(course_id)
    if course:
        new_student.courses.append(course)
        session.add(new_student)
        session.commit()
        print(f"Student {student_name} added to course {course.title}")

from HomeWork_21 import session, Student, Course

course = session.query(Course).filter_by(title="Python Automation").first()
if not course:
    course = Course(title="Python Automation")
    session.add(course)
    session.commit()
    print("Course added!")

new_student = Student(name="Alex Test")
new_student.courses.append(course)

session.add(new_student)
session.commit()

print(f"Student {new_student.name} added with ID: {new_student.id}")

count = session.query(Student).count()
print(f"DB have students: {count}")

course_names = ['Python', 'Java', 'JavaScript', 'PHP', 'DevOps']
courses_in_db = []

for name in course_names:
    c = session.query(Course).filter_by(title=name).first()
    if not c:
        c = Course(title=name)
        session.add(c)
        session.commit()
    courses_in_db.append(c)

first_names = ['Oleh', 'Ivan', ' Petro', 'Makar','Kindrat', 'Ostap', 'Klavdiya', 'Marfa']
last_name = ["Kovalenko", "Simonenko", "Bamper","Zabor", "Levchenko", "Petrova", "Scevchenko", "Bidonenko"]

for i in range(20):
    full_name = f"{random.choice(first_names)} {random.choice(last_name)} {i+1}"
    student = Student(name=full_name)
    assigned = random.sample(courses_in_db, k=random.randint(1, 2))
    student.courses.extend(assigned)
    session.add(student)

session.commit()
print("First step done: 20 students added")

def get_students_by_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        print(f"\nStudent in course '{course_title}':")
        for s in course.students:
            print(f"- {s.name}")
        else:
            print(f"Cours '{course_title}' not found.")

def get_course_by_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()

    if student:
        print(f"\nCourse, in write {student_name}:")
        for c in student.courses:
            print(f" - {c.title}")
        else:
            print(f"Student '{student_name}' not found")

get_students_by_course('Python')
get_course_by_student('Alex Test')

def update_student_name(student_id, new_name):
    student = session.get(Student, student_id)
    if student:
        old_name = student.name
        student.name = new_name
        session.commit()
        print(f"Student ID: {student_id} updated: {old_name} to {new_name}")
    else:
        print(f"Student with ID: {student_id} not found")

def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {student.name} (ID: {student_id}) was deleted in DB")
    else:
        print(f"Unable to deleted: student with ID {student_id} not exist")

update_student_name(23, "Alex Makarov")
delete_student(1)

student_63 = session.get(Student, 63)
if student_63:
    print(f"Not found student: {student_63}")

update_student_name(63, "Final Student")

delete_student(44)