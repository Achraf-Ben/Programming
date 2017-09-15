lengte = eval(input("Wat is jouw lengte in centimeters? :"))

def lang_genoeg(y):
    y = lengte >= 120  # y is the sum of getallenLijst
    return y

if lang_genoeg(lengte):   # if input is higer then 120
    print("Je bent lang genoeg voor de attractie!")

else:
    print("Sorry je bent te klein.")