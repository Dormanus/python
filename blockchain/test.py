import glob 
import os.path 

def listdirectory(): 
    fichier=[] 
    l = glob.glob('C:/Users/nicol/Documents/python/*') 
    for i in l: 
        if os.path.isfile(i): 
            fichier.append(i)  
    return fichier

print(listdirectory())