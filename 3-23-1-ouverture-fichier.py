# Code de M. Roussel

#f = open("texte.txt", "r", encoding="utf-8")
#f = open("texte.txt", "w", encoding="utf-8")
#f = open("texte.txt", "a", encoding="utf-8")

#Lecture
f = open("texte.txt")
for ligne in f:
    print(ligne)

f.close()

f = open("texte.txt", "r")
print(f.readline()) #lit toute la ligne ou bien n caractères de la ligne actuelle, et passe le curseur à la ligne suivante
f.close()

#Ecriture
f = open("texte.txt", "w", encoding="utf-8")
f.write("YOLO!")
f.close()

#test
f = open("texte.txt", "r", encoding="utf-8")
for ligne in f:
    print(ligne)
f.close()

# invite à la saisie
reponse = input("Quel jours sommes-nous?")
print(reponse)