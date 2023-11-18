import streamlit as st
one = st.selectbox('Have you experienced a loss of appetite?:', ['Select Your Option','Yes', 'No'])
two = st.selectbox('Do you eat fruits and vegetables daily?:', ['Select Your Option','Yes', 'No'])
thre = st.selectbox('Do you eat on a typical day?:', ['Select Your Option','Yes', 'No'])
lb1 = st.selectbox('Have you maintained the same weight or not? :', ['Select Your Option','Gain', 'Loss'])
lb2 = st.selectbox('How do you feel about your current weight?', ['Select Your Option','very bad', 'bad' , 'good', 'very good'])
lb3 = st.selectbox('Do you prepare your meals at home?:', ['Select Your Option','Yes', 'No'])
lb4 = st.selectbox('How many meals do you eat?', ['Select Your Option','3meal', '5meal', '8meal'])
vb5 = st.text_input("Breakfast timing:")
vb6 = st.text_input("Lunch timing:")
vb7 = st.text_input("Dinner timing:")
lb8 = st.selectbox('How often do you eat out?', ['Select Your Option','Daily', 'twice in a week', 'trice in a week'])

