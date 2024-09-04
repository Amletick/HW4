import string
table = str.maketrans(dict.fromkeys(string.punctuation + ' '))
stringinp = input("Введите строку: ").lower()
if stringinp.translate(table) == stringinp[::-1].translate(table):
    print("Палидром")
else:
    print("Не палидром")
