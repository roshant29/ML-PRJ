%%writefile app.py
import streamlit as st
import joblib
model = joblib.load('spam-ham')
st.title('SPAM-HAM CLASSIFIER')#creates a title with naem spam_ham classifier
ip = st.text_input('Enter the message')#creates a text box
op = model.predict([ip])
if st.button('Predict'):
   st.title(op[0])
