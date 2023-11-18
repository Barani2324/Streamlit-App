import streamlit as st
import pandas as pd

option = st.selectbox('Timing', ('please select your option', 'Early morning ', 'Break fast ', 'Lunch ', 'Evening', 'Dinner'))

if option == "Early morning ":
    recipes = st.selectbox('Recipes', ('please select your option', 'Coffee', 'Tea', 'Ragi malt', 'Milk', 'Green tea',
                                        'Badam milk', 'Black coffee'))
    if recipes == "Coffee":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Coffee Powder(g)', 'Sugar(g)', 'Palm Sugar(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Tea":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Tea powder(g)', 'Sugar(g)', 'Palm Sugar(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Ragi malt":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Malt Powder(g)', 'Sugar(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Milk":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Sugar(g)', "Palm Sugar"])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Green tea":
        input_data = pd.DataFrame(index=[0], columns=['Water(lt)', 'Tea Leaves(n)', 'Sugar(g)', 'Palm Sugar(g)', 'Honey(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Badam milk":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Badam Powder(g)', 'Sugar(g)', 'Palm Sugar'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Black coffee":
        input_data = pd.DataFrame(index=[0], columns=['water(lt)', 'Coffee Powder(g)', 'Sugar(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)

elif option == "Break fast ":
    recipes = st.selectbox('Recipes', ('please select your option', 'Idly or Dosa', 'Pongal', 'Upma  or semiya', 'Poori',
                                        'Kichadi', 'Sambar ', 'Gravy'))
    if recipes == "Idly or Dosa":
        input_data = pd.DataFrame(index=[0], columns=['Rice(kg)', 'Fenugreek(g)', 'Urad dhal(kg)', 'Salt(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Pongal":
        input_data = pd.DataFrame(index=[0], columns=['Rice(kg)', 'Bengal gram dal(kg)', 'Pepper(g)', 'Ginger(g)',
                                                       'Chillies', 'Curry leaves', 'Ghee', 'Cumin seeds',
                                                       'Cashew nut', 'Salt'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Upma  or semiya":
        input_data = pd.DataFrame(index=[0], columns=['Rava or semiya(kg)', 'Onion', 'Urad dhal', 'Bengal gram dhal',
                                                       'Chillies', 'Oil', 'Mustard', 'Curry leaves ', 'Salt'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Poori":
        input_data = pd.DataFrame(index=[0], columns=['Wheat flour', 'Salt(g)', 'Oil', 'Water'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Kichadi":
        input_data = pd.DataFrame(index=[0], columns=['Rava', 'Semiya', 'Onion', 'Urad dhal', 'Bengal gram dhal',
                                                       'Chillies', 'Oil', 'Mustard', 'Curry leaves ', 'Salt', 'Carrot',
                                                       'Beans'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Sambar ":
        input_data = pd.DataFrame(index=[0], columns=['Dhal(kg)', 'Onion', 'Tomato', 'Garlic', 'Curry leaves', 'Oil',
                                                       'Salt', 'Mustard', 'Turmeric powder ', 'Chilli powder'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Gravy":
        input_data = pd.DataFrame(index=[0], columns=['Vegetables (potato,Carrot, beans)', 'Onion', 'Tomato',
                                                       'ginger garlic paste ', 'Turmeric powder', 'Chilli powder', 'Oil',
                                                       'Mustard', 'Curry leaves ', 'Salt'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)

elif option == "Lunch ":
    recipes = st.selectbox('Recipes', ('please select your option', 'Rice', 'Sambar', 'Curd', 'Butter milk', 'Poriyal',
                                        'Rasam ', 'Kaara kolambu', 'Kootu', 'Non veg curry', 'Non veg fry', 'Veg Biryani',
                                        'Raitha'))
    if recipes == "Rice":
        input_data = pd.DataFrame(index=[0], columns=['Rice(kg)', 'Water', 'Salt(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Sambar":
        input_data = pd.DataFrame(index=[0], columns=['Dhal', 'Vegetables', 'Onion', 'Tomato', 'Garlic', 'Curry leaves',
                                                       'Oil', 'Salt', 'Mustard', 'Turmeric powder '])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Curd":
        input_data = pd.DataFrame(index=[0], columns=['Curd ', 'Salt', 'Water'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Butter milk":
        input_data = pd.DataFrame(index=[0], columns=['Curd ', 'Ginger', 'Chillies', 'Water', 'Salt'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Poriyal":
        input_data = pd.DataFrame(index=[0], columns=['Vegetables', 'Curry leaves', 'Onion', 'Oil', 'Chilli powder ',
                                                       'Chillies', 'Mustard', 'Turmeric powder'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Rasam ":
        input_data = pd.DataFrame(index=[0], columns=['Tamarind', 'Tomato', 'Chillies', 'Garlic', 'Water',
                                                       'Cumin and pepper ', 'Salt'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Kaara kolambu":
        input_data = pd.DataFrame(index=[0], columns=['Vegetables', 'Onion', 'Tomato', 'Coriander powder  ',
                                                       'Turmeric powder', 'Chilli powder', 'Oil', 'Mustard',
                                                       'Curry leaves', 'Coconut', 'Salt', 'Water'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Kootu":
        input_data = pd.DataFrame(index=[0], columns=['Vegetables,dhal', 'Onion', 'Curry leaves', 'Oil', 'Salt',
                                                       'Mustard', 'Turmeric powder ', 'Chilli powder'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Non veg curry":
        input_data = pd.DataFrame(index=[0], columns=['Meat', 'Onion', 'Tomato', 'ginger garlic paste ',
                                                       'Turmeric powder', 'Chilli powder', 'Coriander powder ',
                                                       'Spices', 'Coconut', 'Salt', 'Water', 'Curry leaves'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Non veg fry":
        input_data = pd.DataFrame(index=[0], columns=['Meat', 'Onion', 'Tomato', 'Turmeric powder', 'Chilli powder',
                                                       'Spices', 'Salt', 'Water', 'Curry leaves'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Veg Biryani":
        input_data = pd.DataFrame(index=[0], columns=['Vegetable', 'Rice', 'Onion ', 'Tomato', 'Turmeric powder',
                                                       'Chilli powder', 'Salt', 'Coriander powder ',
                                                       'Garlic ginger paste ', 'Chilli powder', 'Water', 'Spices',
                                                       'Coriander leaves'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Raitha":
        input_data = pd.DataFrame(index=[0], columns=['Cucumber', 'Carrot ', 'Onion', 'Salt', 'Chilli'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)

elif option == "Evening":
    recipes = st.selectbox('Recipes', ('please select your option', 'Coffee', 'Tea/ginger tea', 'Ragi malt', 'Milk',
                                        'Badam milk'))
    if recipes == "Coffee":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Coffee Powder(g)', 'Sugar(g)', 'Palm Sugar(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Tea/ginger tea":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Tea powder(g)', 'Sugar(g)', 'Palm Sugar(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Ragi malt":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Malt Powder(g)', 'Sugar(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Milk":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Sugar(g)', "Palm Sugar"])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Badam milk":
        input_data = pd.DataFrame(index=[0], columns=['Milk(lt)', 'Badam Powder(g)', 'Sugar(g)', 'Palm Sugar'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)

elif option == "Dinner":
    recipes = st.selectbox('Recipes', ('please select your option', 'Idly or Dosa', 'Sambar', 'Upma  or semiya'))
    if recipes == "Idly or Dosa":
        input_data = pd.DataFrame(index=[0], columns=['Rice(kg)', 'Fenugreek(g)', 'Urad dhal(kg)', 'Salt(g)'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Upma  or semiya":
        input_data = pd.DataFrame(index=[0], columns=['Rava or semiya(kg)', 'Onion', 'Urad dhal', 'Bengal gram dhal',
                                                       'Chillies', 'Oil', 'Mustard', 'Curry leaves ', 'Salt'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
    elif recipes == "Sambar":
        input_data = pd.DataFrame(index=[0], columns=['Dhal(kg)', 'Onion', 'Tomato', 'Garlic', 'Curry leaves', 'Oil',
                                                       'Salt', 'Mustard', 'Turmeric powder ', 'Chilli powder'])
        input_data = input_data.fillna(0)  # fill with zeros
        edited_data = st.experimental_data_editor(input_data)
