#Declaración de variables y lista
notas = []
nom = input(f'Cual es el nombre del alumno?\n')
cant = int(input(f'Cuantas notas ingresará?\n'))
#Bucle for
for i in range(cant):
    condi = 1
    #Bucle While, perciste hasta que la nota sea correcta y entre 0 y 20
    while True:
        # valida otro valor distinto de numero
        try:
            valor = float(input(f'ingrese la nota {i + 1}\n'))
                 
        except ValueError:
            print('El dato ingresado no es número \n')
            continue
        
        #valida que se encuntre entre 0 y 20
        if valor > 20 or valor < 0:
            print('La nota ingresada es menor de cero o mayor a 20, por favor corregir \n')
            continue
        else:#ingresa valor a la lista
            notas.append(valor)
            break 
print(f'\n Las notas ingresadas del alumno {nom}, fueron; {notas}\n')            
print(f'el valor minimo es: {min(notas)} \nel valor maximo es: {max(notas)} \nel promedio de las notas es: {sum(notas)/len(notas)} \n')
