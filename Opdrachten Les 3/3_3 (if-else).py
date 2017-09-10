score = input('Geef je leeftijd : ')
print(score)
passport = input('Nederlands paspoort: ')

if int(score) >= 18 and passport == "ja" or passport == "Ja":
    print('Gefeliciteerd je mag stemmen!')
else:
    print("Helaas je mag niet stemmen")
