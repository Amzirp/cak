Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = float(input("Введите длину 1 стороны: "))
... b = float(input("Введите длину 2 стороны: "))
... c = float(input("Введите длину 3 стороны: "))
... 
... if a + b > c and a + c > b and b + c > a:
...     print("Треугольник существует")
... else:
