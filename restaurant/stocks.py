import csv
import unicodedata
import re

def readStock():
    stock = []
    with open("data/stocks.csv", 'r') as file:
            data = csv.reader(file, delimiter = ";")
            stock.append(list(data))
    return stock[0]

def addStock(product, quantity):
    productN= unicodedata.normalize('NFKD',str(product).upper()).encode('ASCII', 'ignore').decode("utf-8")
    if(re.search("^[A-Z]{1,}([A-Z]{0,}|[A-Z\-\ ]{1,}[A-Z]{1})$",str(productN)) and re.search("^[\d]{1,}$", str(quantity))):
        data = readStock()
        last_id = int(data[len(data)-1][0])
        for d in data:
            print("test")
            if(d[1] == productN):
                print("Ce produit est déjà dans le stock")
                return ''
        with open("data/stocks.csv", 'a') as file:
            file.write(str(last_id +1) + ";" + str(productN) + ";"+ str(quantity) + "\n")
    else:
        print("Le nom du produit n'est pas une chaine de caractères valide (il ne faut pas de caractères spéciaux ou de nombre) ou la quantité n'est pas un nombre !")

def changeStock(id_product, quantity):
    try:
        if(re.search("^[\d]{1,}$", str(quantity))):
            stock = readStock()
            stock[id_product-1] = [str(id_product), stock[id_product-1][1], str(quantity)]
            with open("data/stocks.csv", 'w') as file:
                for s in stock:
                    file.write(s[0] + ";" + s[1] + ";" + s[2] + "\n")
        else: 
            print("Ce n'est pas une quantité")
    except:
        print("L'ID du produit n'est pas reconnu")

def changeName(id_product, name):
    try:
        name = str(name).upper()
        if(re.search("^[A-Z]{1,}([A-Z]{0,}|[A-Z\-\ ]{1,}[A-Z]{1})$",str(name))):
            stock = readStock()
            for d in stock:
                if(d[1] == name):
                    print("Ce produit est déjà dans le stock")
                    return ''
            stock[id_product-1] = [str(id_product), str(name).upper(), stock[id_product-1][2]]
            with open("data/stocks.csv", 'w') as file:
                for s in stock:
                    file.write(s[0] + ";" + s[1] + ";" + s[2] + "\n")
        else:
            print("Ce n'est pas une chaine de caractères !")
    except:
        print("L'ID du produit n'est pas reconnu")

def deleteStock(id_product):
    try:
        stock = readStock()
        response = input("Etes vous sûr de vouloir supprimer le produit " + stock[int(id_product)-1][1] + " ? y/n \n")
        if(response.lower() == "y"):
            elem = stock[int(id_product)-1][1]
            del stock[int(id_product)-1]
            print(elem + " a été supprimé du stock")
            i = 1
            for s in stock:
                s[0] = str(i)
                i += 1
            with open("data/stocks.csv", 'w') as file:
                for s in stock:
                    file.write(s[0] + ";" + s[1] + ";" + s[2] + "\n")
        else:
            print("Aucun produit n'a été supprimé")
    except: print("Aucun produit n'a été supprimé")

def exportStock(nameFile):
    stock = readStock()
    try:
        with open("export/"+nameFile + ".txt", 'x') as file:
            for s in stock:
                file.write(s[0] + ", " + s[1] + ", " +s[2] + "\n")
        print("Le fichier a bien été créé")
    except:
        print("Le fichier n'a pas pu être créé")


