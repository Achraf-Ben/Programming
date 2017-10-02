def inlezen_beginstation(stations):
   invoer = input('Voer het beginstation in: ')
   while True:
        if invoer in stations:
            return invoer
        else:
            invoer = input('Voer het beginstation in: ')

def inlezen_eindstation(stations, beginstation):
    invoer = input('Voer het eindstation in: ')
    while True:
        if invoer in stations:
            if stations.index(invoer) >= stations.index(beginstation):
                return invoer
        else:
            invoer = input('Voer het eindstation in: ')

def omroepen_reis(stations, beginstation, eindstation):
    beginStation = stations.index(beginstation)+ 1
    eindStation = stations.index(eindstation) + 1
    afstand = eindStation - beginStation
    prijs = 5 * afstand
    print('Het beginstaton {0} is het {1}e station in het traject'.format(beginstation,beginStation))
    print('Het eindstation {0} is het {1}e station in het traject'.format(eindstation,eindStation))
    print('De afstand bedraagt {0} stations'.format(afstand))
    print('De prijs van het kaartje is {0} euro'.format(prijs))
    return


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam  Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)

omroepen_reis(stations, beginstation, eindstation)
