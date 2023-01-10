import joblib
import streamlit as st

from features.funciones import extract_index, modelTransmission, combustibleType 

model_predict = joblib.load("src/models/cars_fit_model.pkl")
models = joblib.load("src/data/models.pkl")

st.markdown('# Predice el precio de tu vehículo')
st.markdown('##### ***(V.1.0)***')

audi = models[0]
bmw = models[1]
ford = models[2]
hyundai = models[3]
mercedes = models[4]
skoda = models[5]
toyota = models[6]
vauxhall = models[7]
vw = models[8]

model = ' '

st.markdown('### Selecciona la marca de tu vehículo:')
sl_model = st.selectbox('Marca', [' ','Audi', 'BMW', 'Ford', 'Hyundai', 'Mercedes', 'Skoda', 'Toyota', 'Vauxhall',
                                  'Volkswagen'])

if sl_model == ' ':
    st.write('Usa el selector de arriba para seleccionar una marca y que se despliegue el formulario')
else:     
    with st.form(key='model_form'):
        
        if sl_model == 'Audi':
            st.image('images/audi.png')
            model = st.selectbox('Modelo', audi)
        if sl_model == 'BMW':
            st.image('images/bmw.png')
            model = st.selectbox('Modelo', bmw)
        if sl_model == 'Ford':
            st.image('images/ford.png')
            model = st.selectbox('Modelo', ford)
        if sl_model == 'Hyundai':
            st.image('images/hyundai.png')
            model = st.selectbox('Modelo', hyundai)
        if sl_model == 'Mercedes':
            st.image('images/mercedesbenz.png')
            model = st.selectbox('Modelo', mercedes)
        if sl_model == 'Skoda':
            st.image('images/skoda.png')
            model = st.selectbox('Modelo', skoda)
        if sl_model == 'Toyota':
            st.image('images/toyota.png')
            model = st.selectbox('Modelo', toyota)
        if sl_model == 'Vauxhall':
            st.image('images/vauxhall.png')
            model = st.selectbox('Modelo', vauxhall)
        if sl_model == 'Volkswagen':
            st.image('images/volkswagen.png')
            model = st.selectbox('Modelo', vw)

        year = st.slider('Año de fabricación', 1980, 2020)
        transmission = st.selectbox('Transmisión', ['Automatica', 'Manual', 'Semi-automatica', 'Other'])
        mileage = st.number_input('Millas', 0, 1000000)
        fuelType = st.selectbox('Combustible', ['Gasolina', 'Diesel', 'Hybrid', 'Other', 'Electric'])
        tax = st.number_input('Tasas', 0, 1000, step=10)
        motor = st.number_input('Millas por Galón', 0.0, 1000.0)
        engine = st.slider('L/motor', 1.0, 20.0)

        if model != '' and motor != 0 and engine != 0:
            if st.form_submit_button('Enviar'):
                car_predict = [[extract_index(model), 
                                year, 
                                modelTransmission(transmission), 
                                mileage, 
                                combustibleType(fuelType),
                                tax, 
                                motor, 
                                engine]]
        
                if sl_model == ' ':
                    st.write('Selecciona una marca de coche')
                else:
                    st.write('El precio del', sl_model, model, 'es de', model_predict.predict(car_predict)[0].round(), '£')
        else:
            if st.form_submit_button('Enviar'):
                st.text('Por favor rellene todos los campos')
            
    

    
