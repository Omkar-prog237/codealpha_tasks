import streamlit as st 
import numpy as np
import pickle

with open("CodeAlpha_Iris-Flower-Classification.pkl",'rb') as f:
    model = pickle.load(f)
    
st.title("🌸 Iris Flower Prediction")
sepal_length = st.slider('Sepal length', 4.0, 8.0)
sepal_width = st.slider('Sepal width', 2.0, 5.0)
petal_length = st.slider('Petal length', 1.0, 7.0)
petal_width = st.slider('Petal width', 0.1, 2.5)

if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    Species = ['Iris-Sentosa' , 'Iris-Versicolour', 'Iris-Virginica']
    st.success(f"The predicted species is: {Species[prediction[0]]}")