import re
import csv
import matplotlib.pyplot as plt
previous_i = ""
liste = []
w=0
# Ouverture du fichier de sortie de capture de paquets
with open('Sae1.05.txt', 'r') as f: # Lecture de chaque ligne du fichier
    lines = f.readlines()
    
    
with open('Sae1.05.csv','w',newline='') as fichiercsv: #cree le fichier .csv
    writer=csv.writer(fichiercsv)
    writer.writerow(['Temps;Adresse IP d envoie;Vers;Adresse IP de destination;Flags;seq;ack;win;val;ecr;length']) #Les grands titres   
    
    for line in lines: #boucle pour faire tourner toute les analyses sur chaque ligne
    
        match2 = re.search(r'seq\s(\d+)', line) #recherche dans la ligne ce qu'il y a apres "seq"
        if match2:
            test2 = match2.group(1)
        else : 
            test2 = ""
            
        match3 = re.search(r'ack\s(\d+)', line) #recherche dans la ligne ce qu'il y a apres "ack"
        if match3:
            test3 = match3.group(1)
        else : 
            test3 = "" 
            
        match4 = re.search(r'win\s(\d+)', line) #recherche dans la ligne ce qu'il y a apres "win"
        if match4:
            test4 = match4.group(1)
        else : 
            test4 = ""
            
        match5 = re.search(r'val\s(\d+)', line) #recherche dans la ligne ce qu'il y a apres "val"
        if match5:
            test5 = match5.group(1)
        else : 
            test5 = ""
            
        match6 = re.search(r'ecr\s(\d+)', line) #recherche dans la ligne ce qu'il y a apres "ecr"
        if match6:
            test6 = match6.group(1)
        else : 
            test6 = ""
            
        match7 = re.search(r'length\s(\d+)', line) #recherche dans la ligne ce qu'il y a apres "length"
        if match7:
            test7 = match7.group(1)
        else : 
            test7 = ""
            
        if re.search('IP',line): #cherche le mot IP
            resultat = line
            resultat2 = resultat.split() #et recupere les premiers resultats qui nous interesse
            resultat3 = resultat2[2]+';'+resultat2[3]+';'+resultat2[4]
            liste.append(resultat3) 
            
            writer.writerow([resultat2[0]+';'+resultat2[2]+';'+resultat2[3]+';'+resultat2[4]+';'+resultat2[6][1]+';'+test2+';'+test3+';'+test4+';'+test5+';'+test6+';'+test7])
            
for i in liste :
    liste.count(i)
    
# Crée un dictionnaire et stock les chemins IP
paths = {}
for i in liste:
    if i not in paths:
        paths[i] = 1
    else:
        paths[i] += 1
paths = {k: v for k, v in paths.items() if v >= 200}
# Extrait les chemins IP et les comptes
ip_paths = list(paths.keys())
counts = list(paths.values())

#Creation graph1
plt.bar(ip_paths, counts)
plt.xlabel("IP path")
plt.ylabel("Count")
plt.savefig('mon_graphique200.png')
plt.show()    

paths2 = {}
for i in liste:
    if i not in paths2:
        paths2[i] = 1
    else:
        paths2[i] += 1
paths2 = {k: v for k, v in paths2.items() if v >= 800}
# Extrait les chemins IP et les comptes
ip_paths2 = list(paths2.keys())
counts2 = list(paths2.values())

# Cree graph 2
plt.bar(ip_paths2, counts2)
plt.xlabel("IP path")
plt.ylabel("Count")
plt.savefig('mon_graphique800.png')
plt.show()
with open("Paquet-fragmente.txt","w") as f1 :
    # Ouverture du fichier de sortie de capture de paquets
    with open("Sae1.05.txt", "r") as f2:
        # Lecture de chaque ligne du fichier
        for lines in f2:
            # Recherche de la chaine "Flags [" dans la ligne
            if "Flags [" in lines:
                # Utilisation de l'expression reguliere pour extraire les informations de fragmentation
                match = re.search(r"Flags \[(.*)\],", lines)
                flags = match.group(1)
                # Verifie si le paquet est fragmente
                if "F" in flags:
                    f1.write("Paquet Fragmente : \n"+lines)
with open("Compteur-chemin.txt","w") as f2 :            
    for i in liste :
        if i == previous_i :
            w == 0+1
        else :
            liste.count(i)
            f2.write(f"le chemin {i} apparait {liste.count(i)} fois\n")
        previous_i = i
    
