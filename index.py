import streamlit as st
import joblib
import pandas as pd

st.title('Titanic Dataset')
st.write('Using Logistic Regression')


passenger_id = st.number_input('PassengerId')
pclass = st.number_input('Pclass')
age = st.number_input('Age')
fare = st.number_input('Fare')
family_size = st.number_input('FamilySize')
gender_class_female = st.number_input('GenderClass_female')
gender_class_male = st.number_input('GenderClass_male')
embarked_q = st.number_input('Embarked_Q')
embarked_s = st.number_input('Embarked_S')
print(passenger_id)

if st.button('Predict'):
    # Create a DataFrame with named columns
    logisticreg = joblib.load('dumped_model.joblib','r')

    input_data = pd.DataFrame({
        'PassengerId': [passenger_id],
        'Pclass': [pclass],
        'Age': [age],
        'Fare': [fare],
        'FamilySize': [family_size],
        'GenderClass_female': [gender_class_female],
        'GenderClass_male': [gender_class_male],
        'Embarked_Q': [embarked_q],
        'Embarked_S': [embarked_s]
    })

    # prediction = logisticreg.predict(input_data)
    st.write('0')
