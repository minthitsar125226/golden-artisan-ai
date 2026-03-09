import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="The Golden Artisan", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #d4af37; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    # Logo
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=100)
    except:
        st.write("💎")
        
    st.markdown("---")
    
    # option_menu အစား radio ကိုသုံးခြင်း (Error လုံးဝမတက်ပါ)
    choice = st.sidebar.radio(
        "Menu", 
        ["ရွှေတွက်", "အချိုး", "ရွှေဈေး", "လက်စွပ်", "အမရာ"],
        index=None  # အစမှာ ဘာမှမရွေးထားပါ
    )

# --- Main Screen ---
if choice == "ရွှေတွက်":
    st.header("💰 ရွှေတွက်ရန်")
elif choice == "အချိုး":
    st.header("📐 အချိုးအစားတွက်ရန်")
elif choice == "ရွှေဈေး":
    st.header("📈 ရွှေဈေးနှုန်း")
elif choice == "လက်စွပ်":
    st.header("💍 လက်စွပ်အတိုင်းအတာ")
elif choice == "အမရာ":
    st.header("🤖 အမရာ AI Assistant")

# Footer Credit
st.markdown('<div style="text-align: center; color: #d4af37; font-size: 10px; margin-top: 50px;">App by MinThitSarAung</div>', unsafe_allow_html=True)
