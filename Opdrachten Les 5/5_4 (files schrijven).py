import datetime

hardlopers = open("hardlopers.txt", "a")

while True:
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    naam = str(input('Type de naam van de hardloper: '))
    hardlopers.write(str(s) + ' '+ naam + '\n')
    if naam == 'end':
        break
hardlopers.close()