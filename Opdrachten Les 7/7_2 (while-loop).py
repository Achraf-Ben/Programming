while True:
    invoer = input('Geef een string van vier letters: ')
    if len(invoer) == 4:
        print('Inlezen van correcte string: {0} is geslaagd.'.format(invoer)
        break
    else:
        print('{0} heeft {1} letters.'.format(invoer,len(invoer)))