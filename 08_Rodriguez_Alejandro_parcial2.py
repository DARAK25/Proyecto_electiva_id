{"nombre":"Teclado","Precio":80000,"cantidad":3}
{"nombre":"Mouse","Precio":50000,"cantidad":5}
{"nombre":"Monitor","Precio":70000,"cantidad":2}
{"nombre":"Camara","Precio":120000,"cantidad":1}


def Calcular_total (Precio,cantidad):
    total  = Precio*cantidad
    return total 
total = Calcular_total

for producto in "Teclado","Mouse","Monitor","Camara":
    bajo_Stock = ["productos"]
    bajo_Stock.remove("Mouse", "Teclado")
    bajo_Stock.append("Monitor", "Camara")
    resultado = bajo_Stock[1:2]
    print("Productos con bajo Stock: ", resultado)


   

print(total)



