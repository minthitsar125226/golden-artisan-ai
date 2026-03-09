import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu
from PIL import Image

# Page Config
st.set_page_config(page_title="The Golden Artisan", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #e0e0e0; }
    
    /* Sidebar ကို ဖျောက်ခြင်း */
    [data-testid="stSidebar"] { display: none; }
    
    /* ခေါင်းစဉ်များ */
    h1, h2, h3 { color: #d4af37 !important; font-size: 20px !important; text-align: center; }
    
    /* Footer */
    .footer {
        position: fixed; left: 0; bottom: 60px; width: 100%;
        text-align: center; color: #d4af37; font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Logo ပြသခြင်း
try:
    logo = Image.open("logo.png")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2: st.image(logo, use_container_width=True)
except:
    st.write("💎")

# --- Bottom Navigation Menu ---
selected = option_menu(
    None, ["တွက်စက်", "အချိုး", "ဈေးနှုန်း", "အမရာ"],
    icons=['calculator', 'percent', 'graph-up', 'robot'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "nav-link": {"font-size": "14px", "color": "#ffffff"},
        "nav-link-selected": {"background-color": "#d4af37", "color": "black"},
    }
)

# --- Main Logic ---
if selected == "အမရာ":
    st.header("🤖 အမရာ (AI Assistant)")
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        if "messages" not in st.session_state: st.session_state.messages = []
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
            
        if prompt := st.chat_input("မေးခွန်းမေးပါ..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                model = genai.GenerativeModel('gemini-2.0-flash')
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
    except:
        st.error("API Key ချိတ်ဆက်မှု Error ဖြစ်နေပါသည်။")

# Footer
st.markdown('<div class="footer">App by MinThitSarAung</div>', unsafe_allow_html=True)
