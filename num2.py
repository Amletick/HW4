num=[int(i) for i in input("Введите числа через пробел:").split(" ")]
max=num[0]
for i in num:
    if int(i)>max:
        max=num

print(max)