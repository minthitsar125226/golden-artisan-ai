import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Page Configuration
st.set_page_config(page_title="The Golden Artisan", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    [data-testid="stSidebar"] { display: none; }
    
    /* Card Design */
    .custom-card {
        background-color: #1a1a1a;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
        border: 1px solid #333;
        text-align: center;
    }
    .card-title { color: #d4af37; font-size: 13px; margin-bottom: 5px; }
    .card-value { color: #ffffff; font-size: 18px; font-weight: bold; }
    
    /* Footer Credit */
    .footer { text-align: center; color: #d4af37; font-size: 11px; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# Logo
try:
    logo = Image.open("logo.png")
    st.image(logo, width=150)
except:
    st.write("💎")

# --- Content ---
st.subheader("Market Prices")
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="custom-card"><div class="card-title">Gold (Ah Khout)</div><div class="card-value">10,750,000</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="custom-card"><div class="card-title">Gold (15 Pae Yae)</div><div class="card-value">10,100,000</div></div>', unsafe_allow_html=True)

# --- Bottom Navigation (Facebook Style) ---
selected = option_menu(
    None, ["Home", "Calendar", "Tips", "3D", "Settings"],
    icons=['house', 'calendar-date', 'gift', 'box', 'gear'],
    orientation="horizontal",
    styles={
        "container": {"position": "fixed", "bottom": "0", "width": "100%", "background-color": "#1a1a1a"},
        "nav-link-selected": {"background-color": "#d4af37", "color": "black"},
    }
)

# Footer
st.markdown('<div class="footer">App by MinThitSarAung</div>', unsafe_allow_html=True)
