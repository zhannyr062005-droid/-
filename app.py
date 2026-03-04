import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Ұйқысыздық және стресс деңгейін талдау")

# Файлды оқу
try:
    df = pd.read_excel('insomnia_stress_dataset_N150.xlsx')
    st.write("Датасеттің алғашқы жолдары:", df.head())

    # График салу
    st.subheader("Деректердің таралуы")
    fig, ax = plt.subplots()
    df.hist(ax=ax)
    st.pyplot(fig)
except Exception as e:
    st.error(f"Файлды жүктеу мүмкін болмады: {e}")