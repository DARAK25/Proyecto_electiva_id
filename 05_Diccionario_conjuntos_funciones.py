estudiantes=[
    {"nombre":"Ana", "nota":[4.0,3.5,5.0]},  
    {"nombre":"Luis", "nota":[2.5,3.0,2.8]},
    {"nombre":"Carlos", "nota":[4.5,4.0,4.8]}
]
def calcular_promedio(notas):
    suma=0
    promedio=sum(notas)/len(notas)
    return promedio
    promdioestudiantes =calcular_promedio(estudiante[1]["nota"])
    print(round(promedioestudiantes,2))
for estudiante in estudiantes:
    promedio = calcular_promedio(estudiante["nota"]) 
    if promedio>=3.0:
        estado = "Aprobado"
    else:
        estado = "No aprobado"

    estudiante["promedio"]=round(promedio,2)
    estudiante["estado"]=estado    
print(estudiantes)