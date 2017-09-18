def standaardtarief(afstandKM): #standaardbedrag voor een rit
    if afstandKM < 0:
        afstandKM = 0
        tarief = afstandKM * 0.80
        return(tarief)
    elif afstandKM >= 50:
        tarief = 15 + (afstandKM * 0.60)
        return tarief
    else:
        tarief = afstandKM * 0.80
        return tarief

def ritprijs(leeftijd, weekendrit, afstandKM): #return waarde is definitieve prijs
    tarief = standaardtarief(afstandKM)

    if leeftijd <= 11 or leeftijd >= 65 and weekendrit is 1:
        tarief = tarief * 0.65
        print('65+ Weekendtarief:')
        print(tarief)
    elif leeftijd <= 11 or leeftijd >= 65 and weekendrit is 0:
        tarief = tarief * 0.70
        print('65+ Kortingstarief')
        print(tarief)
    elif weekendrit == 1:
        tarief = tarief * 0.60
        print('Weekendtarief:')
        print(tarief)
    else:
        print('Normaaltarief:')
        print(tarief)

ritprijs(64,0,-10)
