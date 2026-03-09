import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Page Config
st.set_page_config(page_title="The Golden Artisan", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* Footer */
    .footer {
        position: fixed; left: 0; bottom: 80px; width: 100%;
        text-align: center; color: #d4af37; font-size: 11px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar (အလုပ်လုပ်ရန် လိုအပ်သည့် Setting များအတွက်)
with st.sidebar:
    st.title("Settings")
    st.write("အခြားဆက်တင်များ")

# Logo ပြသခြင်း
try:
    logo = Image.open("logo.png")
    st.image(logo, use_container_width=True)
except:
    st.write("💎")

# --- Bottom Navigation (အဓိက Menu) ---
selected = option_menu(
    None, ["ရွှေတွက်", "အချိုး", "ရွှေဈေး", "လက်စွပ်", "အမရာ"],
    icons=['calculator', 'percent', 'graph-up', 'gem', 'robot'],
    orientation="horizontal",
    styles={
        "container": {"position": "fixed", "bottom": "0", "width": "100%", "background-color": "#1a1a1a"},
        "nav-link-selected": {"background-color": "#d4af37", "color": "black"},
    }
)

# --- Navigation Logic ---
if selected == "ရွှေတွက်":
    st.header("💰 ရွှေတွက်ရန်")
elif selected == "အချိုး":
    st.header("📐 အချိုးအစားတွက်ရန်")
elif selected == "ရွှေဈေး":
    st.header("📈 ရွှေဈေးနှုန်း")
elif selected == "လက်စွပ်":
    st.header("💍 လက်စွပ်အတိုင်း")
elif selected == "အမရာ":
    st.header("🤖 အမရာ AI")

# Footer Credit
st.markdown('<div class="footer">App by MinThitSarAung</div>', unsafe_allow_html=True)
