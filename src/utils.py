import pandas as pd

def clasificar_familia(cant):
    """Clasifica el tamaño del grupo familiar basado en la cantidad de miembros."""
    if cant == 0:
        return 'Solo'
    elif cant <= 3:
        return 'Familia Pequeña'
    else:
        return 'Familia Grande'

def segmentar_edad(edad):
    """Segmenta la edad en rangos categóricos para el análisis estadístico."""
    if edad < 12:
        return 'Niño'
    elif edad <= 18:
        return 'Adolescente'
    elif edad <= 60:
        return 'Adulto'
    else:
        return 'Mayor'
