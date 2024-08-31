# Solicita la cantidad de personas a agregar y lo guarda como un entero
personas = int(input('Cuantas personas agregarás? '))

# Inicializa un contador en 1
contador = 1

# Inicializa listas vacías para almacenar datos de edad, peso, altura, sueldo y sexo
listaEdad = [] 
listaPeso = []
listaAltura = []
listaSueldo = []
listaSexo = []

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
        if sexo == 'h':  # Si el usuario ingresa 'h', se almacena 1 en la lista de sexo
            listaSexo.append(1)
            break
        elif sexo == 'm':  # Si el usuario ingresa 'm', se almacena 0 en la lista de sexo
            listaSexo.append(0)
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
    maxLista = max(lista)
    
    # Itera sobre cada valor en la lista
    for i in lista:
        norm = 0
        try:
            # Aplica la fórmula de normalización: (valor - mínimo) / (máximo - mínimo)
            norm = (i - minLista) / (maxLista - minLista) 
        except ZeroDivisionError:
            # Maneja el caso en que el máximo y mínimo sean iguales, lo que provocaría una división entre 0
            print('division entre 0 no permitida')
            return 0
        finally:
            # Imprime el valor original y su normalización
            print(f'valor: {i} Normalizacion : {norm:.2f}')


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

print('Normalizacion de Sexo: ')
normalizar(listaSexo)
