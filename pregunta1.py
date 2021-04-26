#Declaración de variables y lista
notas = []
#Bucle for
for i in range(5):
    condi = 1
    #Bucle While, perciste hasta que la nota sea correcta y entre 0 y 20
    while True:
        # valida que valor no sea distinto de numero
        try:
            valor = float(input(f'ingrese la nota {i + 1}\n'))
                 
        except ValueError:
            print('El dato ingresado no es número \n')
            continue
        
        # valida nota entre 0 y 20
        if valor > 20 or valor < 0:
            print('La nota ingresada es menor de cero o mayor a 20, por favor corregir \n')
            continue
        else:#ingresa valor a la lista
            notas.append(valor)
            break 
print(f'Las notas ingresadas fueron; {notas}\n')            
print(f'el valor minimo es: {min(notas)} \nel valor maximo es: {max(notas)} \nel promedio de las notas es: {sum(notas)/len(notas)} \n')
