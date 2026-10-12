import random as rnd
import string

letters = rnd.choices(string.ascii_uppercase, k=3)
digits = rnd.choices(string.digits, k=3)
specials = rnd.choices("!@#$%^&*", k=2)

password = letters + digits + specials
rnd.shuffle(password)

print("Сгенерированный пароль:", "".join(password))
