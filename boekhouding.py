import csv
from helper import *
from presentatie import *

inkomsten = {"Aardbeien-ijs-totaal": 1000, 
             "Vanille-ijs-totaal": 2000, 
             "Chocolade-ijs-totaal": 1500, 
             "Waterijsjes-totaal": 750}

def som(d):
    return sum(d.values())

totaal_inkomsten = som(inkomsten)

def presenteer(d, totaal):
    mijn_dictionary = {
        'Aardbeien_ijs_totaal' : 1000, 
        'Vanille_ijs_totaal' : 2000, 
        'Chocolade_ijs_totaal' : 1500,
        'Waterijsjes_totaal' : 750
    }
    totaal = sum(d.values())
    return mijn_dictionary, totaal

inkomsten = {"Aardbeien-ijs": 1000, 
             "Vanille-ijs": 2000, 
             "Chocolade-ijs": 1500, 
             "Waterijsjes": 750}
mijn_dictionary, totaal = presenteer(inkomsten, 0)

print(mijn_dictionary)
print(totaal)

with open('boekhouding.csv','w,newline=') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])