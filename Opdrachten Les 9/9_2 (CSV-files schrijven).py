import datetime
import csv

with open('inloggers.csv', 'a', newline='') as inloggersCSV:
    writer = csv.writer(inloggersCSV, delimiter=';')  #csv.writer
    writer.writerow(('naam', 'voorl', 'gbdatum', 'email', 'time')) # Columnnames (one tuple!), optional!

    while True:
        naam = input("Wat is je achternaam? ")

        if naam == 'einde':
            break
        else:
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")
            vandaag = datetime.datetime.today()
            time = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
            writer.writerow((naam, voorl, gbdatum, email, time)) # Values, one tuple!!
