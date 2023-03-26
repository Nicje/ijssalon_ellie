from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = float(prijs) * (1 - float(korting))
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

print(aanbieding_1("aardbei", "4", "0.1"))


def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
    btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.21))


def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer
lijst = 220, 430, 125, 160, 205, 90, 345
resultaat = laag_en_hoog(lijst)
print(resultaat)


def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for element in mijn_lijst:
        totaal += element
    gemiddelde = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."

lijst = [220, 430, 125, 160, 205, 90, 345]
resultaat = gemiddelde(lijst)
print(resultaat)


def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer=[tijdelijk[0], tijdelijk[1]]
    return uitvoer

invoer_lijst = [10, 5, 3, 2, 1, 9]
print(meervoudig(invoer_lijst))