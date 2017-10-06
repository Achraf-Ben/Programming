while True:
    try:
        invoer = int(input(": "))
        break
    except ValueError:
        print("Gebruik cijfers voor het invoeren van het aantal!")
    except IOError:
        print("Negatieve getallen zijn niet toegestaan!")
    except ZeroDivisionError:
        print("Delen door nul kan niet!")
    except:
        print("Onjuiste invoer")
