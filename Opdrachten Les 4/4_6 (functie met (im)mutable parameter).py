lijst = ['a','b','c']

def wijzig(x):
    x.remove('a')
    x.remove('b')
    x.remove('c')
    x.append('d')
    x.append('e')
    x.append('f')


print(lijst)
wijzig(lijst)
print(lijst)

print("Waarom kun je in de functie niet de opdracht lijst = ['d','e','f']geven?")
print('Omdat de assignment statement alleen binnen de functie bestaat')
print("Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?")
print('Een string parameter werkt ook niet waarschijnlijk om dezelfde reden als hierboven genoemd.')
print("Welke rol speelt (im)mutabiliteit in deze vraag?")
print('....')