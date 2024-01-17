![Portada](portada_larga.png)
# Proyecto Individual 2 -Siniestros Viales en CABA 

## Introducción

¡Bienvenido al proyecto de análisis de datos sobre siniestros viales en la Ciudad de Buenos Aires! En este proyecto, asumiremos el rol de un Data Analyst, colaborando con el Observatorio de Movilidad y Seguridad Vial (OMSV) bajo la órbita de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires.

La tarea es crucial: analizar un conjunto de datos sobre siniestros viales ocurridos entre 2016 y 2021 con el objetivo de proporcionar información valiosa que permita a las autoridades locales tomar medidas efectivas para reducir la cantidad de víctimas fatales en estos incidentes.

## Contexto

Los siniestros viales, eventos que involucran vehículos en las vías públicas, son una preocupación significativa en una ciudad tan dinámica como Buenos Aires. La alta densidad de tráfico y población aumenta la probabilidad de estos incidentes, que van desde colisiones entre vehículos hasta atropellos y caídas de vehículos. Los impactos abarcan desde daños materiales hasta lesiones graves o incluso fatales para los involucrados, afectando la seguridad de residentes y visitantes, así como la infraestructura vial y los servicios de emergencia.

En Argentina, los siniestros viales representan una causa importante de muertes violentas, con aproximadamente 4,000 personas perdiendo la vida anualmente en estos eventos. Las estadísticas del Sistema Nacional de Información Criminal revelan que entre 2018 y 2022, se registraron 19,630 muertes por siniestros viales en todo el país, equivalente a 11 personas por día.

El OMSV te ha proporcionado un conjunto de datos en formato xlsx que detalla los siniestros viales con resultado de homicidio ocurridos en la Ciudad de Buenos Aires durante el periodo mencionado. La tarea es analizar este conjunto de datos para extraer información clave que respalde la toma de decisiones de las autoridades locales. 

## Desarrollo

### Datos

Para este proyecto se trabajó con la __Bases de Víctimas Fatales en Siniestros Viales__ que se encuentra en formato de Excel y contiene dos pestañas de datos:

- HECHOS: que contiene una fila de hecho con id único y las variables temporales, espaciales y participantes asociadas al mismo.

- VICTIMAS: contiene una fila por cada víctima de los hechos y las variables edad, sexo y modo de desplazamiento asociadas a cada víctima. Se vincula a los HECHOS mediante el id del hecho. En este documento se detallan todas las definiciones manejadas en los datos y en el desarrollo de este proyecto. Por otra parte, en este link se encuentran los datos utilizados en el análisis.

__Proceso de ETL (Extracción, limpieza y carga de datos):__

Se realiza la extraccíon y limpieza de los datos de los dos dataset *HECHOS y VICTIMAS*, a tráves de la utilización de Pandas y Jupyter Netbook.ETL Eliminando nulos, duplicados, con transformaciones necesarias como cambio en los tipos de datos, eliminación de columnas y unión de las tablas en un archivo [ETL](ETL.ipynb), [siniestros_limpio.csv](siniestos_limpio.csv)


__Proceso de EDA (Análisis Exploratorio de los datos):__

Una vez que los datos están limpios, es momento de revisar las relaciones que existen entre las variables numéricas y categóricas de los datasets, encontrar si hay presencia de outliers o anomalías (que no tienen que ser errores necesariamente), y se verificó si hay algún patrón o conocimiento que sirva en un análisis posterior. [EDA](EDA.ipynb)

### Análisis de los datos 

- Se analizan las variables numéricas del dataset su correlación por medio de una matriz, donde se encuentra una relación positiva entre las variables *Edad y Hora*
- La mayoria de los siniestros resultan con una víctima fatal, rara vez involucran 3 víctimas.

__- Análisis Temporal:__

En el transcurso de los años, los accidentes con víctimas fatales muestran: para el período 2016-2018 una tendencia alta y estacionaria, que luego se convierte en bajista (teniendo en cuenta el comienzo de la Pandemia por COVID19 durante 2020); puede verse un pico de siniestros durante Diciembre de 2021 y se retoma la tendencia bajista. Los meses con más victimas fatales son Diciembre (86) y Agosto(71); mientras que los días de la semana Sábado (114) y Domingo (114) tienen la mayor cantidad de víctimas.

Los horarios críticos de los siniestros viales están relacionados con los momentos del ingreso a la jornada laboral (5-9h), el momento del almuerzo (12-14h) y la salida del trabajo (17-18h). Mientras que los fines de semana están relacionados con las salidas nocturnas (4-7h)


__Análisis Demográfico y Geográfico:__

Edad de las víctimas : La distribución del rango etario de víctimas, resulta para los *Masculinos* entre 20 y 40 años; mientras que para los *Femeninos* entre 40, 60 y 80 años.

El patrón de correlación Edad y Hora de las variables númericas se analiza agregando la variable Sexo, de lo que resulta la conclusión que los horarios en que los accidentes son protagonizados por Masculinos es al horario de ingreso y egreso laboral, mientras que para los Femeninos es en el horario cercano al almuerzo.

Utilizando la herramienta GeoPandas y extrayendo los datos de los detalles de los Barrios que conforman las 15 comunas de CABA; resulta el análisis de las coordenadas geográficas y comunas de CABA, que demostro que las comunas con __más siniestos son las 1, 4 , 9, 8 y 7.__


