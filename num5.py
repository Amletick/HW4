word1 = input("Первое слово: ")
word2 = input("Второе слово: ")
if sorted(word1.lower()) == sorted(word2.lower()):
    print("Анаграмма")
else:
    print("Не анаграмма")
