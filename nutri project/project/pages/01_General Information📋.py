import streamlit as st
import datetime


name = st.text_input("Please enter your name :smile: : ")
if name:
    st.write("Welcome to Nutritional Counseling ", name ,":heart_eyes:")
    st.snow()
Dateofbirth = st.text_input("Date of birth: ")

MailID = st.text_input("Mail ID: ")
age = st.number_input('Age (years):', min_value=1, max_value=150, step=1)
gender = st.selectbox('Gender:', ['Select Your Option','male', 'female' , 'transgender'])
Occupation = st.text_input("Occupation: ")
City = st.text_input("City:")
State = st.text_input("state:")
location = st.selectbox('Location:', ['Select Your Option','Urban', 'Rural' , 'Semi Urban'])
country = st.text_input("Country:")
TOW = st.selectbox('Select your Type of Work:', ['Select Your Option','Sedentary', 'Heavy' , 'Moderate'])
smoking = st.selectbox('Smoking Habits:', ['Select Your Option','Yes', 'No'])
Dis = st.selectbox('Any Diseases:', ['Select Your Option','Yes', 'No'])
Alcohol = st.selectbox('Alcohol Habits:', ['Select Your Option','Yes', 'No'])
Edu = st.selectbox('Educational Status:', ['Select Your Option','Literate', 'Illiterate'])
ex = st.selectbox('Exercise:', ['Select Your Option','Yes', 'No'])
Yoga = st.selectbox('Yoga:', ['Select Your Option','Yes', 'No'])
WT = st.text_input("Morning Wake-Up Time:")
NT = st.selectbox('Night time:', ['Select Your Option','Below 8hrs', '8hrs' , 'Above 8hrs'])
FoodAl = st.selectbox('Food Allergies:', ['Select Your Option','Yes', 'No'])
MType = st.selectbox('Meal Type:', ['Select Your Option','Veg', 'Non-Veg'])
PT = st.selectbox('Pattern of Eating:', ['Select Your Option','Slow', 'Moderate' , 'Quick'])
WC = st.text_input("Water Consumption Level (approx)")





