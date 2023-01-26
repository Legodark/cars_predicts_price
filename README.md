# Proyecto de Machine Learning - Predicción de precios de coches de 2ª mano

(Detalles del proyecto en proceso)

Versión actual: ***V.2***

## Concepto

Tengo un concesionario multimarca en el cual disponemos de varios vehículos de segunda mano adquiridos recientemente para su venta, para establecer el precio, he decidido usar Machine Learning, el cual, bajo un entrenamiento previo de los precios del mercado de segunda mano, es capaz de decirme cual sería el mejor precio de venta para estas últimas adquisiciones.

El dataset que he utilizado lo puedes encontrar en kaggle:

[![kaggle](https://img.shields.io/badge/UK--CARS-black?style=flat&logo=kaggle&logoColor=#3776AB&labelColor=101010)](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes)

## Tecnologías usadas

[![python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python&logoColor=#3776AB&labelColor=101010)]()[![numpy](https://img.shields.io/badge/numpy-black?style=for-the-badge&logo=numpy&logoColor=#013243&labelColor=101010)]()[![pandas](https://img.shields.io/badge/pandas-black?style=for-the-badge&logo=pandas&logoColor=#150458&labelColor=101010)]()[![scikit](https://img.shields.io/badge/scikit--learn-black?style=for-the-badge&logo=scikit-learn&logoColor=#F7931E&labelColor=101010)]()[![streamlit](https://img.shields.io/badge/streamlit-black?style=for-the-badge&logo=Streamlit&logoColor=#FF4B4B&labelColor=101010)]()[![colab](https://img.shields.io/badge/Colab-black?style=for-the-badge&logo=Google-Colab&logoColor=#F9AB00&labelColor=101010)]()


## Aplicación

Puedes probar la aplicación aquí:

[![streamlit](https://img.shields.io/badge/streamlit-Probar-black?style=flat&logo=Streamlit&logoColor=#FF4B4B&labelColor=101010)](https://legodark-cars-predicts-price-cars-second-hand-mg2aep.streamlit.app)


### 1. Preparación de los datos

Puedes ver la preparación de los datos aquí:

[![colab](https://img.shields.io/badge/Colab-Preparación-black?style=flat&logo=Google-Colab&logoColor=#F9AB00&labelColor=101010)](https://colab.research.google.com/drive/1wTE82oG--Vm25SuQyaUK4schBtaXfma_)

### 2. Desarrollo

En la siguiente imagen se representa el desarrollo para el selector de marca:

![Formulario](images/examples/code_1.png)

En la aplicación se ve así:

![Formulario](images/examples/formulario.png)

La siguiente imagen se puede ver donde monto el array para pasarselo al metodo predic que se vera la siguiente imagen a esta:

![Procesamiento Formulario](images/examples/code_2.png)

La siguiente imagen se puede ver donde hago la predicción y hago que se muestre por pantalla pasando el resultado por la función `convertidor` para sacar el precio con la divisa correcta:

![Predicción](images/examples/code_4.png)

En la siguiente imagen se muestran las funciones para el procesado de los datos del formulario:

![Funciones](images/examples/code.png)

Consta de 4 funciones:

Función `extract_index`:

Esta función se encarga de extraer el indice al que corresponde a un modelo en un diccionario, por ejemplo el modelo A1 tiene el indice 0, esto es importante, puesto que para predecir un vehiculo hay que indicarle a que modelo pertenece y la predición de el valor correcto para dicho modelo.

![Funcion](images/examples/code_6.png)

El proceso de creación del diccionario lo puedes ver aquí: 

[![colab](https://img.shields.io/badge/Colab-Preparación-black?style=flat&logo=Google-Colab&logoColor=#F9AB00&labelColor=101010)](https://colab.research.google.com/drive/1wTE82oG--Vm25SuQyaUK4schBtaXfma_)

Función `modelTransmission`:

Esta función lo que hace es darle un valor numerico a cada tipo de caja de cambios:

![Funcion](images/examples/code_7.png)


Función `combustibleType`:

Aquí hago lo mismo que en la función anterior pero para cada tipo de combustible:

![Funcion](images/examples/code_8.png)

Función `convertidor`:

Esta función lo que hace es convertir el valor obtenido por la predicción en la divisa que el usuario desee:

![Funcion](images/examples/code_9.png)

