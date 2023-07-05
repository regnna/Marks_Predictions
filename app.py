import streamlit as st
import pandas as pd
import numpy as np
import pickle

filename='student_mark_predicor_model.pkl'
model = pickle.load(open(filename,'rb'))
st.set_page_config(
    page_title="Student Marks Evolution",
    layout="centered",
    initial_sidebar_state="collapsed",
    # page_icon="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/",
    page_icon="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f004.svg",
    menu_items={
        'Get Help': 'https://github.com/regnna',
        'Report a bug': 'https://github.com/regnna',
        'About': 'Regnna'
    }

)


def add_bg():
    st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://images.unsplash.com/photo-1688232542797-c3e762c7e3c3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1932&q=80");
                background-attachment: fixed;
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

add_bg()

hide_st_style="""
                <style>
                #MainMenu {visibility:hidden;}
                footer{visibility:hidden;}
                </style>
                """
st.markdown(hide_st_style,unsafe_allow_html=True)
# st.set_page_config(page_title='Student marks')
st.markdown("<h1 style='text-align: center; color: white;'> Student MARKS Predictions </h1>", unsafe_allow_html=True)




#Hours they study
Hours =st.slider('Enter Hours the Student studies',0,24)
hours=int(Hours)



if st.button('Predict Marks'):
    #Call the ML Model
    predict=model.predict([[hours]])[0][0]
    my_prediction = int(round(predict))
    if my_prediction>=95:
        my_prediction=94
    #Display the predicted Score Range
    x=f'Predicted marks the student will obtain : {my_prediction-5} to {my_prediction+5}' 
    # st.success("<h1 style='text-align: center; color: white;'> Student MARKS Predictions </h1>")
    st.success(x)