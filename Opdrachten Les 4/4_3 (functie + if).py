lengte = eval(input("Wat is jouw lengte in centimeters? :"))

def lang_genoeg(invoerLengte): #function to check if input is higher then 120
    invoerLengte = lengte >= 120
    return invoerLengte

if lang_genoeg(lengte):   # if input is higer then 120
    print("Je bent lang genoeg voor de attractie!")

else: # if not higher then 120
    print("Sorry je bent te klein.")