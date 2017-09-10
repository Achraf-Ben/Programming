cijferPunt = 30
cijferICOR = 7
cijferPROG = 7
cijferCSN = 8

gemiddelde = ((cijferICOR + cijferPROG + cijferCSN) / 3)
beloning = gemiddelde * cijferPunt

overzicht = "Mijn cijfers (gemiddeld een " + str(gemiddelde) + ") leveren een beloning van € " + str(beloning) + " op!"
print(overzicht)