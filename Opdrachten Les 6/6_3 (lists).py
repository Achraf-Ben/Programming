invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoerList = [int(s) for s in invoer.split('-')]
print('Gesorteerde list van ints:' + str(invoerList))

invoerList.sort()
hoogsteGetal = invoerList[-1]
laagsteGetal = invoerList[0]

print('Grootste getal: {0} en Kleinste getal: {1}'.format(hoogsteGetal,laagsteGetal))

aantalGetallen = len(invoerList)
sumGetallen = sum(invoerList)
gemiddeldeCijfer = sumGetallen / aantalGetallen

print('Aantal getallen: {0} en som van de getallen: {1}'.format(aantalGetallen,sumGetallen))
print('Gemiddelde: {}'.format(gemiddeldeCijfer))