import csv

with open('newfile.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')  #csv.writer
    writer.writerow(('number', 'name')) # Columnnames (one tuple!), optional!

    while True:
        name = input('Name? ')

        if name == '':
            break

        number = input('Number? ')

        writer.writerow((number, name)) # Values, one tuple!!

