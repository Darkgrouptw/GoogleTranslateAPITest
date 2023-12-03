import requests
import json

# Read File
def ReadFile(pPath):
    f = open(pPath, "r")
    data = f.read()
    print(data)
    j = json.load(str(data))
    print (j)
    f.close()
    return j


ReadFile("GoogleAPIKey/GoogleAPIKey.box")

