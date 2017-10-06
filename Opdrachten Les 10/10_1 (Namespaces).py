import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

dictionary = processXML('10_1.xml')
artikelNaam = []

for artikel in dictionary['artikelen']['artikel']:
    artikelNaam.append(artikel['naam'])

print(artikelNaam)

d = input("Press a key")


