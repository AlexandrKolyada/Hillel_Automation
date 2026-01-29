people_records = [
        ('John', 'Doe', 28, 'Engineer', 'New York'),
        ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
        ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
        ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
        ('Michael', 'Brown', 22, 'Student', 'Seattle'),
        ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
        ('David', 'Miller', 33, 'Software Developer', 'Austin'),
        ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
        ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
        ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
        ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
        ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
        ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
        ('Ava', 'White', 42, 'Journalist', 'San Diego'),
        ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
    ]


people_records.insert(0, (('Oleksandr', 'Kolyada', 38, 'QA', 'Hof')))
print(people_records)
people_records[1], people_records[5] = people_records[5], people_records[1]
print(people_records)

print("|"*70)
old_people = all(int(people_records[i][2]) >= 30 for i in [6, 10, 13])
print("All people are 30 years old? - ", old_people)