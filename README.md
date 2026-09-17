# Análisis exploratorio del Titanic

Proyecto de análisis exploratorio de datos sobre los pasajeros del Titanic

## Dataset

- **Nombre:** Titanic - Machine Learning from Disaster
- **Fuente:** [Kaggle](https://www.kaggle.com/c/titanic/data)
- **Descripción:** Información de 891 pasajeros del Titanic (edad, sexo, clase, tarifa, si sobrevivió, etc.). Para esta práctica se utiliza únicamente el archivo `train.csv`.

## Objetivo

Analizar la información disponible de los pasajeros del Titanic para identificar características asociadas con la supervivencia. Se realizo la limpieza, preprocesamiento, análisis exploratorio y visualización.

## Requisitos

- Python 3.10 o superior
- Las dependencias listadas en `requirements.txt`

## Instalación

Clonar el repositorio:
git clone https://github.com/TU_USUARIO/titanic-analisis.git

Entrar al proyecto:
cd titanic-analisis


Crear un entorno virtual:
python -m venv .venv

Activarlo:
**Windows (PowerShell):**
.venv\Scripts\activate

**macOS/Linux:**
source .venv/bin/activate


Instalar las dependencias:
pip install -r requirements.txt

## Ejecución

Desde la raíz del proyecto:
python src/analysis.py


También se puede abrir el notebook `src/analysis.ipynb` en Jupyter o VS Code y ejecutar celda por celda.

## Análisis realizados

1. Porcentaje general de supervivencia
2. Supervivencia según el sexo
3. Supervivencia según la clase del pasajero
4. Supervivencia según la categoría de edad (Niño, Joven, Adulto, Adulto mayor)

Además se crearon dos variables nuevas:
- `FamilySize`: número total de familiares a bordo + 1
- `AgeCategory`: categoría de edad del pasajero

## Resultados y conclusiones

- Solo el **38.38%** de los pasajeros sobrevivió.
- Las **mujeres** tuvieron una tasa de supervivencia mucho más alta (**74.20%**) que los hombres (**18.89%**).
- Los pasajeros de **primera clase** sobrevivieron en un **62.96%**, frente al **24.24%** de tercera clase.
- Los **niños** (menores de 12 años) presentaron la tasa de supervivencia más alta entre categorías de edad (**57.35%**).
- Los factores más determinantes para sobrevivir fueron: **sexo, clase socioeconómica y edad**, en ese orden.

## Estructura del proyecto

titanic-analisis/
├── data/
│ └── train.csv
├── src/
│ ├── analysis.py
│ └── analysis.ipynb
├── outputs/
│ ├── supervivencia_sexo.png
│ ├── supervivencia_clase.png
│ └── distribucion_edades.png
├── README.md
├── requirements.txt
└── .gitignore


## Autor


Yuliana Elizabeth Banda del Ángel