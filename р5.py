Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bigger = int(input("Введите max число: "))
... smaller = int(input("Введите min число: "))
... 
... if bigger % smaller == 0:
...     print(bigger, "кратно", smaller)
... else:
...     print(bigger, "не кратно", smaller)
...     remainder = bigger % smaller
