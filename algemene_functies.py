def mijn_functie_1(a):
    resultaten = []
    for getal in a:
        resultaat = getal * getal
        resultaten.append(resultaat)
    return resultaten
print(mijn_functie_1([2, 4, 10, 12]))

def mijn_functie_2(a,b):
    uitvoer_lijst=[]
    for i in range(len(a)):
        uitvoer_lijst.append(a[i]+b[i])
        uitvoer_lijst.append(a[i]-b[i])
        uitvoer_lijst.append(a[i]*b[i])
        uitvoer_lijst.append(a[i]/b[i])
    return uitvoer_lijst

print(mijn_functie_2([12, 12, 15, 100], [3, 2, 5, 20]))