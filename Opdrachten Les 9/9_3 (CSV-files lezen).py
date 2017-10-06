import csv

with open('scores.csv', 'r') as scores:

    reader = csv.reader(scores, delimiter=';')
    maxt = 0

    for row in reader: # Row is a list
        if int(row[2]) > int(maxt):
            naam = row[0]
            datum = row[1]
            maxt = int(row[2])

    print('De hoogste score is: {2} op {1} behaald door {0}'.format(naam,datum,maxt))
