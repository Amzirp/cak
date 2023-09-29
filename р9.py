Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ch = int(input("Выберите фигуру: 1 - прямоугольник, 2 - треугольник, 3 - круг: "))
... 
... if ch == 1:
...     l = float(input("Введите длину прямоугольника: "))
...     w = float(input("Введите ширину прямоугольника: "))
...     a = l * w
...     print("Площадь прямоугольника:", a)
... elif ch == 2:
...     b = float(input("Введите длину основания треугольника: "))
...     h = float(input("Введите h треугольника: "))
...     a = 0.5 * b * h
...     print("Площадь треугольника:", a)
... elif ch == 3:
...     r = float(input("Введите радиус круга: "))
...     a = 3.14159 * r ** 2
...     print("Площадь круга:", a)
... else:
