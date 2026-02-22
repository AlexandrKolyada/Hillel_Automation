class Student:
    def __init__(self, name, last_name, age, average_score):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score


    def update_average_score(self, new_score):
        if 0<= new_score <= 100:
            self.average_score = new_score
        else:
            print("Error - wrong score")
            return new_score

    def show_info(self):
        print(self.name, self.last_name, self.age, self.average_score)

new_student = Student(name='Oleh', last_name='Pit', age=21, average_score=87)
new_student.show_info()
print(new_student.average_score)
new_student.update_average_score(95)
print(new_student.average_score)
new_student.update_average_score(150)
print(new_student.average_score)
new_student.show_info()