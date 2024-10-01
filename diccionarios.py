numbers = {1: 'uno', 2: 'Dos',3:'Tre'}
print(numbers)

print(numbers[2])

information = { "name": "Facu", 
               "apellido": "Peralta",
               "edad": 29,
               "altura": 1.73}


print(information)
print("-----")
del information["edad"]
print (information)

print("-----")

claves = information.keys()
print(claves)
print(type(claves))

pairs = information.items()
print(pairs)


camerasDictionary = {
    "Nikon Z6III":{
        "precio": 2500,
        "Mpx": 24.4,
        "Sensor type": "Full Frame"
    },
    "Nikon Z5":{
        "precio": 1200,
        "Mpx": 24.4,
        "Sensor type": "Full Frame"
    }
}

print(camerasDictionary["Nikon Z5"])
print(camerasDictionary["Nikon Z6III"])