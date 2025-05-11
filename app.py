import streamlit as st
from update_data import get_data
from utils import predecir_combate

st.title("Predicción de Combates UFC")

with st.spinner("Actualizando base de datos..."):
    df_fighters, df_combats = get_data()

fighter_names = sorted(set(df_fighters['name']))

a = st.selectbox("Luchador A", fighter_names)
b = st.selectbox("Luchador B", fighter_names)
rounds = st.radio("¿Número de asaltos?", [3, 5])
if st.button("Predecir"):
    predecir_combate(a, b, rounds, df_combats)
