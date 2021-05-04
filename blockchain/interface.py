#bcid = [id] -> les id de tous les blockchain créé par l'utilisateur/ Vide au début
#Voulez vous créer un blockchain -> on ajouter un élément dans bcid
#Ou voulez vous ajouter une données -> on afficher les id des blockchain
#Entrée une donnée
#print la donnée
import blockchain
import block
import function
import csv



def restoreBlockchain():
    chain = []
    [idffichier,fichier]= function.listdirectory()
    for f in fichier:
        with open("save/" + f, 'r') as file:
            data = csv.reader(file, delimiter = ";")
            chain.append(blockchain.Blockchain(list(data)))
    return chain


def use():
    listBlockchain = restoreBlockchain()
    print("Voulez vous créer un blockchain?y/n")
    response = input()
    if(response.lower() == "y"):
        print("Quelle donnée voulez vous ajouter?")
        data = input()
        listBlockchain.append(blockchain.Blockchain(block.Block(data)))
    elif(response.lower() == "n"):
        [idfichier,fichier] = function.listdirectory()
        print("Voici les Blockchain existant :")
        print(str(idfichier))
        print("Voulez vous ajouter une donnée dans un des Clockchain ?y/n")
        answer = input()
        if(answer.lower() == "y"):
            print("Dans quelle blockChain voulez vous ajoutez un block ?")
            choice = input()
            if(choice in str(idfichier)):
                i = 0
                while listBlockchain[i].getId() != int(choice):
                    i = i + 1
                bc = listBlockchain[i]
                print("Quelle donnée voulez vous ajouter ?")
                bc.addBlock(block.Block(str(input())))
            else:
                print("Ce fichier n'existe pas")
                use()
    else:
        print("Je n'ai pas compris votre réponse")
        use()
    for b in listBlockchain:
        print(str(b.getId()))
        b.showBlockchain()
        print("___________________")
    print("Voulez vous continuez ?y/n")
    answer = input()
    if(answer.lower() == "y"):
        use()