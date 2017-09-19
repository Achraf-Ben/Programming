def convert(celcius):
    farenheit = (celcius * 1.8) + 32
    return farenheit

print('{:^5} {:^7}'.format("F", "C"))
for celcius in range(-30, 41, 10):
    farenheit = convert(celcius)
    print('{:5} {:7}'.format(farenheit, celcius))