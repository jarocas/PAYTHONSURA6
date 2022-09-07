#Los diccionarios son variables especiales que mepermiten almacenar multiples datos de dufernete tipo en una sola variable.

empleado={
    'nombre':"James",
    'cedula':1067840732,
    'cargo':"Analista de datos",
    'salario': 8000000,
    'horasTrabajadas': 40,
    'aplicaSubsidioTransporte':False,
    'deuda':[1500000,8000000]
}
print(empleado)
print(empleado['deuda'][1])

#Recorriendo un diccionario:
for observadorAtrivuto,observadorValor in empleado.items():
    print(observadorAtrivuto)
    print(observadorValor)