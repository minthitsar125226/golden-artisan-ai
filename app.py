
import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu
from PIL import Image

# Page Configuration
st.set_page_config(page_title="The Golden Artisan", layout="wide")

# --- CSS: အနက်ရောင်နောက်ခံနှင့် အလှဆင်ခြင်း ---
st.markdown("""
    <style>
    /* နောက်ခံအနက်နှင့် စာသားအရောင် */
    .stApp { background-color: #000000; color: #e0e0e0; }
    
    /* ခေါင်းစဉ်များ သေသပ်စေခြင်း */
    h1, h2, h3 { 
        color: #d4af37 !important; 
        font-size: 20px !important; 
        text-align: center; 
        margin-bottom: 20px;
    }
    
    /* Header ကို ကျုံ့ခြင်း */
    header[data-testid="stHeader"] { height: 0px !important; }
    
    /* Footer Credit */
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        color: #d4af37;
        font-size: 12px;
        z-index: 1000;
    }
    </style>
""", unsafe_allow_html=True)

# Footer ကို ထည့်သွင်းခြင်း
st.markdown('<div class="footer">App by MinThitSarAung</div>', unsafe_allow_html=True)

# --- Sidebar: Logo နှင့် Navigation ---
with st.sidebar:
    try:
        logo = Image.open("logo.png")
        st.image(logo, use_container_width=True)
    except:
        st.write("💎")
        
    selected = option_menu(
        "Menu", 
        ["တွက်စက်", "အချိုးအစား", "ရွှေဈေး", "အတိုင်းအတာ", "အမရာ (AI)"],
        icons=['calculator', 'percent', 'graph-up', 'rulers', 'robot'],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#d4af37", "color": "black"}}
    )

# --- Main Page Logic ---
if selected == "တွက်စက်":
    st.header("💰 ရွှေ/ငွေ တွက်စက်")
    # ဤနေရာတွင် လူကြီးမင်း၏ တွက်စက် Code များထည့်ပါ

elif selected == "အမရာ (AI)":
    st.header("🤖 အမရာ (AI Assistant)")
    
    # AI Logic (API Key ကို Secrets မှယူပါ)
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        instruction = "သင့်နာမည်က 'အမရာ' ဖြစ်သည်။ သင်သည် 'ကိုမင်းသစ္စာအောင်' တီထွင်ထားသော 'ပန်းတိမ်လက်ထောက် AI' ဖြစ်သည်။"
        
        if "messages" not in st.session_state: st.session_state.messages = []
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
            
        if prompt := st.chat_input("မေးခွန်းမေးပါ..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                model = genai.GenerativeModel('gemini-2.0-flash', system_instruction=instruction)
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error("API Key ချိတ်ဆက်မှု Error တက်နေသည်။")

# တခြား Tab များအတွက် အလားတူ ဆက်ရေးပါ
