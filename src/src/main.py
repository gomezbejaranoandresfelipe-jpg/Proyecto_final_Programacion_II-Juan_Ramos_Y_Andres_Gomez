import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Importar las funciones del módulo hermano utils
from utils import clasificar_familia, segmentar_edad

def ejecutar_pipeline():
    print("Iniciando pipeline de análisis de datos...")
    
    # 1. Cargar datos
    df = pd.read_csv('data/train.csv')
    
    # 2. Ingeniería de variables y limpieza de nulos
    df['Familiares'] = df['SibSp'] + df['Parch']
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Tiene_Cabina'] = df['Cabin'].notnull()
    
    # 3. Aplicar funciones desde utils.py
    df['Grupo_Familiar'] = df['Familiares'].apply(clasificar_familia)
    df['Grupo_Etario'] = df['Age'].apply(segmentar_edad)
    
    # 4. Generar y exportar tabla analítica multi-índice
    tabla = df.groupby(['Grupo_Familiar', 'Grupo_Etario', 'Tiene_Cabina'])['Survived'].mean() * 100
    os.makedirs('outputs/tablas/', exist_ok=True)
    tabla.to_csv('outputs/tablas/tabla_analitica_supervivencia.csv')
    print("-> Tabla analítica exportada a outputs/tablas/")
    
    # 5. Generar y guardar gráfico estadístico
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Grupo_Etario', y='Survived', hue='Sex', errorbar=None, palette='muted')
    plt.title('Tasa de Supervivencia por Grupo Etario y Sexo')
    os.makedirs('outputs/graficos/', exist_ok=True)
    plt.savefig('outputs/graficos/supervivencia_etaria.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("-> Gráfico estadístico exportado a outputs/graficos/")
    print("¡Pipeline ejecutado con éxito!")

if __name__ == "__main__":
    ejecutar_pipeline()
