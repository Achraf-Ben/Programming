def namen():
    'Vraagt om een naam en kijkt hoevaak deze voorkomt'
    lijst = []
    invoer = ''
    invoer = input("Voer een naam in: ")
    while invoer != '':
        invoer = input("Voer een naam in: ")
        if invoer != '':
            lijst.append(invoer)
    return lijst

def frequency(itemlist):
    counters = {}
    for item in itemlist:
        if item in counters:
            counters[item] += 1
        else:
            counters[item] = 1
    return counters

namenlijst = namen()
namendictonary = frequency(namenlijst)

print(namendictonary)

for key in namendictonary:
    if namendictonary[key] > 1:
        print('Er zijn {} studenten met de naam {}'.format(namendictonary[key],key))
    else:
        print('Er is {} student met de naam {}'.format(namendictonary[key],key))
