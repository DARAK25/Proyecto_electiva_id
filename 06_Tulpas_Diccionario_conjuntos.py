# Listas

lista = [29, True, 3.1415, "El número de Avogadro sí que mola"]

print(lista)
print(lista[-1])
print(lista[1:3])

lista[2] = "He cambiado este elemento"

lista[2] = [3, 2, 1]
print(lista)

print(len(lista))

lista_nueva = [1, 2, 3, 4, 5]
##############################
lista_nueva.append(3)

print(lista_nueva)

print(lista_nueva.count(3))

print(lista_nueva.index(4))

lista_nueva.remove(3)

print(lista_nueva)

###############################
# Tuplas

tupla = ("¿La tierra es plana?", True, False)
print(tupla)   

print(tupla[0])
print(tupla[1])
print(tupla[2])

print(tupla.count(True))
print(tupla.index(False))

print((1))
print((1,))
#######################################

# Conjunto

print(set())

print(set([5, 2, 5, 1, 1.5]))
print(set((5, 2, 5, 1, 1.5)))
print(set("52511.5"))

conjunto = set([2, 3, 3, 4])
conjunto_2 = set([5, 3, 5, 6])
conjunto_3 = set([4, 2])

print(conjunto)
print(conjunto_2)
print(conjunto_3)

conjunto.add(1)
print(conjunto)

conjunto.remove(1)
print(conjunto)

print(conjunto.intersection(conjunto_2))
print(conjunto_2.issubset(conjunto))
print(conjunto_3.issubset(conjunto))

##############################
# Diccionario

diccionario = {1: "Uno", 2: "Dos"}
diccionario[3] = "Tres"
print(diccionario)

dict_lista_tuplas = dict([(1, "Uno"), (2, "Dos"), (3, "Tres")])
print(dict_lista_tuplas)

dict_lista_string = dict(Uno = 1, Dos = 2, Tres = 3)
print(dict_lista_string)

dict_tipos = {1: "integer", 
              2.2: "float", 
              "texto": "string", 
              (1, 2): "tupla"}

print(dict_tipos)

dict_repeticion = {1: "Primero", 1: "Último"}
print(dict_repeticion)

print(diccionario, 
      diccionario.keys(), 
      diccionario.values(), 
      diccionario.items())

claves = diccionario.values()
print(claves)
diccionario[1] = "One"
print(claves)
diccionario.pop(2)
print(diccionario)

###################################

personajes = ["Kakyoin", "Joseph", "Jotaro"]
personajes.remove("Kakyoin")
personajes.append("Polnareff")
resultado = personajes[1:2]
print(resultado)

respuesta = ("Yes","Yes","Yes")
resultado = (respuesta.count("Yes"), respuesta.index("Yes"))
print(resultado)

temporada_2 = set(["Joseph", "Caesar"])
temporada_3 = set(["Jotaro", "Joseph", "Avdol", "Kakyoin", "Polnareff"])
resultado = temporada_2 & temporada_3
print(resultado)

protas = {1: "Jonnathan", 2: "Joseph", 3: "Jotaro"}
jojos = {"Jonnathan": "Phantom Blood",
         "Joseph": "Battle Tendency",
         "Jotaro": "Stardust Crusaders"}
resultado = jojos[protas[3]]
print(resultado)

