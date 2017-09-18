def kwadraten_som(grondgetallen):
    uitkomst = 0;
    for getal in grondgetallen:
        if (getal >= 0):
            uitkomst = uitkomst + getal*getal
    return uitkomst


print(kwadraten_som([4, 5, 3, -81]))