file_in = open('kaartnummers.txt', 'r')

smallestInt = 0

intList = [int(x.split(",")[0]) for x in file_in.readlines()]
print(intList)
regels = len(intList)
number = max(intList)
laatsteregel = ''

string_format = 'Deze file telt {0} regels\n' \
                'Het grootste kaartnummer is: {1} en dat staat op regel {2}'
result = string_format.format(regels, number, laatsteregel)
print(result)