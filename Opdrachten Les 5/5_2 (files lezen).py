kaartnummers = open('kaartnummers.txt', 'r')

for regel in kaartnummers.readlines():
    regel = regel.rstrip() # Verwijdert /n aan het einde van de regel
    line = regel.split(',')
    print('{1} heeft kaartnummer: {0}'.format(line[0], line[1]))

kaartnummers.close()