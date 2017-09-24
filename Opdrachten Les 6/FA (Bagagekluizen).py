def menu():
    'Prints the main menu'
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")


def toon_aantal_kluizen_vrij():
    'Counts number of rows in kluizen.txt'
    kluizen = open("kluizen.txt", 'r')
    aantalBezet = kluizen.readlines()
    aantalVrij = 12 - len(aantalBezet)
    kluizen.close()
    print("Er zijn nog {} kluizen vrij.".format(aantalVrij))

def nieuwe_kluis():
    'Removes used kluisnummer from list and lets the user choose a password for the first kluis in the remaining list'
    kluizen = open("kluizen.txt", 'r')
    listAvailable = [1,2,3,4,5,6,7,8,9,10,11,12]
    listUsed = [1,2,3,4,5,6,7,8,9,10,11,12]
    empty = 0

    for regel in kluizen:
        regel = regel.rstrip()  # Verwijdert /n aan het einde van de regel
        kluisregel = regel.split(';')
        kluisUsed = int(kluisregel[0])

        if kluisUsed in listAvailable:
            listAvailable.remove(kluisUsed)
    kluizen.close()

    if len(listAvailable) is not empty:
        kluizen = open("kluizen.txt", 'a')
        wachtwoord = input('Vul een wachtwoord voor uw kluis in: ')
        kluizen.write('\n'+str(listAvailable[0])+';'+wachtwoord)
        print('Uw heeft kluisnummer: {} en uw wachtwoord is: {}'.format(listAvailable[0],wachtwoord))
        kluizen.close()
    else:
        print("Er zijn helaas geen kluizen beschikbaar.")
    k = input("press close to exit")


def kluis_openen():
    'Asks user for kluisnummer and password to "unlock" the kluis'
    kluisnummer = input('Geef uw kluisnummer op: ')
    wachtwoord = input('Geef uw wachtwoord op: ')
    combinatie = kluisnummer + ';' + wachtwoord
    print('Uw combinatie:' + combinatie)
    kluizen = open("kluizen.txt", 'r')

    for regel in kluizen:
        regel = regel.rstrip()  # Verwijdert /n aan het einde van de regel
        kluisregel = regel.split(';')
        if combinatie[0] == regel[0]:
            print("Uw kluis is geopend.")
        else:
            print('De ingevoerde ccombinatie is onjuist')

    k = input("press close to exit")

def kluis_teruggeven():
    'Asks user for kluisnummer and password and then deletes it from kluizen.txt'
    kluisnummer = input('Geef uw kluisnummer op: ')
    wachtwoord = input('Geef uw wachtwoord op: ')
    combinatie = kluisnummer + ';' + wachtwoord

    kluizen = open("kluizen.txt", 'r')
    regels = kluizen.readlines()
    kluizen.close()

    kluizen = open("kluizen.txt", 'a')
    for regel in regels:
        if regel == combinatie:
            kluizen.write("Deleted")
            print('Uw kluis is succesvol teruggenomen.')
        else:
            print('De ingevoerde combinatie is onjuist')
    k = input("Press a key to exit")

menu()
invoer = input("Wat wilt u doen? [1-4]: ")
actie = int(invoer)

if actie==1:
    toon_aantal_kluizen_vrij()
elif actie==2:
    nieuwe_kluis()
elif actie==3:
    kluis_openen()
elif actie==4:
    kluis_teruggeven()
else:
    print("Sorry de invoer is niet correct, voer een cijfer in tussen 1 en 4.")
