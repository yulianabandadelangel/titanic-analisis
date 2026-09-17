# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# %%
df = pd.read_csv("../data/train.csv")
df.head()

# %%
print("Filas y columnas:", df.shape)
print("\nColumnas:", df.columns.tolist())
print("\nTipos de datos:")
print(df.dtypes)
print("\nNulos por columna:")
print(df.isnull().sum())
print("\nDuplicados:", df.duplicated().sum())

# %%
df.describe(include="all")

# %%
df["Age"] = df["Age"].fillna(df["Age"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df = df.drop(columns=["Cabin"])

df.isnull().sum()

# %%
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

def categoria_edad(edad):
    if edad < 12:
        return "Niño"
    elif edad < 18:
        return "Joven"
    elif edad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"

df["AgeCategory"] = df["Age"].apply(categoria_edad)

df[["Age", "AgeCategory", "SibSp", "Parch", "FamilySize"]].head(10)

# %%
total = len(df)
sobrevivieron = df["Survived"].sum()
porcentaje = (sobrevivieron / total) * 100

print(f"Total de pasajeros: {total}")
print(f"Sobrevivientes: {sobrevivieron}")
print(f"Porcentaje de supervivencia: {porcentaje:.2f}%")

# %%
supervivencia_sexo = df.groupby("Sex")["Survived"].mean() * 100
print("Porcentaje de supervivencia por sexo:")
print(supervivencia_sexo.round(2))

# %%
supervivencia_clase = df.groupby("Pclass")["Survived"].mean() * 100
print("Porcentaje de supervivencia por clase:")
print(supervivencia_clase.round(2))

# %%
supervivencia_edad = df.groupby("AgeCategory")["Survived"].mean() * 100
print("Porcentaje de supervivencia por categoría de edad:")
print(supervivencia_edad.round(2))

# %%
plt.figure(figsize=(7, 5))
sns.barplot(x="Sex", y="Survived", data=df)
plt.title("Tasa de supervivencia por sexo")
plt.ylabel("Proporción de sobrevivientes")
plt.xlabel("Sexo")
plt.savefig("../outputs/supervivencia_sexo.png")
plt.show()

# %%
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", hue="Survived", multiple="stack", bins=20)
plt.title("Distribución de edades según supervivencia")
plt.xlabel("Edad")
plt.ylabel("Cantidad de pasajeros")
plt.savefig("../outputs/distribucion_edades.png")
plt.show()

# %%


# %%
plt.figure(figsize=(7, 5))
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Tasa de supervivencia por clase")
plt.ylabel("Proporción de sobrevivientes")
plt.xlabel("Clase")
plt.savefig("../outputs/supervivencia_clase.png")
plt.show()

# %% [markdown]
# ## Conclusion
# 
# El dataset del Titanic contenia (891 pasajeros) 
# 
# 1. **Supervivencia general:** solo el 38.38% de los pasajeros sobrevivió (342 de 891). La mayoría no logró salvarse en el naufragio.
# 
# 2. **El sexo fue el factor más determinante:** las mujeres tuvieron una tasa de supervivencia del 74.20%, casi cuatro veces mayor que la de los hombres (18.89%). ahi podria decir que era porque antes se decia las "mujeres y niños primero" al momento de abordar los botes salvavidas.
# 
# 3. **La clase socioeconómica influyó fuertemente:** los pasajeros de primera clase sobrevivieron en un 62.96%, los de segunda en un 47.28% y los de tercera solo en un 24.24%. 
# 
# 4. **Los niños tuvieron ventaja:** la categoría "Niño" (menores de 12 años) alcanzó un 57.35% de supervivencia, seguida por "Joven" (48.89%), "Adulto" (36.44%) y "Adulto mayor" (26.92%). Esto quiere decir que le daban prioridad a los menores durante la evacuación.
# 
# 5. **Tratamiento de datos faltantes:** la columna `Age` presentaba 177 valores nulos que se rellenaron con la mediana; `Embarked` tenía 2 nulos rellenados con la moda; y `Cabin` fue eliminada al tener 687 nulos (77% de los datos), lo que la volvía poco confiable.
# 
# 6. **Variables creadas:** se generó `FamilySize` y `AgeCategory` para clasificar a los pasajeros en Niño, Joven, Adulto y Adulto mayor.
# 
# Entonces podemos ver que para sobrevivir al hundimiento del Titanic tomaban en cuenta cosas como el sexo, la clase socioeconómica y la edad, en ese orden de importancia.


