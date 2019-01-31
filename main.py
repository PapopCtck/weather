from json import dumps
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
import os

fileName = input("File :").casefold()
fileName = os.path.splitext(os.path.basename(fileName))[0]

with open(fileName+".xml", 'r') as f:
    xmlString = f.read()
jsonString = dumps(bf.data(fromstring(xmlString)),indent=4)
print(jsonString)

with open(fileName+".json", 'w') as f:
    f.write(jsonString)