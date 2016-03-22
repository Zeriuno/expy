#Types, notes de M. Roussel

a = 2 #entier
c = "Chaîne" #chaîne de caractères
tab = [] #liste vide
tab2 = [33, 44, 55]
liste = [tab, tab2]

print(tab2)
print(liste)
print(tab2[1])
print(33 in tab2)
#tab2[8] = 87 #de moi: cela donne l'erreur Index out of range.
tab2[2] = 'a' #de moi: une liste peut contenir des types différents
#taille
print(len(tab2))
print(tab2) #de moi

tab2.append(1)
print(tab2)

tab3 = [1, 1, 1, 6, 5] #de moi
print(tab3.index(1))  #de moi #retourne le premier indice uniquement
print(tab3[0:2]) #de moi
liste4 = tab3[0:3] #de moi
print(liste4) #de moi

#table de hachage

ht1 = {}
ht1["âge"] = 12
ht1["ville"] = "Paris"
ht1["cheveux"] = "blond"
print(ht1["âge"])
print(ht1)

ht2 = dict(âge=3, ville="Bordeaux", cheveux="roux")
print(ht2)

print(sorted(ht1.keys()))
print(sorted(ht2.values()))