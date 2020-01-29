import random
def cargarDiccionario():
    archivo = open("listado-general.txt", "r")
    diccionario = []
    for linea in archivo.readlines():
        diccionario.append(linea[:-1])
    return diccionario


grafico = [
    '''
        ________
        |       |
        X       |
       /|\\      |
        |       |   ¡Hás perdido!
       / \\      |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
       /|\\      |
        |       |
       /        |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
       /|\\      |
        |       |
                |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
       /|       |
        |       |
                |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
        |       |
        |       |
                |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
                |
                |
                |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
                |
                |
                |
                |
                |
                |
            ---------
    '''
]

grafico_victoria = [
    '''
        ________
        |       |
        X       |
       /|\\      |
        |       |   ¡Hás perdido!
       / \\      |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
       /|\\      |
        |       |   ¡Hás Ganado, Felicitaciones!
       /        |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
       /|\\      |
        |       |   ¡Hás Ganado, Felicitaciones!
                |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
       /|       |
        |       |   ¡Hás Ganado, Felicitaciones!
                |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
        |       |
        |       |   ¡Hás Ganado, Felicitaciones!
                |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
        0       |
                |
                |   ¡Hás Ganado, Felicitaciones!
                |
                |
                |
            ---------
    ''',
    '''
        ________
        |       |
                |
                |
                |   ¡Hás Ganado, Felicitaciones!
                |
                |
                |
            ---------
    '''
]

def verificarLetra(letra_ingresada):
    index = 0
    resp = False
    for letra in palabra_comparacion:
        if letra == letra_ingresada:
            aciertos[index] = True
            resp = True
        index = index + 1
    
    


    return resp

def verificarResultado():
    for var in aciertos:
        if not var:
            return False

    return True 

def muestraEstadoVictoria(opnciones):
    print(grafico_victoria[opnciones])

def muestraEstado(opnciones):
    print(grafico[opnciones])

def muestra_palabra(iscompleta):
    if iscompleta:
        for letra in palabra:
            print(" " + letra.upper()+ " ", end="")
    else:
        var = 0
        for letra in palabra:
            if aciertos[var]:
                print(" " + palabra[var].upper()+ " ", end="")
            else:
                print(" _ ", end="")
            
            var = var + 1

    print("\n")

    print("Letras seleccionadas: ", end="")
    for letra in letras_elegidas:
        print(letra.upper(), end=" ")
    
    print("\n")

def guardarLetraIngresada(letra_ingresada):
    resp = False
    for letra in letras_elegidas:
        if letra == letra_ingresada:
            resp = True
    if not resp:
        letras_elegidas.append(letra_ingresada)

def cargaPalabraComparacion():
    for letra in palabra:
        if letra == "á":
            palabra_comparacion.append("a")
        elif letra == "é":
            palabra_comparacion.append("e")
        elif letra == "í":
            palabra_comparacion.append("i")
        elif letra == "ó":
            palabra_comparacion.append("o")
        elif letra == "ú":
            palabra_comparacion.append("u")
        else:
            palabra_comparacion.append(letra)

#--------  INICIA PROGRAMA  ---------
jugar = True
palabra = []
palabra_comparacion = []
aciertos = []
letras_elegidas = []

cantidad_intentos = 0

diccionario = cargarDiccionario()

while jugar:
    palabra = list(diccionario[random.randint(0, len(diccionario))])
    cantidad_intentos = 6
    aciertos = []
    letras_elegidas = []
    palabra_comparacion = []
    cargaPalabraComparacion()
    for letra in palabra:
        aciertos.append(False)
    
    muestraEstado(cantidad_intentos)
    muestra_palabra(False)

     #---- COMIENZA EL JUEGO -------
    while cantidad_intentos > 0:


        while True:
            letra_ingresada = input("Ingrese la letra que desea seleccionar: ")
            
            if len(letra_ingresada) == 1:
                if letra_ingresada.isalpha():
                    break
        
        print(" ------- ------ ------ ------ ------ ------")

        guardarLetraIngresada(letra_ingresada)
        
        
        if not verificarLetra(letra_ingresada):
            cantidad_intentos = cantidad_intentos - 1

        #--- Ha GANADO??? -----
        if verificarResultado():
            muestraEstadoVictoria(cantidad_intentos)
            muestra_palabra(True)
            break
        else:
            muestraEstado(cantidad_intentos)
            if cantidad_intentos == 0:
                muestra_palabra(True)
            else:
                muestra_palabra(False)
        
        

    
    


    #---- jugar otra vez? ------
    resp = input("¿Desea jugar otra vez? Si/No: ")
    if resp.lower().startswith("s"):
        jugar = True
    else:
        jugar = False