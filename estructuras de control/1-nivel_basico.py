edad = int(input('ingrese su edad')); 

if(edad >= 18): 
    print('usted es mayor de edad'); 
else: 
    print('usted es menor de edad'); 


cantdePreguntas = int(input('Ingrese la cantidad de preguntas'))
cantdeCorrectas = int(input('Ingrese la cantidad de preguntas correctas')) 

porcentaje = (cantdeCorrectas / cantdePreguntas) * 100
if(cantdeCorrectas <= cantdePreguntas):
    if( porcentaje > 89): 
        print('Excelente')
    elif(porcentaje > 69): 
        print('Bueno')
    elif(porcentaje > 59): 
        print('Aprobado')
    elif(porcentaje < 60): 
        print('Desaprobado')




iFallidos = int(input('ingrese la cantidad de intentos fallidos'))
if(iFallidos > 5): 
    print('cuenta bloqueada')