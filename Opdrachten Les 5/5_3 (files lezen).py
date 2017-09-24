def numLines(filename):
    'telt het aantal regels in een bestand'

    infile = open(filename, 'r')
    lineList = infile.readlines()
    infile.close()

    return len(lineList)

maxNummer = 0
lineCount = 1

kaartnummers = open("kaartnummers.txt", 'a')

with open('kaartnummers.txt', 'r') as kaartnummers:
    for line in kaartnummers:
        nummers = int(line.split(',')[0])
        if nummers > maxNummer:
             maxNummer = nummers
             lineNummer = lineCount
        lineCount += 1

numLines = numLines('kaartnummers.txt')

print('Deze file telt '+ str(numLines) +' regels')
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(maxNummer, lineNummer))