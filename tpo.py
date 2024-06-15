import random

parametros = [
    # <= 500, > 500, > 1000, costo
    [750, 650, 600, 50000], #Casamiento
    [850, 750, 700, 60000], #15 años
    [650, 550, 550, 35000], #Cumpleaños
    [750, 650, 650, 38000], #Bautismo
    [1000, 900, 800, 25000] #Otros
]

encabezado = ["Nombre de evento","Cantidad de fotos", "Costos de fotografías", "Precio por unidad" ,"Facturación total" ,"Costo total del evento", "Ganancia" ]
#!!!!!!!!!!! NO PODEMOS ALMACENAR TEXTO EN VARIABLES, SOLO PUEDEN IMPRIMIRSE O SEA ESCRIBIRLAS DIRECTAMENTE DENTRO DE UN PRINT !!!!!!!
# ESTO HAY QUE CAMBIARLO, LO DEJAMOS SOLO PARA PROBAR COMO IMPRIME

eventos_realizados = []

def generar_datos_del_mes(parametros):
    eventos_realizados_en_el_mes = random.randint(30,80)

    for i in range(0, eventos_realizados_en_el_mes):
        index_evento = random.randint(0, len(parametros) - 1)
        id_evento = index_evento + 1
        cantidad_de_fotos = random.randint(300,5000)

        if cantidad_de_fotos <= 500:
            precio_por_unidad = parametros[index_evento][0]
        elif cantidad_de_fotos > 500 and cantidad_de_fotos < 1000:
            precio_por_unidad = parametros[index_evento][1]
        else:
            precio_por_unidad = parametros[index_evento][2]
            
        costos_fotografias = 50 * cantidad_de_fotos
        
        costo_total = parametros[index_evento][3] + costos_fotografias
        
        facturacion = (cantidad_de_fotos * precio_por_unidad) 
        
        ganancia = facturacion - costo_total
        
        #["Id evento","Cantidad de fotos", "Costos de fotografías", "Precio por unidad" ,"Facturación total" ,"Costo total del evento", "Ganancia" ]
        eventos_realizados.append([id_evento, facturacion, costo_total, cantidad_de_fotos, costos_fotografias, precio_por_unidad, ganancia ])

def facturacion_costos_eventos(tipo_evento, eventos_realizados):
    if tipo_evento == 0:
        # 1) Total de la facturación del mes, los costos y cuantos eventos fueron
        total_facturacion = 0
        for evento in eventos_realizados:
            total_facturacion += evento[1]

        total_costos = 0
        for evento in eventos_realizados:
            total_costos += evento[2]
        
        cantidad_eventos = len(eventos_realizados)
        
    else:
        # Muestra por tipo de evento
        total_facturacion = 0
        for evento in eventos_realizados:
            if evento[0] == tipo_evento:
                total_facturacion += evento[1]

        total_costos = 0
        for evento in eventos_realizados:
            if evento[0] == tipo_evento:
                total_costos += evento[2]
        
        cantidad_eventos = 0
        for evento in eventos_realizados:
            if evento[0] == tipo_evento:
                cantidad_eventos += 1
        
    return total_facturacion, total_costos, cantidad_eventos


def bubble_sort(matriz):
    n = len(matriz)
    
    for i in range(n):
        for j in range(0, n-i-1):
        
            if matriz[j][1] < matriz[j+1][1]:
                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]



def traer_por_tipo():
    datos_por_eventos = []
    for id_evento in range(1,6):
        fac, costos, ev = facturacion_costos_eventos(id_evento, eventos_realizados)
        datos_por_eventos.append([id_evento, fac, costos, ev])
    return datos_por_eventos

generar_datos_del_mes(parametros)

# matriz_por_tipo = traer_por_tipo()

