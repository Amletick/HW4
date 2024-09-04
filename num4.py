import random
import string
length=int(input("Длина пароля: "))
chars=string.ascii_letters+string.digits+string.punctuation
pswd=''.join(random.choice(chars) for i in range(length))
print(pswd)
