import pandas as pd

# Ejemplo de datos
data = {
    'Provincia': ['Buenos Aires', 'Córdoba', 'Santa Fe'],
    'Acceso_actual': [500, 300, 200],
    'Nuevo_acceso': [510, 306, 204]
}

df = pd.DataFrame(data)

# Calcular KPI
df['KPI (%)'] = ((df['Nuevo_acceso'] - df['Acceso_actual']) / df['Acceso_actual']) * 100

print(df)