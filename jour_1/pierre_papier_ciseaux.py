import random

def choice():
    number = random.randint(1, 3)
    if number == 1:
        choie = "pierre"
    
    elif number == 2:
        choie = "papier"
    
    elif number == 3:
        choie = "ciseaux"
    
    return choie

def result(j1, j2):
    if j1 == "pierre" and j2 == "ciseaux":
        victoir = "j1"

    elif j1 == "ciseaux" and j2 == "papier":
        victoir = "j1"
    
    elif j1 == "papier" and j2 == "pierre":
        victoir = "j1"

    elif j1 == j2:
        victoir = "egalite"

    else:
        victoir = "j2"

    return victoir

i = 0
pointJ1 = 0
pointJ2 = 0

while i < 10:
    j1 = choice()
    j2 = choice()
    resultat = result(j1, j2)
    
    if resultat == "j1":
        pointJ1 += 1
    
    elif resultat == "j2":
        pointJ2 += 1

    print(resultat)
    i += 1

if pointJ1 != pointJ2:
    print("\nVictoir ")
    if pointJ1 > pointJ2:
        print("J1 avec " + str(pointJ1))
    
    else:
         print("J2 avec " + str(pointJ2))

else:
    print("Egalité avec " + str(pointJ1))

