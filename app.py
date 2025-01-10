import streamlit as st
import pickle
import numpy as np

# import out model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

# brand
company = st.selectbox("Choose the Brand", df['Company'].unique())

# type of laptop
type = st.selectbox("Choose the type", df['TypeName'].unique())

# RAM
ram = st.selectbox("Choose the Ram in gb", [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight
weight = st.number_input("Choose the weight")

# touch
touchscreen = st.selectbox("Touch Screen", ['No', 'Yes'])

# ips
ips = st.selectbox("IPS", ['No', 'Yes'])

# screen size
screen_size = st.slider('Scrensize in inches', 10.0, 18.0, 13.0)

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',df['CpuBrand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['GpuBrand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    query = query.reshape(1, 12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0])))+ "€ or " + str(1.03*(int(np.exp(pipe.predict(query)[0])))) + "$(US)")