import stocks

def menuPrincipal():
    print("__________________________________________________________________________________________")
    print("____________________                 RESTAURANT LIPSUM                ____________________")
    print("____________________                 15 rue des Ecoles                ____________________")
    print("____________________                    08360 GIVET                   ____________________")
    print("__________________________________________________________________________________________ \n")
    print("MENU PRINCIPAL : \n")
    print("1. PRISE DE COMMANDE")
    print("2. GESTION DES STOCKS")
    print("3. GESTION DU MENU")
    print("4. HISTORIQUE DES COMMANDES")
    print("5. QUITTER \n")
    print("QUE VOULEZ VOUS FAIRE ? (1-5) :")
    answer = input()
    if(answer == "2"):
        headerStock()
    if(answer == "5"):
        print("Au revoir")


def headerStock():
    print("__________________________________________________________________________________________")
    print("____________________                 RESTAURANT LIPSUM                ____________________")
    print("____________________                GESTIONS DES STOCKS               ____________________")
    print("__________________________________________________________________________________________ \n")
    print("__________________________________________________________________________________________ \n")
    print("|     |    PRODUIT                                                         |   QUANTITE  |")
    print("__________________________________________________________________________________________ ")


def menuStock():
    try:
        stock= stocks.readStock()
        headerStock()
        for s in stock:
            maxName = 68
            maxId = 4
            maxQty = 12
            nbspaceId = (maxId - len(s[0]))/2
            spaceId = ""
            iId = 0
            while iId < nbspaceId:
                spaceId = spaceId + " "
                iId += 1
            nbspaceName = maxName - len(s[1])
            spaceName = ""
            iName = 0
            while iName < nbspaceName:
                spaceName = spaceName + " "
                iName += 1
            nbspaceQty = (maxQty - len(s[2]))/2
            spaceQty = ""
            iQty = 0
            while iQty < nbspaceQty:
                spaceQty = spaceQty + " "
                iQty += 1
            print("|" + spaceId + s[0]+ spaceId+"|" + s[1]+ spaceName + "|" +spaceQty + s[2] +spaceQty+" |")
        print("__________________________________________________________________________________________ \n")
        print("1. MISE A JOUR DE LA QUANTITE D'UN PRODUIT")
        print("2. MISE A JOUR DU NOM D'UN PRODUIT")
        print("3. AJOUT DE PRODUIT")
        print("4. EXPORTER LA LISTE DES PRODUITS")
        print("5. SUPPRIMER UN PRODUIT")
        print("6. RETOUR AU MENU PRINCIPAL \n")
        print("QUE VOULEZ VOUS FAIRE ? (1-5)")
        answer = input()  
        if(answer == "1"):
            print("Sur quelle id du produit voulez vous modifier la quantité ? ")
            id_product= input()
            print("Quelle est la nouvelle quantité ? ")
            quantity = input()
            stocks.changeStock(id_product, int(quantity))
        elif(answer == "2"):
            print("Sur quelle id du produit voulez vous modifier la nom ? ")
            id_product= input()
            print("Quelle est le nouveau nom ? ")
            name = input()
            stocks.changeName(id_product, name)
        elif(answer == "3"):
            print("Quelle produit voulez vous ajouter ? ")
            product = input() 
            print("Avec quelle quantité ? ")
            quantity = input()
            stocks.addStock(product, int(quantity))
        elif(answer == "4"):
            print("Veuillez renseigner le nom du fichier : ")
            nameFile = input()
            stocks.exportStock(nameFile)
        elif(answer == "5"):
            print("Quel est Id du produit que vous voulez supprimer ? ")
            id_product = input()
            stocks.deleteStock(id_product)
        elif(answer == "6"):
            menuPrincipal()
        else:
            print("Je n'ai pas compris votre réponse")
            menuStock()
        menuStock()
    except:
        print("Une erreur est survenue")
        

menuStock()