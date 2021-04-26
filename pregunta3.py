#Declaración de variables y lista
cant = int(input(f'Cuantos alumnos registrará?\n'))
alumnos = dict()

#Ingresar los datos de cada alumno
for j in range(cant):
    nom = input(f'Cual es el nombre del alumno N° {j + 1}?\n')
    canNot = int(input(f'Cuantas notas ingresará para el alumno {nom}?\n'))
    notas = []
    #Recorremos una lista para ingresar las notas
    for i in range(canNot):
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

    #find e while y agregar datos al diccionario
    alumnos.update(dict(nomAlu = nom, notAlum = notas, min = min(notas), max = max(notas), prom = sum(notas)/len(notas)))

for clave, valor in alumnos.items():
    print(f' la clave es {clave} y el valor es {valor}')