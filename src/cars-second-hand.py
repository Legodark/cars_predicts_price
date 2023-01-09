import streamlit as st
import joblib

from data.funciones import extract_index, modelTransmission, combustibleType 

models = joblib.load("data/models.pkl")
model_predict = joblib.load("models/cars_fit_model.pkl")

st.title('(V.0.2)Predice el precio de tu vehículo:')

audi = models[0]
bmw = models[1]
ford = models[2]
hyundai = models[3]
mercedes = models[4]
skoda = models[5]
toyota = models[6]
vauxhall = models[7]
vw = models[8]

st.text('Selecciona la marca de tu vehículo:')
sl_model = st.selectbox('Marca', ['Audi', 'BMW', 'Ford', 'Hyundai', 'Mercedes', 'Skoda', 'Toyota', 'Vauxhall',
                                  'Volkswagen'])
with st.form(key='model_form'):

    if sl_model == 'Audi':
        model = st.selectbox('Modelo', audi)
    if sl_model == 'BMW':
        model = st.selectbox('Modelo', bmw)
    if sl_model == 'Ford':
        model = st.selectbox('Modelo', ford)
    if sl_model == 'Hyundai':
        model = st.selectbox('Modelo', hyundai)
    if sl_model == 'Mercedes':
        model = st.selectbox('Modelo', mercedes)
    if sl_model == 'Skoda':
        model = st.selectbox('Modelo', skoda)
    if sl_model == 'Toyota':
        model = st.selectbox('Modelo', toyota)
    if sl_model == 'Vauxhall':
        model = st.selectbox('Modelo', vauxhall)
    if sl_model == 'Volkswagen':
        model = st.selectbox('Modelo', vw)

    year = st.slider('Año de fabricación', 1980, 2020)
    transmission = st.selectbox('Transmisión', ['Automatica', 'Manual', 'Semi-automatica', 'Other'])
    mileage = st.number_input('Millas', 0, 1000000)
    fuelType = st.selectbox('Combustible', ['Gasolina', 'Diesel', 'Hybrid', 'Other', 'Electric'])
    tax = st.number_input('Tasas', 0, 1000, step=10)
    motor = st.number_input('Miles per gallon', 0, 1000)
    engine = st.slider('L/motor', 1, 7)

    if model != '' and motor != '' and engine != '':
        result = st.form_submit_button('Enviar')
    else:
        st.text('Por favor rellena los datos.')
        st.form_submit_button('Enviar')

car_predict = [[extract_index(model), year, modelTransmission(transmission), mileage, combustibleType(fuelType),
                tax, motor, engine]]

st.write('El precio del', sl_model, model, 'es de', model_predict.predict(car_predict)[0].round(), '£')

