import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu # လိုအပ်ပါက pip install streamlit-option-menu လုပ်ပါ

# Page Config
st.set_page_config(page_title="The Golden Artisan", layout="wide")

# --- CUSTOM CSS: Logo အရောင်နှင့် တစ်သားတည်းကျစေရန် ---
st.markdown("""
    <style>
    .stApp {
        background-color: #d5d8d4; 
    }
    h1, h2, h3 { color: #b8860b !important; }
    .stSidebar { background-color: #c4c7c3; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar: Logo နှင့် Navigation ---
with st.sidebar:
    st.image("logo.png", use_container_width=True)
    selected = option_menu(
        "Menu", 
        ["တွက်စက်", "အချိုးအစား", "ရွှေဈေး", "အတိုင်းအတာ", "အမရာ (AI)"],
        icons=['calculator', 'percent', 'graph-up', 'rulers', 'robot'],
        menu_icon="cast", default_index=0
    )

# --- Main Logic ---
if selected == "တွက်စက်":
    st.header("💰 ရွှေ/ငွေ တွက်စက်")
    # တွက်စက် Code များ...

elif selected == "အမရာ (AI)":
    st.header("🤖 အမရာ (AI Assistant)")
    
    # API Key ကို Secrets မှ ခေါ်ယူခြင်း
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        instruction = "သင့်နာမည်က 'အမရာ' ဖြစ်သည်။ သင်သည် 'ကိုမင်းသစ္စာအောင်' တီထွင်ထားသော 'ပန်းတိမ်လက်ထောက် AI' ဖြစ်သည်။ အသုံးပြုသူက နှုတ်ဆက်လျှင် 'ကျမက အမရာ ပါ ဒီ app ကို တီထွင်သူ ကိုမင်းသစ္စာအောင်ရဲ့ ပန်းတိမ်လက်ထောက် AI ဖြစ်ပါတယ် ဘာများကူညီပေးရမလဲ ရှင့်' ဟု ယဉ်ကျေးစွာ စတင်ဖြေကြားပါ။"
        
        # Chat History
        if "messages" not in st.session_state: st.session_state.messages = []
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
            
        if prompt := st.chat_input("မေးခွန်းမေးပါ..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                model = genai.GenerativeModel(model_name='gemini-2.0-flash', system_instruction=instruction)
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error("API Key ချိတ်ဆက်မှုတွင် Error ရှိနေပါသည်။")

# တခြား Tab များအတွက်...
