Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = int(input("Введите дальность выстрела "))
... if d > 28 and d < 30:
... 	print("Попал")
... if d >= 30:
... 	print("Перелёт")
... if d > 0 and d <= 28:
... 	print("Недолёт")
... if d <= 0:
