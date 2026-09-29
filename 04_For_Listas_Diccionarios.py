contador = 1

while contador <= 5: #Imprime valores dentro de una condición mientras sea verdadera
    print(contador)
    contador += 1

for numero in range (1,6): #Coloca los valores que estan dentro del rango
    print (numero)

print("///////////")

for number in range (5): #forma de escribirlo
    print (number)

print("///////////")

#range(1,6): final e inicio no incluido

for rango in range(0,11,2): #Se salta de 2 en 2 
    print(rango)

print("///////////")

for nomber in range (11,1,-2):
    print(nomber)

print("///////////")

#for con acumulador

total = 0
#Contador
print("///////////")
for vuelta in range(4):
    numero = int (input ("numero: "))
    total = total + numero
print ("Total: ", total)

print("///////////")
#FOR + IF

for number in range (0,11):
    if number %2 == 0:
        print(number, "es impar")
else:
    print(number, "es impar")

print("///////////")

#Contar y acumular dentro de un for

contador = 0
suma = 0
for numero in range (1,11):
    if numero %2 == 0:
        contador += 1
        suma += numero

print ("cantidad de pares: ", contador)
print ("suma de pares:", suma)
print("///////////")

#Break termina unn ciclo 
#continue solo salta esa vuelta

for namber in range(1,8): #Continue
    if namber == 3:
        continue
    print(namber)
print("///////////")

for nuer in range(1,7):
    if nuer == 4:
        break
print(nuer)
print("///////////")

texto = "hola"
for letra in texto:
    print("letra: ", letra)

texto = "Area Técnica"
texto = texto.lower()

if letra in "Aeiouáéíóú":
    ...

print("///////////")

texto = "python"
len(texto) # 6
texto[0] #p
texto[-1] #n
texto[0:3] #pyt
texto[::-1] #nohtyp

print("///////////")

notas = [4.5, 5.0, 3.0, 2.5, 4.8 , 3.2]
print (notas [0]) #?
print (notas [-1]) #?
print (len(notas)) #?

print("///////////")

#Recorrer listas con for

notas = [4.5, 4.2, 4.9, 3.0]
for nota in notas:
    print ("Nota: ", nota)

print("///////////")

suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
