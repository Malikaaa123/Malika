
# 1. Работа с целыми и вещественными числами
# ================================================
a = 7
b = 89
x = 8.5
y = 9.3
print(a, b, x, y)
print(type(a), type(b), type(x), type(y))
# 2. Основные арифметические операции
num1 = 10
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)
# 3. Особенности работы с делением
a = 10
b = 3
print(a / b)
print(a // b)
print(a % b)

a = -10
b = 3
print(a / b)
print(a // b)
print(a % b)

a = 10
b = -3
print(a / b)
print(a // b)
print(a % b)
# 4. Работа с приоритетом операторов
a = 5 + 3 * 2
b = (5 + 3) * 2
c = 10 / 2 ** 2
print(a)
print(b)
print(c)
# 5. Использование сокращенных операторов
count = 10
count += 5
count -= 3
count *= 2
count /= 4
print(count)
# 1. Создание строк
s1 = "Python"
s2 = 'Программирование'
print(s1, s2)
s3 = """Это первая строка
Это вторая строка
А это третья строка"""
print(s3)
empty = ""
print(len(empty))
# 2. Конкатенация строк
first_name = "Иван"
last_name = "Петров"
full_name = first_name + " " + last_name
print(full_name)
# 3. Преобразование типов
s = "Возраст: "
age = 25
print(s + (str(age)))
# 4. Дублирование строк
print("ха " * 5)
# 5. Длина строки
text = "Привет, мир!"
print(len(text))
t2 = ""
print(len(t2))
sentence = "Я изучаю Python"
print("Python" in sentence)
print("Java" in sentence)
# 7. Сравнение строк
a = "apple"
b = "banana"
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
# 8. Код символов
print(ord('A'))
print(ord('a'))
print(ord('Я'))
