
def delKlinkers(woord):
    'This returns a given word without vowels'
    result = ''
    for char in woord:  # loop
        if char not in 'aeiou':
            result = result + char
    return result # returns result to variable result

delKlinkers('Achraf')
