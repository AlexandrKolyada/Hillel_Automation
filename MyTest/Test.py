#my_dict = {'name': 'Василь', 'age': 25, 'city': 'Київ'}
from lesson_2.main import result1

#for key in my_dict:
   # print(key)
#print("|"*50)
#for value in my_dict.values():
   # print(value)
#print("|"*50)
#for key, value in my_dict.items():
   # print(key, value)
age = 8

for i in range(age):
    for j in range(age):
        print(f'{i}{j}', end= ' ')
    print()

def own_sum(first_number, second_number):
        result = first_number + second_number
        return result

result1 = own_sum(1, 5)
print(result1)