Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> y = int(input("Введите год: "))
... 
... if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
...     print(y, "высокосный год")
...     d = 366
... else:
...     print(y, "не высокосный год")
...     d = 365
... 
