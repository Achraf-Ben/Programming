def numLines(filename):
    'telt het aantal regels in een bestand'

    infile = open(filename, 'r')
    lineList = infile.readlines()
    infile.close()

    return len(lineList)

maxNumber = 0
lineCount = 0

with open('kaartnummers.txt', 'r') as kaartnummers:
    for line in kaartnummers:
        nummers = int(line.split(',')[0])
        if nummers > maxNumber:
             maxNumber = nummers
             lineNumber = lineCount
        lineCount += 1

numLines = numLines('kaartnummers.txt')

print('Deze file telt '+ str(numLines) +' regels')
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(maxNumber,lineNumber))