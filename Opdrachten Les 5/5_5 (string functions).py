invoerZin = input("Type een zin: ")
woorden = invoerZin.split()
gemiddelde = sum(len(woord) for woord in woorden) / len(woorden)
print(gemiddelde)