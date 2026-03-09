import streamlit as st
from streamlit_option_menu import option_menu
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
    
    # option_menu ကို အမှားကင်းအောင် ရေးသားထားခြင်း
    selected = option_menu(
        menu_title=None, # Sidebar မှာဖြစ်တဲ့အတွက် None ထားတာ ပိုကောင်းပါတယ်
        options=["ရွှေတွက်", "အချိုး", "ရွှေဈေး", "လက်စွပ်", "အမရာ"],
        icons=['calculator', 'percent', 'graph-up', 'gem', 'robot'],
        menu_icon="cast", 
        default_index=None,
        styles={
            "nav-link": {"color": "white", "font-size": "14px"},
            "nav-link-selected": {"background-color": "#d4af37", "color": "black"},
        }
    )

# --- Main Screen (ရွေးချယ်မှသာ ပေါ်လာမည်) ---
if selected == "ရွှေတွက်":
    st.header("💰 ရွှေတွက်ရန်")
elif selected == "အချိုး":
    st.header("📐 အချိုးအစားတွက်ရန်")
elif selected == "ရွှေဈေး":
    st.header("📈 ရွှေဈေးနှုန်း")
elif selected == "လက်စွပ်":
    st.header("💍 လက်စွပ်အတိုင်းအတာ")
elif selected == "အမရာ":
    st.header("🤖 အမရာ AI Assistant")

# Footer Credit
st.markdown('<div style="text-align: center; color: #d4af37; font-size: 10px; margin-top: 50px;">App by MinThitSarAung</div>', unsafe_allow_html=True)
