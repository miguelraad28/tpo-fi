import random

parametros = [
    # <= 500, > 500, > 1000, costo
    [750, 650, 600, 50000], #Casamiento
    [850, 750, 700, 60000], #15 años
    [650, 550, 550, 35000], #Cumpleaños
    [750, 650, 650, 38000], #Bautismo
    [1000, 900, 800, 25000] #Otros
]
# ELIMINAR: 
# encabezado = [ ]

def generar_datos_del_mes(parametros):
    eventos_realizados_en_el_mes = random.randint(30,80)
    
    eventos = []

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
        
        # ["Id evento","Facturación", "Costo total", "Cantidad de fotos" ,"Costos fotografías" ,"Precio por foto", "Ganancia" ]
        eventos.append([id_evento, facturacion, costo_total, cantidad_de_fotos, costos_fotografias, precio_por_unidad, ganancia ])

    return eventos

def facturacion_costos_eventos(tipo_evento, datos):
    if tipo_evento == 0:
        # 1) Total de la facturación del mes, los costos y cuantos eventos fueron
        total_facturacion = 0
        for evento in datos:
            total_facturacion += evento[1]

        total_costos = 0
        for evento in datos:
            total_costos += evento[2]
        
        cantidad_eventos = len(datos)
    else:
        # Muestra por tipo de evento
        total_facturacion = 0
        for evento in datos:
            if evento[0] == tipo_evento:
                total_facturacion += evento[1]

        total_costos = 0
        for evento in datos:
            if evento[0] == tipo_evento:
                total_costos += evento[2]
        
        cantidad_eventos = 0
        for evento in datos:
            if evento[0] == tipo_evento:
                cantidad_eventos += 1
        
    return total_facturacion, total_costos, cantidad_eventos


def bubble_sort(matriz):
    n = len(matriz)
    
    for i in range(n):
        for j in range(0, n-i-1):
        
            if matriz[j][1] < matriz[j+1][1]:
                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]

    return matriz


def traer_por_tipo():
    datos_por_eventos = []
    for id_evento in range(1,6):
        fac, costos, ev = facturacion_costos_eventos(id_evento, eventos_realizados)
        datos_por_eventos.append([id_evento, fac, costos, ev])
    return datos_por_eventos


#Funcion que imprime el menu por pantalla
def imprimir_menu():
    print()
    print("********************************************")
    print("Debe elegir una opcion, solo numeros enteros")
    print("1 - Total de la facturación del mes, los costos y cuantos eventos fueron")   
    print("2 - Total de facturación por tipo de evento, el costo y la cantidad de eventos ordenado por facturación")
    print("3 - Listado completo detallado del total facturado de cada evento con su tipo, ordenado por total facturado")
    print("4 - Ver datos de eventos (Casamientos)")
    print("5 - Ver datos de eventos (15 Años)")
    print("6 - Ver datos de eventos (Cumpleaños)")
    print("7 - Ver datos de eventos (Bautismo)")
    print("8 - Ver datos de eventos (Otros)")
    print("0 - Salir")
    print("********************************************")
    print()

    return

#Funcion que valida que las opciones elegidas del menu sean las correctas.
#Solo valida numeros. Si se ingresa letras se corta el programa.
def validar_opcion_menu(opcion):
    flag=True
    if 0 > opcion > 8: #Se ha ingresado un valor invalido por menu
        flag=False
    
    return flag

#************************
#Programa principal
#************************

# Generación de datos acorde parametros
eventos_realizados = generar_datos_del_mes(parametros)

print("Bienvenido al programa")
print()

#Leer la primera vez la opcion del menu
imprimir_menu()
opcion = int(input("Ingrese la opcion elegida del menu principal: "))

