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

    if leeftijd <= 11 or leeftijd >= 65 and weekendrit is 1:  # weekend + -12 en 65+ korting
        tarief = tarief * 0.65   #tarief * 0.70 = 35% korting
        print('65+ Weekendtarief:')
        print(tarief) # print kortingstarief 65+
    elif leeftijd <= 11 or leeftijd >= 65 and weekendrit is 0:  # -12 en 65+ korting
        tarief = tarief * 0.70   #tarief * 0.70 = 30% korting
        print('65+ Kortingstarief')
        print(tarief) # print kortingstarief 65+
    elif weekendrit == 1:
        tarief = tarief * 0.60  # tarief * 0.60 = 40% korting
        print('Weekendtarief:')
        print(tarief)  # print kortingstarief 65+
    else:
        print('Normaaltarief:')
        print(tarief) # print standaardtarief

ritprijs(64,0,-10)
