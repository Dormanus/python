import random

number = random.randint(1, 10)
print("Votre nombre:\n")
player = input()
score = 1000

while int(player) != number:
    if int(player) < number:
        print("Le nombre à trouver est plus grand")
        score -= 5

    elif int(player) > number:
        print("Le nombre à trouver est plus petit")
        score -= 5

    print("Votre nombre:\n")
    player = input()

print("score " + str(score))
