import joblib
import streamlit as st

from features.funciones import extract_index, modelTransmission, combustibleType, convertidor

st.set_page_config(
    initial_sidebar_state="collapsed"
)

# Cache para cargar el modelo 1 vez.
@st.cache(allow_output_mutation=True)
def load_model():
	  return joblib.load("src/models/cars_fit_model.pkl")

model_predict = load_model()
models = joblib.load("src/data/models.pkl")



col_1, col_2 = st.columns([2, 0.3])

with col_1:
    
    st.title('Predice el precio de tu vehículo')

with col_2:
    
    logo = 'src/images/fiat500.png'
    st.image(logo)

st.markdown('##### ***(V.1.3)***')

# Variables donde se almacenan los datos para los menus
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

sl_model = st.selectbox('Marca', [' ','Audi', 'BMW', 'Ford', 'Hyundai', 'Mercedes', 'Skoda', 'Toyota', 'Vauxhall',
                                  'Volkswagen'])

# Formulario
if sl_model == ' ':
    st.write('Usa el selector de arriba para seleccionar una marca y que se despliegue el formulario')
else:     
    with st.form(key='model_form'):
        
        if sl_model == 'Audi':
            st.image('src/images/audi.png')
            model = st.selectbox('Modelo', audi)
        if sl_model == 'BMW':
            st.image('src/images/bmw.png')
            model = st.selectbox('Modelo', bmw)
        if sl_model == 'Ford':
            st.image('src/images/ford.png')
            model = st.selectbox('Modelo', ford)
        if sl_model == 'Hyundai':
            st.image('src/images/hyundai.png')
            model = st.selectbox('Modelo', hyundai)
        if sl_model == 'Mercedes':
            st.image('src/images/mercedesbenz.png')
            model = st.selectbox('Modelo', mercedes)
        if sl_model == 'Skoda':
            st.image('src/images/skoda.png')
            model = st.selectbox('Modelo', skoda)
        if sl_model == 'Toyota':
            st.image('src/images/toyota.png')
            model = st.selectbox('Modelo', toyota)
        if sl_model == 'Vauxhall':
            st.image('src/images/vauxhall.png')
            model = st.selectbox('Modelo', vauxhall)
        if sl_model == 'Volkswagen':
            st.image('src/images/volkswagen.png')
            model = st.selectbox('Modelo', vw)

        year = st.slider('Año de fabricación', 1980, 2020)
        transmission = st.selectbox('Transmisión', ['Automatica', 'Manual', 'Semi-automatica', 'Other'])
        mileage = st.number_input('Millas', 0, 1000000)
        fuelType = st.selectbox('Combustible', ['Gasolina', 'Diesel', 'Hybrid', 'Other', 'Electric'])
        tax = st.number_input('Tasas', 0, 1000, step=10)
        motor = st.number_input('Millas por Galón', 0.0, 1000.0)
        engine = st.slider('L/motor', 1.0, 20.0)
        divisa = st.selectbox('Divisa', ['€', '$', '£'])

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
                
                car_price = model_predict.predict(car_predict)[0].round()
        
                if sl_model == ' ':
                    st.write('Selecciona una marca de coche')
                else:
                    st.markdown(f'### El precio de su :red[{sl_model} {model}] es de :green[{int(convertidor(divisa, car_price))}]:orange[{divisa}]')
        else:
            if st.form_submit_button('Predecir :car:'):
                st.text('Por favor rellene todos los campos')
                
# Configuración de sidebar
                
st.sidebar.image('src/images/profile_image.png')
st.sidebar.title('Puedes encontrame en:')
st.sidebar.markdown(':computer: [***Mi blog***](https://ozerec.addpotion.com)')
st.sidebar.markdown(':cat: [***Mi Github***](https://github.com/legodark)')
st.sidebar.markdown(':office: [***Mi Linkedin***](https://www.linkedin.com/in/jcs91/)')
