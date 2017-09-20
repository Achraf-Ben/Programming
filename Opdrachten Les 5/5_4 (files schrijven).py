import datetime

while True:
    hardlopers = open("hardlopers.txt", "a")
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    hardlopers.write(str(s) + ' '+ str(input('Type de naam van de hardloper: ') + '\n'))
    hardlopers.close()