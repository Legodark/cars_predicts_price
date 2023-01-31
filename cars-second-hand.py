import joblib
import streamlit as st

from features.funciones import extract_index, modelTransmission, combustibleType, convertidor

st.set_page_config(
    initial_sidebar_state="collapsed"
)

# Cache para cargar el modelo 1 vez.
@st.cache(allow_output_mutation=True)
def load_model():
	  return joblib.load("models/cars_fit_model.pkl")

model_predict = load_model()
models = joblib.load("data/models.pkl")



col_1, col_2 = st.columns([2, 0.3])

with col_1:
    
    st.title('Predice el precio de tu vehículo')

with col_2:
    
    logo = 'images/logo.gif'
    st.image(logo)

st.markdown('##### ***(V.2.1)***')

# Diccionario que almacena las marcas y los modelos
marcas_modelos = {' ': '',
                  'Audi': models[0],
                  'Bmw': models[1],
                  'Ford': models[2],
                  'Hyundai': models[3],
                  'Mercedes': models[4],
                  'Skoda': models[5],
                  'Toyota': models[6],
                  'Vauxhall': models[7],
                  'Volkswagen': models[8]
                  }

# Selector de marca
sl_model = st.selectbox('Marca', marcas_modelos.keys())

# Formulario
if sl_model == ' ':
    st.write('Usa el selector de arriba para seleccionar una marca y que se despliegue el formulario')
else:     
    with st.form(key='model_form'):
        
        st.image(f"images/{sl_model.lower()}.png")
        model = st.selectbox('Modelo', marcas_modelos[sl_model])

        year = st.slider('Año de fabricación', 1980, 2020)
        transmission = st.selectbox('Transmisión', ['Automatica', 'Manual', 'Semi-automatica', 'Other'])
        mileage = st.number_input('Millas', 0, 1000000)
        fuelType = st.selectbox('Combustible', ['Gasolina', 'Diesel', 'Hybrid', 'Other', 'Electric'])
        tax = st.number_input('Tasas', 0, 1000, step=10)
        motor = st.number_input('Millas por Galón', 0.0, 1000.0)
        engine = st.slider('L/motor', 1.0, 20.0)
        divisa = st.selectbox('Divisa', ['€', '$', '£'])

        # Procesamiento del formulario
        if model != '' and motor != 0 and engine != 0:
            if st.form_submit_button('Predecir :car:'):
                car_predict = [[extract_index(model), 
                                year, 
                                modelTransmission(transmission), 
                                mileage, 
                                combustibleType(fuelType),
                                tax, 
                                motor, 
                                engine]]
                
                # Predicción del vehículo
                car_price = model_predict.predict(car_predict)[0].round()
        
                if sl_model == ' ':
                    st.write('Selecciona una marca de coche')
                else:
                    st.markdown(f'### El precio de su :red[{sl_model} {model}] es de :green[{int(convertidor(divisa, car_price))}]:orange[{divisa}]')
        else:
            if st.form_submit_button('Predecir :car:'):
                st.text('Por favor rellene todos los campos')
                
# Configuración de sidebar
                
st.sidebar.image('images/profile_image.png')
st.sidebar.title('Puedes encontrame en:')
st.sidebar.markdown(':computer: [***Mi blog***](https://ozerec.addpotion.com)')
st.sidebar.markdown(':cat: [***Mi Github***](https://github.com/legodark)')
st.sidebar.markdown(':office: [***Mi Linkedin***](https://www.linkedin.com/in/jcs91/)')
