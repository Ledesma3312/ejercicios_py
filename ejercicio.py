# Inicializa listas vacías para almacenar datos de edad, peso, altura, sueldo y sexo
listaEdad = [] 
listaPeso = []
listaAltura = []
listaSueldo = []
listaSexoM = []  # Lista para almacenar si es mujer (1) o no (0)
listaSexoH = []  # Lista para almacenar si es hombre (1) o no (0)

# Crea una lista que agrupa las listas de sexo por columnas
listaColumnaSexo = [listaSexoH, listaSexoM]

# Inicializa un contador en 1 para recorrer las personas
contador = 1

# Solicita la cantidad de personas a agregar y lo guarda como un entero
personas = int(input('Cuantas personas agregarás? '))

# Bucle que se ejecuta hasta que se agreguen los datos de todas las personas
while(contador <= personas):
    # Solicita y almacena la edad de la persona como entero
    edad = int(input('edad: '))
    listaEdad.append(edad)
    
    # Solicita y almacena el peso de la persona como flotante
    peso = float(input('peso: '))
    listaPeso.append(peso)
    
    # Solicita y almacena la altura de la persona como flotante
    altura = float(input('altura: '))
    listaAltura.append(altura)
    
    # Solicita y almacena el sueldo de la persona como flotante
    sueldo = float(input('sueldo :'))
    listaSueldo.append(sueldo)
    
    # Solicita el sexo de la persona y lo almacena como 1 para hombre y 0 para mujer
    while True:
        sexo = input('Sexo (h/m): ').lower()
        print('\n')
        if sexo =='h':  # Si el usuario ingresa 'h', se almacena 1 en listaSexoH y 0 en listaSexoM
            listaSexoH.append(1)
            listaSexoM.append(0)
            break
        elif sexo == 'm':  # Si el usuario ingresa 'm', se almacena 1 en listaSexoM y 0 en listaSexoH
            listaSexoM.append(1)
            listaSexoH.append(0)
            break
        else:
            # Si el usuario ingresa un valor inválido, se solicita que ingrese un valor válido
            print('Ingresa un sexo válido (h para hombre, m para mujer).')
    
    # Incrementa el contador en 1 para pasar a la siguiente persona
    contador = contador + 1

# Función para normalizar los valores de una lista
def normalizar(lista):
    # Obtiene el valor mínimo de la lista
    minLista = min(lista)
    
    # Obtiene el valor máximo de la lista
    maxLista= max(lista)
    
    # Inicializa un contador para identificar la persona
    contadorPersonas=0
    
    # Ordena la lista de menor a mayor
    lista.sort()
    
    # Itera sobre cada valor en la lista
    for i in lista:
        contadorPersonas +=1
        try:
            # Aplica la fórmula de normalización: (valor - mínimo) / (máximo - mínimo)
            norm = (i - minLista) / (maxLista - minLista) 
        except ZeroDivisionError:
            # Si ocurre una división por cero, se maneja el error y se retorna 0
            return 0
        finally:
            # Imprime el número de persona, el valor original y su normalización
            print(f'Persona {contadorPersonas}--valor: {i:.2f} -- Normalizacion : {norm}')

# Imprime la normalización de las diferentes listas de datos
print('Normalizacion de edades: ')
normalizar(listaEdad)
print('\n')

print('Normalizacion de pesos: ')
normalizar(listaPeso)
print('\n')

print('Normalizacion de altura: ')
normalizar(listaAltura)
print('\n')

print('Normalizacion de Sueldo: ')
normalizar(listaSueldo)
print('\n')

# Imprime la normalización de los datos de sexo por persona
print('Normalización de Sexo:')
for i in range(personas):  
    hombre = listaColumnaSexo[0]  # Accede a listaSexoH
    mujer = listaColumnaSexo[1]  # Accede a listaSexoM
    
    # Imprime si la persona es hombre (1) o mujer (1) según la lista correspondiente
    print(f'Persona { i + 1} --hombre  --mujer \n             {hombre[i]}         {mujer[i]}')
