import streamlit as st
from streamlit_option_menu import option_menu

# CSS အမှားမပါအောင် သေချာရေးသားခြင်း
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

# မှန်ကန်သော option_menu Format
selected = option_menu(
    menu_title="Main Menu", 
    options=["တွက်စက်", "အချိုးအစား", "ရွှေဈေး", "အတိုင်းအတာ", "အမရာ (AI)"],
    icons=['calculator', 'percent', 'graph-up', 'rulers', 'robot'],
    menu_icon="cast", 
    default_index=0,
    orientation="horizontal"
)

st.write(f"ရွေးချယ်ထားသော Menu: {selected}")
