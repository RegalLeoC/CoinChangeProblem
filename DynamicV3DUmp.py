import json

#Actualizacion del JSON
def writeToJSONFile(data):
    with open("coin-change.json", "w") as fp:
        json.dump(data, fp)


#Lo que se va a pasar
#Tus denominaciones
den = [1,5,6,9,20,50,100]

#Las nuevas cantidades por moneda
cantidades = [50,2,50,50,0,0,50]

data = {}

for i in range(len(den)):
    data[str(den[i])] = cantidades[i]

writeToJSONFile(data)