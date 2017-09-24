def strings():
    'Function to transforms input into a list'
    list = []

    inputList = input("Geef lijst met minimaal 10 strings: ")

    if inputList[5] == '':
        list.append(inputList.split(","))
        inputList = input("Geef lijst met minimaal 10 strings: ")
    print("De nieuw-gemaakte lijst met alle vier-letter strings is:\n")
    print(list)

    return list

strings()