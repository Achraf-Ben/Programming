def ticker(bestand):
    'Functie om dictonary uit te lezen'
    dictonary = {}
    with open(bestand, 'r') as bestand:
        lines = bestand.readlines()
        for line in lines:
            line = line.rstrip()
            line = line.split(':')
            dictonary[line[0]] = line[1]
            print(dictonary)
        return dict


companyName = input('Enter Company name: ')

for key, val in ticker('ticker.txt'):
    if key == companyName:
        print('Ticker symbol: {}'.format(val))

tickerSymbol = input('Enter Ticker symbool: ')

for key, val in ticker('ticker.txt'):
    if val == tickerSymbol:
        print('Ticker symbol: {}'.format(key))