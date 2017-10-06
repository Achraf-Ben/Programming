import csv

with open('stations.csv', 'r') as myCSVFile:

    reader = csv.reader(myCSVFile, delimiter=';')

    for row in reader: # Row is a list
        print("Station: {}, Type: {}".format(row[0], row[2]))
