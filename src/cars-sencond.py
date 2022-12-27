import streamlit as st
import numpy as np
import pandas as pd
import joblib


dic_cars = joblib.load('./data/diccionario_coches.pkl')
models = joblib.load('./data/models.pkl')

audi = models[0]
bmw = models[1]
ford = models[2]
hyundai = models[3]
mercedes = models[4]
skoda = models[5]
toyota = models[6]
vauxhall = models[7]
vw = models[8]

print(audi)

sl_model = st.selectbox('Marca', ['Audi', 'BMW', 'Ford', 'Hyundai', 'Mercedes', 'Skoda', 'Toyota', 'Vauxhall', 'volkswagen'])

with st.form(key='my_form'):
    if sl_model == 'Audi':
        model = st.selectbox('Modelo', audi)



coche_prueba = model

for index, coche in dic_cars.items():
  if coche == coche_prueba:
    print(index)

# with st.form(key='my_form'):
#     model = st.selectbox('Modelo', ['Class A', 'Class C', 'Class E'])
#     year = st.slider('Año de fabricación', 2015, 2020)
#     transmission = st.selectbox('Transmisión', ['Automatica', 'Manual', 'Semi-automatica'])
#     mileage = st.number_input('Millas', 0, 1000000)
#     fuelType = st.selectbox('Combustible', ['Gasolina', 'Diesel', 'Hybrid', 'Other'])
#     tax = st.number_input('Tasas', 0, 1000, step=10)
#     motor = st.slider('L/consumo', 4, 20)
#     engine = st.slider('L/motor', 1, 7)

#     if model != '' and motor != '' and engine != '':
#         result = st.form_submit_button('Enviar')
#     else:
#         st.text('Por favor rellena los datos.')
#         st.form_submit_button('Enviar')

