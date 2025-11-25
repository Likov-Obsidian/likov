from random import randint

secret = randint(1, 100)
guess = 0

print("Угадай число от 1 до 100!")

while guess != secret:
    guess = int(input("Твоя догадка: "))
    
    if guess > secret:
        print("Меньше")
    elif guess < secret:
        print("Больше")
    else:
        print("Угадал!")