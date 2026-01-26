import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer2 = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer2)
print("/" * 40)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer3 = adwentures_of_tom_sawer2.replace("....", " ")
print(adwentures_of_tom_sawer3)
print("/" * 40)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer4 = adwentures_of_tom_sawer3.replace("  ", " ")
print(adwentures_of_tom_sawer4)
print("/" * 40)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(adwentures_of_tom_sawer4.count("h"))
print("/" * 40)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adwentures_of_tom_sawer5 = len(re.findall(r'[A-Z]', adwentures_of_tom_sawer4))
print(adwentures_of_tom_sawer5)
print("/" * 40)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
text_index = adwentures_of_tom_sawer.find('Tom', 2)
print(text_index)
print("|" * 40)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = re.split(r'[.!?]+' ,adwentures_of_tom_sawer4)
print(adwentures_of_tom_sawer_sentences)
print("|" * 40)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3])
print("|" * 40)
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print(any(map(str.startswith, map(str.strip, adwentures_of_tom_sawer_sentences), ["By the time"] * len(adwentures_of_tom_sawer_sentences))))
print("|" * 40)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

lengs_word = len(adwentures_of_tom_sawer_sentences[3].split())
print(lengs_word)
print("|" * 40)