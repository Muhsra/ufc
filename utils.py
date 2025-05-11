import streamlit as st
import joblib
import pandas as pd

model_win = joblib.load("model_win.pkl")
model_method = joblib.load("model_method.pkl")
model_rounds = joblib.load("model_rounds.pkl")

def predecir_combate(name_a, name_b, rounds, df):
    comb = df[(df["fighter_A"] == name_a) & (df["fighter_B"] == name_b) & (df["rounds"] == rounds)]
    if comb.empty:
        st.error("Combate no encontrado en el histórico")
        return
    row = comb.iloc[0]
    X = row[['height_diff','reach_diff','sig_strikes_A','sig_strikes_B','takedowns_A','takedowns_B','control_time_A','control_time_B']].values.reshape(1, -1)
    st.success(f"Ganador probable: {'Luchador A' if model_win.predict(X)[0] == 'A' else 'Luchador B'}")
    st.info(f"Método probable: {model_method.predict(X)[0]}")
    st.info(f"Asaltos estimados: {model_rounds.predict(X)[0]}")
