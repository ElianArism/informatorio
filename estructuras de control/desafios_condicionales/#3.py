
cantCompuesto = int(input('ingrese la cant. de metros cuadrados por hectarea que abarca el fertilizante (Nros enteros):  ' ))
porcentaje = (cantCompuesto / 10000) * 100

if(porcentaje >= 10):

    existenMatorrales = input('Existe vegetacion de tipo matorral en su suelo? (Si o No):  ').lower()

    if(existenMatorrales == 'si' or existenMatorrales == 'no'): 

        if(existenMatorrales == 'no'): 
            print('Es factible la utilizacion de fertilizantes')
        else: 
            print('No es factible la utilizacion de fertilizantes')

    else: 
        print('Ocurrio un error')

else: 
    print('No es factible la utilizacion de fertilizantes')