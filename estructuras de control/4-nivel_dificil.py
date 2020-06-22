turno = input('ingrese su turno (Tarde o Noche)')
turno = turno.lower() 
nombre = input('ingrese su nombre')
nombre = nombre.lower()
nombre = nombre[0:1]

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'v', 'w', 'x', 'y', 'z']

if(turno == 'tarde' or turno == 'noche'):
    if(turno == 'tarde'):  
        i = 0
        for letra in abc:
            if(nombre is letra): 
                if(i <= 12): 
                    print('su grupo es A')
            i+= 1
        else: 
            print('su grupo es B')
            
    elif(turno == 'noche'): 
        i = 0
        for letra in abc:
            if(nombre is letra): 
                if(i >= 13): 
                    print('su grupo es A')
            i+= 1
        else: 
            print('su grupo es B')
        
else: 
    print('algo salio mal, intentelo de nuevo')
        
                
         


    