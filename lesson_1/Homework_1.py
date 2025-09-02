# 1. Создание переменных и вывод значений
name = "Малика"
age = 25
height = 1.67
print(name)
print(age)
print(height)

# 2. Изменение значений переменных
x = 10
print(type(x))
x = 25.5
print(type(x))
x = "Python"
print(x)
print(type(x))

# 3. Копирование ссылок

a = 7
b= a
print(a)
print(b)
a = 10
print(b)

# 4. Каскадное присваивание
x, y ,z = 100, 100,100
print(x, y, z)

print(id(x), id(y), id(z))
# одинаковые

x, y ,z = 111, 123, 333
print(x, y, z)
print(id(x), id(y), id(z))
# Разные

# 5. Обмен значений переменных

a = 5
b = 10
a , b = 10, 50
print(a, b)

# 6. Работа с именами переменных
import keyword
print(keyword.kwlist)
# 7. Использование функции type()
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1), type(var2), type(var3))
var1 = "Hello"
print(type(var1))
# 8. Дополнительные задания
m = "меня"
ma = "зовут"
lika = "малика"
kali = 13
ma_li_ka = 2.5
print(m, ma, lika, kali, ma_li_ka)
print(type(m), type(ma), type(lika), type(kali), type(ma_li_ka))

я = 10
print(я)
# Попробуй объявить переменную с русским именем (переменная = 10). Работает ли это? да