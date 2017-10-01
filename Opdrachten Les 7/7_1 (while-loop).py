lijst = []

while True:
    nummer = input("Geef een getal: ")
    if nummer == 0:
        break
    else:
        lijst.append(nummer)

if len(lijst) == 1:
    print('Er is {0} getal ingevoerd, de som is: {1}'.format(len(lijst),sum(lijst)))
else:
    print('Er zijn {0} getallen ingevoerd, de som is: {1}'.format(len(lijst), sum(lijst)))