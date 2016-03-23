
def listePrenom(t):
    prenom = "o"
    prenom = input("Saisir un prénom (\"exit\" pour quitter) : ")
    f = open(t, "w", encoding="utf-8")
    while(prenom != "exit"):
        f.write(prenom + "\n")
        prenom = input("Saisir un prénom (\"exit\" pour quitter) : ")
    f.close()

def lisFichier(t):
    f = open(t)
    print(f.read())
    f.close()

listePrenom("3-23-3-prenoms.txt")
lisFichier("3-23-3-prenoms.txt")