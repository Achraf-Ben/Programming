def seizoen(maandnummer):
    maandnummer = str(maandnummer)
    if maandnummer in ('3','4','5'):
        print('Lente')
    elif maandnummer in ('6','7','8'):
        print('Zomer')
    elif maandnummer in ('9','10','11'):
        print('Herfst')
    else:
        print('Winter')

seizoen(1)