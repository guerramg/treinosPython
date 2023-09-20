import random

numeros = [1, 50, 35, 80, 100]

print(random.choice(numeros))

randRange = random.randint(1,100)
print (randRange)

print(random.sample(numeros, 3))