import pandas as pd

def get_data():
    df_f = pd.read_csv("ufc_fighters.csv")
    df_c = pd.read_csv("ufc_combats.csv")
    return df_f, df_c
