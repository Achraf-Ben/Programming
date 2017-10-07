import random
def monopolyworp():
    'Functie die een Monopoly worp simuleert'
    counter = 0
    while True:
        eerste = random.randrange(1, 7)
        tweede = random.randrange(1, 7)
        totaal = eerste+tweede
        if eerste == tweede:
            print(eerste, '+', tweede, '=', totaal, ' (dubbel)')
            counter += 1
            neerste = random.randrange(1, 7)
            ntweede = random.randrange(1, 7)
            ntotaal = neerste+ntweede
            if neerste == ntweede:
                print(neerste, '+', ntweede, '=', ntotaal, ' (dubbel)')
                counter += 1
                deerste = random.randrange(1, 7)
                dtweede = random.randrange(1, 7)
                dtotaal = deerste+dtweede
                if deerste == dtweede:
                    print(deerste, '+', dtweede, '=', ' (Direct naar de gevangenis)')
                    break
                else:
                    print(deerste, '+', dtweede, '=', dtotaal)
                    break
            else:
                print(neerste, '+', ntweede, '=', ntotaal)
                break
        else:
            print(eerste, '+', tweede, '=', totaal)
            break


monopolyworp()
