
def listePrenom(t):
    """
    :param t: string used as the file name
    :return: nothing
    """
    prenom = "o"
    prenom = input("Saisir un prénom (\"exit\" pour quitter) : ")
    f = open(t, "w", encoding="utf-8")
    while(prenom != "exit"):
        f.write(prenom + "\n")
        prenom = input("Saisir un prénom (\"exit\" pour quitter) : ")
    f.close()

def lisFichier(t = texte.txt): #on a ainsi précisé un paramètre par défaut
    """
    Function opens file :param t:, read and print it to the end, then closes it.
    :return: no return
    """
    f = open(t)
    print(f.read())
    f.close()

listePrenom("3-23-3-prenoms.txt")
lisFichier("3-23-3-prenoms.txt")