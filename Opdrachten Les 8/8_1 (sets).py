bruin = {'Deurne', 'Helmond Brouwhuis', 'Helmond', 'Helmond Hout', 'Breukenlaan', 'Best'}
groen = {'Weert', 'Heeze', 'Geldrop', 'Breukenlaan', 'Best'}

overeenkomsten = bruin.intersection(groen)
print(overeenkomsten)

verschil = bruin.difference(groen)
print(verschil)

totaal = bruin.union(groen)
print(totaal)