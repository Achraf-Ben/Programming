import csv

with open('stations.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')

    for row in reader:
        print("Treinstation: {}, Type: {}".format(row['name'], row['type']))

# Row is a dict
# First line is not printed.
