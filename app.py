
import streamlit as st
from PIL import Image

# Page Config
st.set_page_config(page_title="The Golden Artisan", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* မျက်နှာပြင် အပေါ်ပိုင်း ရွှေ့ခြင်း */
    .block-container { padding-top: 1rem; }
    
    .stApp { background-color: #000000; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #d4af37; }
    
    /* ခေါင်းစဉ်များ */
    h1 { color: #d4af37 !important; margin-top: -20px; }
    
    /* Button များ (Sidebar အတွက်) */
    div.stButton > button {
        width: 100%;
        background-color: transparent;
        color: white;
        border: 1px solid #d4af37;
        margin-bottom: 5px;
        text-align: left;
    }
    div.stButton > button:hover { background-color: #d4af37; color: black; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=100)
    except:
        st.write("💎")
        
    st.markdown("---")
    
    # Session State ကို သုံးပြီး Tool ရွေးချယ်ခြင်း
    if 'page' not in st.session_state: st.session_state.page = None

    if st.button("💰 ရွှေတွက်ရန်"): st.session_state.page = "ရွှေတွက်"
    if st.button("📐 အချိုးအစား"): st.session_state.page = "အချိုး"
    if st.button("📈 ရွှေဈေး"): st.session_state.page = "ရွှေဈေး"
    if st.button("💍 လက်စွပ်"): st.session_state.page = "လက်စွပ်"
    if st.button("🤖 အမရာ"): st.session_state.page = "အမရာ"

# --- Main Screen ---
# ခေါင်းစဉ်ကို အပေါ်ဆုံးထိ တင်ထားပေးသည်
if st.session_state.page == "ရွှေတွက်":
    st.header("💰 ရွှေတွက်ရန်")
elif st.session_state.page == "အချိုး":
    st.header("📐 အချိုးအစားတွက်ရန်")
elif st.session_state.page == "ရွှေဈေး":
    st.header("📈 ရွှေဈေးနှုန်း")
elif st.session_state.page == "လက်စွပ်":
    st.header("💍 လက်စွပ်အတိုင်းအတာ")
elif st.session_state.page == "အမရာ":
    st.header("🤖 အမရာ AI Assistant")
