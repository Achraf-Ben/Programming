def numLines(filename):
    'returns the number of lines in file filename'

    infile = open(filename, 'r’)
    lineList = infile.readlines()
    infile.close()

    return len(lineList)
