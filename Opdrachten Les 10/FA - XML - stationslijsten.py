import xmltodict

def processXML(filename):
    'Proces XML file'
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

dictionary = processXML('stations.xml')

print("\n Dit zijn de codes en types van de 4 stations:")
for station in dictionary['Stations']['Station']:
    print('{}  -  {}'.format(station['Code'],station['Type']))

print('\n Dit zijn alle stations met één of meer synoniemen:')
for station in dictionary['Stations']['Station']:
    synoniemen = station['Synoniemen']
    if station['Synoniemen'] is not None:
        print('{}  -  {}'.format(station['Code'],synoniemen['Synoniem']))


print("\n Dit is de lange naamvan elk station:")
for station in dictionary['Stations']['Station']:
    langeNaam = station['Namen']
    print('{}  -  {}'.format(station['Code'],langeNaam['Lang']))

d = input("Press a key")


