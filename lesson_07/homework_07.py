# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(f"{number}" + "x" + f"{multiplier}"+ "=" f"{result}")
        # Increment the appropriate variable
        multiplier += 1
    return None

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

print("/"* 60)
# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(num1, num2):
    result = num1 + num2
    print(result)
sum_numbers(12, 5)
print("/"* 60)
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    if not numbers:
        return None
    result = sum(numbers) / len(numbers)
    return result

calculate_average([2, 3, 7, 6, 9, 3])
print(calculate_average([2, 3, 7, 6, 9, 3]))
print("/"* 60)
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers_text(my_text: str):
    my_text = my_text.split(" ")
    my_text = list(my_text)
    print(my_text[-1::-1])
revers_text("Написати функцію, яка приймає рядок та повертає його у зворотному порядку")
print("/"* 60)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def leng_word(my_text):
    #my_text = "Написати функцію, яка приймає список слів та повертає найдовше слово у списку"
    my_text = my_text.split(" ")
    lengest_word = max(my_text, key=len)
    result = []
    for i in my_text:
        if len(i) == len(lengest_word):
            result.append(i)
    return result
leng_word("Написати функцію, яка приймає список слів та повертає найдовше слово у списку")
print(leng_word("Написати функцію, яка приймає список слів та повертає найдовше слово у списку"))
print("/"* 60)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    i = 0
    len_sub = len(str2)
    while i + len_sub <= len(str1):
        if str1[i:i + len_sub] == str2:
            return i
        i += 1

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""  Написати функцію, яка рахує кількість унікальних символів.
"""
def your_symbol(some_word):
    count = set()
    for char in some_word:
        if char not in count:
            count.add(char)

    if len(count) > 10:
        print("True")
    else:
        print("False")

your_symbol("huligan")
print("/"* 60)

# task 8
"""  Перевірка наявності літери 'h/H' у слові.
"""
def func_08(your_word):
    while True:
        your_word = input("Enter your word with ""h/H"":")
        if "h" in your_word.lower():
            print(f"Good: {your_word}")
            break
        else:
            print("Wrong word, try again")
func_08("huligan")
print("/"* 60)

# task 9
"""  Знайти сумму парниї чисел.
"""
def sum_list(list1):
    list2 = []

    for i in list1:
        if i % 2 == 0:
            list2.append(i)
    print(list2)
    return sum(list2)
sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 17 ,18, 19, 20])
print("/"* 60)

# task 10
"""  Повертає зі списку тільки едементи - стрінг.
"""
def only_string(list1):
    list2 = []

    for el in list1:
        if type(el) == str:
            list2.append(el)
    return list2
only_string(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
print("/"* 60)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""