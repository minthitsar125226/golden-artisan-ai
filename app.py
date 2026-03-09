
import streamlit as st
from PIL import Image

# Page Config
st.set_page_config(page_title="The Golden Artisan", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* မျက်နှာပြင် အပြင်အဆင် */
    .stApp { background-color: #000000; color: #ffffff; }
    [data-testid="stSidebar"] { 
        background-color: #0a0a0a; 
        border-right: 1px solid #d4af37; 
    }
    
    /* ခေါင်းစဉ်ကို အချိုးကျစွာ ချုံ့ပြီး နေရာချခြင်း */
    .custom-header {
        color: #d4af37;
        font-size: 18px; /* စာလုံးကို ထပ်ချုံ့ထားသည် */
        font-weight: bold;
        margin-top: 30px; /* အပေါ်မှ နည်းနည်းပြန်ချထားသည် */
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* Sidebar Buttons */
    div.stButton > button {
        width: 100%;
        background-color: transparent;
        color: white;
        border: 1px solid #d4af37;
        margin-bottom: 8px;
        text-align: left;
        border-radius: 8px;
    }
    div.stButton > button:hover { 
        background-color: #d4af37; 
        color: black; 
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    # Logo
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=80) # Logo ကိုလည်း ပိုကျစ်လျစ်အောင် လုပ်ထားသည်
    except:
        st.write("💎")
        
    st.markdown("---")
    
    if 'page' not in st.session_state:
        st.session_state.page = None

    # Tools Navigation
    if st.button("💰 ရွှေတွက်ရန်"): st.session_state.page = "ရွှေတွက်ရန်"
    if st.button("📐 အချိုးအစားတွက်ရန်"): st.session_state.page = "အချိုးအစားတွက်ရန်"
    if st.button("📈 ရွှေဈေးနှုန်း"): st.session_state.page = "ရွှေဈေးနှုန်း"
    if st.button("💍 လက်စွပ်အတိုင်းအတာ"): st.session_state.page = "လက်စွပ်အတိုင်းအတာ"
    if st.button("🤖 အမရာ AI Assistant"): st.session_state.page = "အမရာ AI Assistant"

# --- Main Screen ---
if st.session_state.page:
    # ခေါင်းစဉ်ကို စာသားအပြည့်အစုံဖြင့် သေသပ်စွာပြခြင်း
    st.markdown(f'<p class="custom-header">{st.session_state.page}</p>', unsafe_allow_html=True)
else:
    # ဘာမှမရွေးရသေးခင် မျက်နှာပြင်အလွတ်
    st.empty()

# Brand Credit
st.markdown('<div style="text-align: center; color: #d4af37; font-size: 10px; margin-top: 50px; opacity: 0.6;">App by MinThitSarAung</div>', unsafe_allow_html=True)