# bubble_sort(matriz_por_tipo)
# for tipo_evento in matriz_por_tipo:
#     match tipo_evento[0]:
#         case 1:
#             print("Casamientos - Facturación: ", tipo_evento[1], " Costos: ", tipo_evento[2], " Cantidad de eventos: ", tipo_evento[3])
#         case 2:
#             print("15 Años - Facturación: ", tipo_evento[1], " Costos: ", tipo_evento[2], " Cantidad de eventos: ", tipo_evento[3])
#         case 3:
#             print("Cumpleaños - Facturación: ", tipo_evento[1], " Costos: ", tipo_evento[2], " Cantidad de eventos: ", tipo_evento[3])
#         case 4:
#             print("Bautismos - Facturación: ", tipo_evento[1], " Costos: ", tipo_evento[2], " Cantidad de eventos: ", tipo_evento[3])
#         case 5:
#             print("Otros - Facturación: ", tipo_evento[1], " Costos: ", tipo_evento[2], " Cantidad de eventos: ", tipo_evento[3])
            
            
bubble_sort(eventos_realizados)

for tipo_evento in eventos_realizados:
    # eventos_realizados.append([id_evento, facturacion, costo_total, cantidad_de_fotos, costos_fotografias, precio_por_unidad, ganancia ])
    match tipo_evento[0]:
        case 1:
            nombre_evento = 'Casamiento'
        case 2:
            nombre_evento = '15 Años'
        case 3:
            nombre_evento = 'Cumpleaños'
        case 4:
            nombre_evento = 'Bautismo'
        case 5:
            nombre_evento = 'Otro'
    print(nombre_evento)
    print("  Facturación: ", tipo_evento[1], " Costo total: ", tipo_evento[2])
    print("  Cantidad de fotos: ", tipo_evento[3], " Precio de venta x foto: ", tipo_evento[5])
    print()


#Funcion que imprime el menu por pantalla
#Se agregan las opciones necesarias segun el programa de cada uno.
def imprimirMenu():
    print()
    print("********************************************")
    print("Debe elegir una opcion, solo numeros enteros")
    print("1 - Elige la opcion 1")   
    print("2 - Elige la opcion 2")
    print("3 - Elige la opcion 3")
    print("0 - Salir")
    print("********************************************")
    print()
    
    return


#Funcion que valida que las opciones elegidas del menu sean las correctas.
#Solo valida numeros. Si se ingresa letras se corta el programa.
#Agregar las opciones necesarias segun el programa de cada uno.

def validarOpcionMenu(opcion):
    flag=True
    if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=0: #Se ha ingresado un valor invalido por menu
        flag=False
    
    return flag
    
#************************   
#Programa principal
#************************   


print("Bienvenido al programa")
print()

#Leer la primera vez la opcion del menu
imprimirMenu()
opcion=int(input("Ingrese la opcion elegida del menu principal: "))

#Comienzo del proceso de las opciones del menu elegidas.

while opcion!=0:

    flagMenu=validarOpcionMenu(opcion)
    while flagMenu == False:
        print("Opcion de menu invalida, vuelva a ingresar...")
        print()
        opcion=int(input("Ingrese la opcion elegida del menu principal: "))
        flagMenu=validarOpcionMenu(opcion)

    #Analizamos las opciones validas del menú
    if opcion==1:
        #Instrucciones para la opcion 1
        print("Has elegido la opcion 1")
        #ingreso de datos para opcion 1
        #proceso de datos para opcion 1
        #impresion de datos para opcion 1
    elif opcion==2:
        print("Has elegido la opcion 2")
        #ingreso de datos para opcion 2
        #proceso de datos para opcion 2
        #impresion de datos para opcion 2
    elif opcion==3:
        print("Has elegido la opcion 3")
        #ingreso de datos para opcion 3
        #proceso de datos para opcion 3
        #impresion de datos para opcion 3

    #Luego de procesar la opcion del menu elegida
    #Vuelvo a invocar al menu
    imprimirMenu()   
    opcion=int(input("Ingrese la opcion elegida del menu principal: "))

else:
    print("FIN DEL PROGRAMA")
    
    

#Fin del programa

# def mostra_listado_por_tipo(tipo_evento, eventos_realizados):
    