
tamañoPez = ['Normal', 'Debajo de lo normal', 'Poco por encima de lo normal', 'Sobredimensionado']

print('Esta es la lista de tamaños: ')
i = 0
for tamaño in tamañoPez: 
    print(i, '_ Tamaño: ', tamaño)
    i += 1

tamañoIngresado = int(input('Ingrese el numero correspondiente al tamaño del pez')) 

if(tamañoIngresado >= 0 and tamañoIngresado < 4):
    if(tamañoIngresado == 0):
        print("Pez en buenas condiciones")
    elif(tamañoIngresado == 1): 
        print("Pez con problemas de nutrición")
    elif(tamañoIngresado == 2): 
        print("Pez con síntomas de organismo contaminado")
    else: 
        print("Pez contaminado")
else: 
    print('ocurrio un error, intentelo de nuevo')


