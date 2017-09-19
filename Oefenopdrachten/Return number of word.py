def numWords(filename):
    'returns the number of words in file filename'

    infile = open(filename)
    content = infile.read()
    infile.close()
    wordList = content.split()

    return len(wordList)
