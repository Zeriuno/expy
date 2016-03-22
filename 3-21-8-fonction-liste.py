def listeM5(liste):
    if(len(liste) > 5):
        return True
    else:
        return False

yo = [1, 5]
lo = [5, 9, 6, 7, 2, 111]

print(listeM5(yo))
print(listeM5(lo))
#print(listeM5(5)) on ne déclare pas le type passé, mais si on passe quelque chose qui ne supporte pas la fonction len, on a un crash.

def nPairs(n):
    if (n > 0):
        pairs = []
        i = 0
        pairs.append(2)
        while(len(pairs) < n):
            pairs.append(pairs[i]+2)
            i+=1
        return pairs
    else:
        print("L'argument de la fonction doit être positif")

print(nPairs(8))

def nPairs2(n):
    pairs = []
    if (n > 0):
        i = 2
        while(len(pairs) < n):
            pairs.append(i)
            i+=2
    return pairs

print (nPairs2(2))

def nPairsRec(n):
    while ( len(pairs) < n):
        i += 2
        pairs.append(i)
    return pairs

def nPairsRange(n):
    pairs = range(2, n, 2)
    return pairs

print(nPairsRange(5))