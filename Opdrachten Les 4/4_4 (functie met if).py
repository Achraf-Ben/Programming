def new_password(check): #new_password function
    newpassword = input('Geef uw nieuwe wachtwoord op:')
    if len(newpassword) <= 6 and newpassword != oldpassword: #if length of newpassword is less then 6
        print('False')
    else:
        print('True')


oldpassword = input('Geef uw oude wachtwoord: ')
new_password(oldpassword)

k=input("press close to exit")