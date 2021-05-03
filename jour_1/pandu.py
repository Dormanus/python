import random
import re

number = random.randint(0, 4)

words = ["bonjour", "terre", "python", "lune", "palourd"]
vie = 6
word = ""
print(words[number])
for i in words[number]:
    if i == words[number][0]:
        word = i
    elif i == words[number][len(words[number])-1]:
        word += i
    else:
        word += "_"
    
print(word)
i = 0

while vie > 0:
    print("Donner une lettre:\n")
    lettre = input()

    if re.search("^[a-zA-Z]$", lettre):
        if lettre in words[number] and lettre != word[0] and lettre != word[len(word)-1]:
            
            while True:
                i = words[number].find(lettre, i + 1)

                temp = list(word)
                temp[i] = lettre
                word = "".join(temp)
                
                if i == -1:
                    print(word)
                    break

        else:
            vie -= 1
        
        if word.find("_") == -1:
            break
    
    else:
        print("invalide\n")

if vie == 0:
    print("Perdu! Le mot était " + words[number])

else:
    print("Victoir!")