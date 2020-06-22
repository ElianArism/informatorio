rec1 = {'Lentejas', 'Apio'}
rec2 = {'Morron', 'Cebolla'}

def listar(rec):   
    i = 0
    rec.add('Verduras')
    rec.add('Berenjena')

    for ing in rec:
        print(i ,'. ', ing)
        i += 1

def elegirIngredientes(): 
    salida = set()
    salida.add(input('ingrese El primer Ingrediente de tres '))
    salida.add(input('ingrese El segundo Ingrediente de tres ')) 
    salida.add(input('ingrese El tercer Ingrediente de tres '))
    return salida 

print('Que tipo de receta desea: \n ')
print('RECETA 1: Lentejas y Apio \n ') 
print('--------------------------\n')
print('RECETA 2: Morron y Cebolla\n')
print('--------------------------\n')
print('\n')


recElegida = int(input('Seleccione (1 o 2): '))

if(recElegida == 1 or recElegida == 2): 
    if(recElegida == 1): 
        listar(rec1)
        salida = elegirIngredientes()
        print('los ingredientes elegidos fueron: ', salida)
    else:
        listar(rec2)
        salida = elegirIngredientes()
        print('los ingredientes elegidos fueron: ', salida)
else: 
    print('ocurrio un error')


      
