def buscar_preceptores_repetidos(cursos: list, año1: int, año2: int) -> set:
    '''
    Busca los preceptores repetidos en 2 años distintos
    '''
    preceptores_año1 = set()
    preceptores_año2 = set()    

    for curso in cursos:
        if curso['año_division'][0] == año1:
            preceptores_año1.add(curso['preceptor'])
    
    for curso in cursos:
        if curso['año_division'][0] == año2:
            preceptores_año2.add(curso['preceptor'])
    
    preceptores_repetidos = preceptores_año1.intersection(preceptores_año2)
    
    return preceptores_repetidos

def buscar_preceptores_año(cursos: list, año: int) ->set:
    '''
    Busca preceptores que esten solamente
    en un año especifico
    '''
    preceptores_año = set()
    preceptores_repetidos = set()

    for curso in cursos:
        if curso['año_division'][0] == año:
            preceptores_año.add(curso['preceptor'])
    
    for curso in cursos:
        if curso['año_division'][0] != año:
            preceptores_repetidos.add(curso['preceptor'])
    
    preceptores_total = preceptores_año - preceptores_repetidos
    
    return preceptores_total