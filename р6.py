Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = float(input(" x: "))
... y = float(input(" y: "))
... 
... if x > 0 and y > 0:
...     print("Точка находится в 1 четверти")
... elif x < 0 and y > 0:
...     print("Точка находится во 2 четверти")
... elif x < 0 and y < 0:
...     print("Точка находится в 3 четверти")
... elif x > 0 and y < 0:
...     print("Точка находится в 4 четверти")
... else:
