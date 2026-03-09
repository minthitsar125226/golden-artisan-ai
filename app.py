import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Page Config
st.set_page_config(page_title="The Golden Artisan", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #e0e0e0; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #d4af37; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
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
    
    # နှိပ်မှသာ Tool ရောက်မည့် Menu
    selected = option_menu(
        "Menu", 
        ["ရွှေတွက်", "အချိုး", "ရွှေဈေး", "လက်စွပ်", "အမရာ"],
        icons=['calculator', 'percent', 'graph-up', 'gem', 'robot'],
        menu_icon="cast", default_index=None, # default_index=None ထားခြင်းဖြင့် အစတွင် ဘာမှ မရွေးထားပါ။
        styles={
            "nav-link-selected": {"background-color": "#d4af37", "color": "black"},
        }
    )

# --- Navigation Logic ---
# အစပိုင်းတွင် selected သည် None ဖြစ်နေသဖြင့် ဘာမှ ပေါ်မလာပါ။
if selected == "ရွှေတွက်":
    st.header("💰 ရွှေတွက်ရန်")
    st.write("တွက်ချက်မှုများ ဤနေရာတွင် ပေါ်လာပါမည်။")
elif selected == "အချိုး":
    st.header("📐 အချိုးအစားတွက်ရန်")
elif selected == "ရွှေဈေး":
    st.header("📈 ရွှေဈေးနှုန်းများ")
elif selected == "လက်စွပ်":
    st.header("💍 လက်စွပ်အတိုင်းအတာ")
elif selected == "အမရာ":
    st.header("🤖 အမရာ AI Assistant")
else:
    # ဘာမှ မရွေးရသေးလျှင် မျက်နှာပြင် အလွတ်ဖြစ်နေပါမည်
    st.empty() 

# Brand Credit
st.markdown('<div style="text-align: center; color: #d4af37; font-size: 10px; margin-top: 50px;">App by MinThitSarAung</div>', unsafe_allow_html=True)
