import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🌙 Ұйқысыздық және стресс деңгейін болжау моделі")

# Деректерді жүктеу
df = pd.read_excel('insomnia_stress_dataset_N150.xlsx')

# Модельді дайындау (мысалы, стресс деңгейін болжау)
# Біз жас, ұйқы сағаты және кофеин қолдану негізінде стрессті болжаймыз
X = df[['age', 'sleep_hours', 'caffeine_use']] 
y = df['stress_level']

model = LinearRegression()
model.fit(X, y)

st.sidebar.header("Мәліметтерді енгізіңіз:")
user_age = st.sidebar.slider("Жасыңыз", 10, 80, 25)
user_sleep = st.sidebar.slider("Ұйқы сағаты (тәулігіне)", 1, 12, 7)
user_caffeine = st.sidebar.slider("Кофеин қолдану (1-10)", 0, 10, 3)

# Болжам жасау
if st.button("Болжам жасау"):
    prediction = model.predict([[user_age, user_sleep, user_caffeine]])
    st.success(f"Сіздің болжамды стресс деңгейіңіз: {prediction[0]:.2f}")
    
    if prediction[0] > 2:
        st.warning("Ескерту: Стресс деңгейі жоғары! Көбірек демалуға тырысыңыз.")
    else:
        st.info("Стресс деңгейі қалыпты.")

st.write("---")
st.subheader("Жаттықтыруға қолданылған деректер:")
st.dataframe(df.head())
