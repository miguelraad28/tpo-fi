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
        eventos_realizados.append([id_evento,cantidad_de_fotos, costos_fotografias, precio_por_unidad , facturacion, costo_total, ganancia ])
        
        
        
    
generar_datos_del_mes(parametros)


def facturacion_costos_eventos(tipo_evento, eventos_realizados):
    if tipo_evento == 0:
        total_facturacion = 0
        for evento in eventos_realizados:
            total_facturacion += evento[4]

        total_costos = 0
        for evento in eventos_realizados:
            total_costos += evento[5]
        
        cantidad_eventos = len(eventos_realizados)
        
    else:
        total_facturacion = 0
        for evento in eventos_realizados:
            if evento[0] == tipo_evento:
                total_facturacion += evento[4]

        total_costos = 0
        for evento in eventos_realizados:
            if evento[0] == tipo_evento:
                total_costos += evento[5]
        
        cantidad_eventos = 0
        for evento in eventos_realizados:
            if evento[0] == tipo_evento:
                cantidad_eventos += 1
        
    return total_facturacion, total_costos, cantidad_eventos


fac, costos, ev = facturacion_costos_eventos(5, eventos_realizados)

print("Facturación: ", fac, " Costos: ", costos, " Cantidad de eventos: ", ev)
# # Imprimir la matriz
# for fila in matriz:
#     print(fila)
# # Necesitamos saber
# # Total de la facturación del mes
# # Costos del mes
# # Cantidad de eventos del mes
# # Total de facturación por tipo de evento
# # Costo total pol tipo de evento
# # Listado de eventos ordenado por facturación, indicar su tipo
# # Facturación y cantidad de fotos de cada uno de los eventos de un tipo

# tipos_de_eventos=