Los siniestros se producen en 62% de los casos en el tipo de calle Avenida y en el 82% de los casos se corresponden con un Cruce entre calles. Lo que resulta un patrón que se repite a lo largo de los años.

__- Análisis Participativo:__

Para el caso de la variable Participantes de los sinietros; se analiza a Acusados, como el vehículo que tiene la responsabilidad del hecho, de lo que resultan los Autos, Colectivos y Vehículos de Carga como mayores involucrados. Para el análisis de las Victimas, que en momento del accidente resultaban mayormente en el Rol de Conductor o Peatón; y el siniestro se produce en la mayoría de los casos en Motos y luego como Peaton.

## Indicadores de Rendimiento Clave KPI

Una vez finalizado el Análisis Exploratorio, se utiliza el dataset resultante Siniestros y los extraidos de la página oficial de CABA con los datos de las [comunas](comunas.xlsx) ; para trabajar en la herramienta PowerBi a fin de obtener los KPI (Indicadores de Rendimiento Clave) y un dashboard de presentación del informe y Visualización de datos.

__KPI Propuestos__

__- Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior__

Se define la tasa de homicidios en siniestros viales como el número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico. Su fórmula es: (Número de homicidios en siniestros viales / Población total) * 100,000

Número de Homicidios de Siniestros = Tomando la variable Num víctimas del dataset Población Total = Tomada del Censo 2022. (Fuente:INDEC)

__- Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior__

Se define la cantidad de accidentes mortales de motociclistas en siniestros viales como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado periodo temporal. Su fórmula para medir la evolución de los accidentes mortales con víctimas en moto es: (Número de accidentes mortales con víctimas en moto en el año anterior - Número de accidentes mortales con víctimas en moto en el año actual) / (Número de accidentes mortales con víctimas en moto en el año anterior) * 100

Cantidad de Accidentes Mortales en Moto = Tomando la variable Victima que se iguale a el campo [MOTO] del dataset

__- Reducir en un 15% la cantidad de accidentes con víctimas fatales de peatones en el último semestre, en CABA, respecto al semestre anterior.__

Se define la cantidad de accidentes fatales de peatones en siniestros viales como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que circulaban a pie en un determinado periodo temporal. Su fórmula para medir la evolución de los accidentes mortales con víctimas peaton es: (Número de accidentes mortales con víctimas peaton en el semestre anterior - Número de accidentes mortales con víctimas peaton en el semestre actual) / (Número de accidentes mortales con víctimas peaton en el semestre anterior) * 100

Cantidad de Accidentes Mortales en Moto = Tomando la variable Victima que se iguale a el campo [PEATON] del dataset.

## Conclusiones

A partir del análisis exahustivo de los datos y su posterior visualización a través del dashboard en PowerBi; se concluye que las víctimas fatales por siniestros de tránsito entre los años 2016 a 2021 fueron 717 personas. Que la franja horaria de mayor problemática es la del ingreso laboral (5-9h), la del almuerzo (12-14h)y la del regreso a casa(17-18h); aunque durante los fines de semana (Sábado y Domingo), los accidentes se manifiestan en los horarios de salidas nocturnas (3-7h). Las víctimas son en un 76% Masculinas, y sus edades entre el rango etario de 20-40 años. Además en los siniestros de Masculinos los mayores casos se dan en su rol como Conductor. Los tipos de vehículos más frecuentes con Víctimas son las Motos y luego los Peatones; mientras que para los Acusados los vehículos más frecuentes son Autos, Colectivos y cargas. En cuanto a el lugar donde se producen los siniestros, las Avenidas a lo largo de los años han sido los espacios de mayor cantidad de siniestros; y en Cruce mayor a las calles. Se observo un patrón en relación con la variable Edad, Hora y Sexo. Donde los Masculinos de entre 20 a 40 años y en los horarios de entrada y salida laboral o para el caso de los fines de semana en horas de salidas nocturnas.

Asi se concluye que deberían mejorarse las señales y controles en las Avenidas sobre todo en las comunas 1 y 4 de CABA. Que podrían generarse campañas de prevención dirigidas a los Masculinos de entre 20 y 40 años .

## Estructura del Repositorio

1. /Archivos_note: - Esta carpeta contiene los Jupyter Notebooks (.ipynb) con el código completo y bien comentado.

- ETL: Este libro contiene todo el paso a paso de las Extracciones, Transformaciones y Cargas de datos. Pre-procesado y Calidad del Dato.
- EDA: En éste archivo encontrarás todo el proceso de Analítica Predictiva y Prescriptiva de las diferentes variables de nuestro conjunto de datos.
- functions: De este libro generé una copia .py para que fuese ejecutable. Acá encontrarás una serie de funciones que regularmente usaba desde el ETL ó el EDA entonces lo convertí en un código reutilizable.

2. /Dataset - Almacena los datasets fuentes y los resultantes despues del ETL y EDA, en una versión limpia y procesada.
- homicidios y lesiones: Archivo en formato xlsx. Son nuestra fuente de datos original.
- siniestos_limpio: Es el archivos resultantes de la limpieza del ETL, en formato csv.
- comunas: Archivo en formato csv donde se integran todos los datos de las comunas con sus nombres.

3. /comunas: - Carpetas de los ejecutables para poder utilizar geopandas.

4. /imagenes: - Imagenes que se utilizaron para desarrollar el proyecto.

## Autor

__Barrionuevo, Gabriela Soledad.__




