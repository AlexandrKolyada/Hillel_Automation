alice_in_wonderland = "Would you tell me, please, which way I ought to go from here?\nThat depends a good deal on where you want to get to, said the Cat.\nI don't much care where —— said Alice.\nThen it doesn't matter which way you go, said the Cat.\n—— so long as I get somewhere, Alice added as an explanation.\nOh, you're sure to do that, —— said the Cat, if you only walk long enough."
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
print("/" * 40)
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea = 436_402
azov_sea = 37_800
area_sea = black_sea + azov_sea
print(f"area of the Azov and Black Seas = {area_sea} km2")
print("/" * 40)
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
three_syllables = 375_291
first_and_second_syllables = 250_449
second_and_third_syllables = 222_950
first_syllable = three_syllables - second_and_third_syllables
third_syllable = three_syllables - first_and_second_syllables
second_syllable = three_syllables - (first_syllable + third_syllable)
print(f"first syllable = {first_syllable} items\nsecond syllable = {second_syllable} items\nthird syllable = {third_syllable} items")
print("/" * 40)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
credit_month = 18
credit_per_month = 1179
computer = credit_per_month * credit_month
print(f"cost of the computer =  {computer} UAH")
print("/" * 40)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f"a) 8019 : 8 = {a}\nb) 9907 : 9 = {b}\nc) 2789 : 5 = {c}\nd) 7248 : 6 = {c}\ne) 7128 : 5 = {e}\nf) 19224 : 9 = {f}")
print("/" * 40)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 274 * 4
pizza_medium = 218 * 2
juice = 35 *4
pie = 350
water = 21 * 3
all_products = pizza_big + pizza_medium + juice + pie + water
print(f"all products cost {all_products} UAH")
print("/" * 40)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
one_page_photos = 8
page = all_photos /one_page_photos
print(f"Igor will need {int(page)} pages for photos")
print("/" * 40)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
family_trip = 1600
car_gas_tank = 48
fuel_per_100_km = 9
fuel_consumption_for_the_trip = family_trip * fuel_per_100_km / 100
visiting_gas_station = fuel_consumption_for_the_trip / car_gas_tank
print(f"Fuel consumption for the entire trip = {int(fuel_consumption_for_the_trip)} L\nGas station visits throughout the trip = {int(visiting_gas_station)} L")