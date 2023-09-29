Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... x = float(input("Введите координату x: "))
... y = float(input("Введите координату y: "))
... r = float(input("Введите r круга: "))
... 
... d = math.sqrt(x ** 2 + y ** 2)
... 
... if d <= r:
...     print("Точка принадлежит кругу")
... else:
