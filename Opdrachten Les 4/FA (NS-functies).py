def standaardtarief(afstandKM):
    'Standaardbedrag voor een rit'
    if afstandKM < 0:
        afstandKM = 0
        tarief = afstandKM * 0.80
    elif afstandKM >= 50:
        tarief = 15 + (afstandKM * 0.60)
    else:
        tarief = afstandKM * 0.80
    return tarief

def ritprijs(leeftijd, weekendrit, afstandKM):
    'Return waarde is definitieve prijs'
    tarief = standaardtarief(afstandKM)

    if leeftijd <= 11 or leeftijd >= 65:
        if weekendrit == 1:
            tarief = tarief * 0.65
            print('65+ Weekendtarief')
            print(tarief)
        else:
            tarief = tarief * 0.70
            print('65+ Kortingstarief:')
            print(tarief)
    elif weekendrit == 1:
        tarief = tarief * 0.60
        print('Weekendtarief:')
        print(tarief)
    else:
        print('Normaaltarief:')
        print(tarief)

# Test loop
leeftijden = [11,12,20,64,65]
weekenden = [0,1]
afstanden = [-10, 50, 100]

for leeftijd in leeftijden:
    for weekend in weekenden:
        for afstand in afstanden:
            ritprijs(leeftijd,weekend,afstand)