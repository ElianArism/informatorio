def nroLetra(l): 
    i = 0
    for letra in abc: 
        if(l == letra): 
            return i
        i+= 1 
    return i
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'v', 'w', 'x', 'y', 'z']

nBarrio = input('ingrese el nombre del barrio')
ubicacion = input('ingrese la ubicacion C (Centrico) - NC (No Centrico)').upper()
nBarrio = nroLetra(nBarrio[0:1].lower())

if((ubicacion == 'C' and nBarrio < 12) or (ubicacion == 'NC' and nBarrio > 12)): 
    print('Su barrio se encuentra en la Seccion A')
else: 
    print('Su barrio se encuentra en la Seccion B')