#Comienzo del proceso de las opciones del menu elegidas.
while opcion != 0:

    flagMenu=validar_opcion_menu(opcion)
    while flagMenu == False:
        print("Opcion de menu invalida, vuelva a ingresar...")
        print()
        opcion=int(input("Ingrese la opcion elegida del menu principal: "))
        flagMenu=validar_opcion_menu(opcion)

    #Analizamos las opciones validas del menú
    if opcion==1:
        #Instrucciones para la opcion 1
        print()
        print("Has elegido la opcion 1")
        facturacion, costos, cant_eventos = facturacion_costos_eventos(0, eventos_realizados)
        print()
        print("Facturación total: $", facturacion, " Costos totales: $", costos, " Cantidad de eventos: ", cant_eventos)
    elif opcion==2:
        print()
        print("Has elegido la opcion 2")
        matriz_por_tipo = traer_por_tipo()
        matriz_ordenada = bubble_sort(matriz_por_tipo)
        print()
        for tipo_evento in matriz_por_tipo:
            match tipo_evento[0]:
                case 1:
                    print("Casamientos (",tipo_evento[3],") - Facturación: $", tipo_evento[1], " Costos: $", tipo_evento[2])
                case 2:
                    print("15 Años (",tipo_evento[3],") - Facturación: $", tipo_evento[1], " Costos: $", tipo_evento[2])
                case 3:
                    print("Cumpleaños (",tipo_evento[3],") - Facturación: $", tipo_evento[1], " Costos: $", tipo_evento[2])
                case 4:
                    print("Bautismos (",tipo_evento[3],") - Facturación: $", tipo_evento[1], " Costos: $", tipo_evento[2])
                case 5:
                    print("Otros (",tipo_evento[3],") - Facturación: $", tipo_evento[1], " Costos: $", tipo_evento[2])
        #impresion de datos para opcion 2
    elif opcion==3:
        print("Has elegido la opcion 3")
        matriz_ordenada = bubble_sort(eventos_realizados)

        for tipo_evento in eventos_realizados:
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
            print("Tipo de evento:", nombre_evento)
            print("  Facturación: $", tipo_evento[1], " - Costo total: $", tipo_evento[2])
            print("  Cantidad de fotos:", tipo_evento[3], "- Precio de venta x foto: $", tipo_evento[5])
            print()
    elif opcion==4:
        print("Has elegido la opcion 1")
        facturacion, costos, cant_eventos = facturacion_costos_eventos(1, eventos_realizados)
        print()
        print("Tipo de evento: Casamientos")
        print(" Facturación total: $", facturacion, " Costos totales: $", costos, " Cantidad de eventos: ", cant_eventos)
    elif opcion==5:
        print("Has elegido la opcion 1")
        facturacion, costos, cant_eventos = facturacion_costos_eventos(2, eventos_realizados)
        print()
        print("Tipo de evento: 15 Años")
        print(" Facturación total: $", facturacion, " Costos totales: $", costos, " Cantidad de eventos: ", cant_eventos)
    elif opcion==6:
        print("Has elegido la opcion 1")
        facturacion, costos, cant_eventos = facturacion_costos_eventos(3, eventos_realizados)
        print()
        print("Tipo de evento: Cumpleaños")
        print(" Facturación total: $", facturacion, " Costos totales: $", costos, " Cantidad de eventos: ", cant_eventos)
    elif opcion==7:
        print("Has elegido la opcion 1")
        facturacion, costos, cant_eventos = facturacion_costos_eventos(4, eventos_realizados)
        print()
        print("Tipo de evento: Bautismos")
        print(" Facturación total: $", facturacion, " Costos totales: $", costos, " Cantidad de eventos: ", cant_eventos)
    elif opcion==8:
        print("Has elegido la opcion 1")
        facturacion, costos, cant_eventos = facturacion_costos_eventos(5, eventos_realizados)
        print()
        print("Tipo de evento: Otros")
        print(" Facturación total: $", facturacion, " Costos totales: $", costos, " Cantidad de eventos: ", cant_eventos)

    #Luego de procesar la opcion del menu elegida
    #Vuelvo a invocar al menu
    imprimir_menu()   
    opcion=int(input("Ingrese la opcion elegida del menu principal: "))
else:
    print("FIN DEL PROGRAMA")

#Fin del programa