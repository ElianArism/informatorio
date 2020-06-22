dia1 = int(input('Ingrese la cant de ventas del dia 1: ')) 
dia2 = int(input('Ingrese la cant de ventas del dia 2: '))

if(dia1 > dia2): 
    print('las ventas del dia 1 superaron a las del dia 2')
elif(dia1 == dia2): 
    print('las ventas fueron las mismas en ambos dias')
else: 
    print('las ventas del dia 2 superaron a las del dia 1')

