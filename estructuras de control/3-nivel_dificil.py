listVegetarian = ['Pimiento', 'Rucula']
listCarnivora = ['Jamon', 'Panceta']

choice = input('Quiere una pizza vegetariana? (Si o No)') 
if(choice.lower() == 'si' or choice.lower() == 'no' ): 
    if(choice.lower() == 'si'):
        print('lista de ingredientes:') 
        i = 0 
        for ingrediente in listVegetarian: 
           
            print(i, '. ', ingrediente, '\n')
            i+= 1 
        
        cIngrediente = int(input('elija su ingrediente (ingrese el numero correspondiente a la lista)')) 
        print('la pizza elegida es vegetariana \n')
        print('Sus ingredientes son: Mozzarella, Tomate y ', listVegetarian[cIngrediente])
    else: 
        print('lista de ingredientes:') 
        i = 0 
        for ingrediente in listCarnivora: 
           
            print(i, '. ', ingrediente, '\n')
            i+= 1 
        
        cIngrediente = int(input('elija su ingrediente (ingrese el numero correspondiente a la lista)')) 
        print('la pizza elegida no es vegetariana \n')
        print('Sus ingredientes son: Mozzarella, Tomate y ', listCarnivora[cIngrediente]) 
else: 
    print('ocurrio un error, intentelo otra vez')