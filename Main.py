import matplotlib.pyplot as plt
import numpy as np

class Gare:
    gare = ""
    codeUIC = ""
    def __init__(self,gare,codeUIC):
        self.gare = gare
        self.codeUIC = codeUIC

    def __str__(self):
        return "Gare : "+self.gare+" Code UIC : "+self.codeUIC

    def __eq__(self, other):
        return self.gare == other.gare and self.codeUIC == other.codeUIC

    def __hash__(self):
        return hash((self.gare, self.codeUIC))

class Object:
    date=""
    objet=""
    gare= None
    classe=""
    enregistrement=""

    def __init__(self,date,gare,objet,classe,enregistrement):
        self.date=date
        self.gare=gare
        self.objet=objet
        self.classe=classe
        self.enregistrement=enregistrement


    def __str__(self):
        return "Date : "+self.date+" Gare : "+self.gare + " Objet : "+self.objet+" Classe : "+self.classe+" Enregistrement : "+self.enregistrement

listeObjet=[]
gareSet = set()
missing = 0

with open('objets-trouves-gares.csv', 'r') as file:
    # Skip the first line
    next(file)
    for line in file:
        line = line.split(";")
        # Create a Gare object
        gare = Gare(line[1],line[2])
        # Add the Gare object to the set if it doesn't already exist
        if gare not in gareSet:
            gareSet.add(gare)

        #now get the pointer to the one in the set
        for g in gareSet:
            if g == gare:
                gare = g

        objet = Object(line[0],gare,line[3],line[4],line[5])
        if objet.date == "" or objet.gare.gare == "" or objet.gare.codeUIC == "" or objet.objet == "" or objet.classe == "" or objet.enregistrement == "":
            missing += 1
        listeObjet.append(objet)

print("Nombre d'objets manquants : ", missing)
print("Nombre d'objets trouvés : ", len(listeObjet))
print("pourcentage d'objets maquant : ", (missing/len(listeObjet)) * 100, "%")

#pretraitement des données
datas =[]
test = [] ## all data with empty gare
for objet in listeObjet:
    if objet.gare.gare == "":
        test.append(objet)
    else:
        datas.append(objet)


# tracages de données utiles

## affichage de nb d'objets par gare, chaque gare auras le nombre d'objets trouvés par catégorie (classe)
## xlabels : les gares
## ylabels : le nombre d'objets trouvés (par classe) par gare

gareObjet = {}
for objet in datas:
    if objet.gare.gare not in gareObjet:
        gareObjet[objet.gare.gare] = {}
    if objet.classe not in gareObjet[objet.gare.gare]:
        gareObjet[objet.gare.gare][objet.classe] = 1
    else:
        gareObjet[objet.gare.gare][objet.classe] += 1

x = []
y = []
for key in gareObjet.keys():
    x.append(key)
    #trier les classes
    classes = []
    for objet in gareObjet[key].keys():
        classes.append(objet)
    classes.sort()

    y.append([gareObjet[key][classe] for classe in classes])


plt.figure("Nombre d'objets par gare")
plt.bar(x,y)
plt.show()