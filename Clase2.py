import pandas as pd
file_path = "/Users/andres/Downloads/spotify.csv"

df = pd.read_csv(file_path)
print(f'Info del DataFrame')
df.info()


# Valores nulos por columna
print("Valores nulos por columna:")
valores_nulos = df.isnull().sum()
print(valores_nulos)

print("Valores de la columna Duration ms:")
print(df['duration_ms'])

# mediana
print("Mediana Duration ms:")
mediana = df['duration_ms'].median()
print(mediana)

# moda
print("Moda en Duration ms:")
moda = df['duration_ms'].mode()
print(moda)


# media
print("media en Duration ms:")
media = df['duration_ms'].mean()
print(media)

# Desviación estándar
print("Desviacion Estandar en Duration ms:")
desv_estandar = df['duration_ms'].std()
print(desv_estandar)