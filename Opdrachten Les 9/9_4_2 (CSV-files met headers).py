import csv

with open('artikelen.csv', 'r') as artikelen:
    artikelen = csv.reader(artikelen, delimiter=';')
    duursteArtikel = 0

    for row in artikelen: # Row is a list
            print(row)
            artikelNummer = row[0]
            artikelCode = row[1]
            naam = row[2]
            voorraad = row[3]
            try:
                prijs = eval(row[4])
                print(type(prijs))
                if prijs >= duursteArtikel:
                    duursteArtikel = prijs
                    print('Het duurste artikel is: {0} en die kost {1} Euro \n '
                      'Er zijn slechts {2} exemplaren in voorraad van het product met nummer {3}'.format(row[2],row[4],row[3],row[0]))

            except ValueError:
                continue
