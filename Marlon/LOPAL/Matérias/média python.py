Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = int(input("Digite sua idade aqui: ")
...         5
...            
SyntaxError: '(' was never closed
>>> num1 = int(input("Digite sua idade aqui: "))
...            
Digite sua idade aqui: 5
>>> num2 = int(input("Digite sua idade aqui: ")
...            2
...            
SyntaxError: '(' was never closed
>>> num2 = int(input("Digite sua idade aqui: "))
...            
Digite sua idade aqui: 3
>>> num3 = int(input("Digite sua idade aqui: "))
...            
Digite sua idade aqui: 9
>>> num4 = int(input("Digite sua idade aqui: "))
...            
Digite sua idade aqui: 7
>>> num5 = int(input("Digite sua idade aqui: "))
...            
Digite sua idade aqui: 6
>>> num6 =(( num1 + num2 + num3 + num4 + num5) /5)
...            
>>> print("A sua média é:", num6)
