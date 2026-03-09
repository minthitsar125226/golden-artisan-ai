import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Page Config
st.set_page_config(page_title="The Golden Artisan", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* မျက်နှာပြင် အလွတ်ဖြစ်စေရန် */
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* Sidebar အနက်ရောင်နှင့် ရွှေရောင် Border */
    [data-testid="stSidebar"] { 
        background-color: #0a0a0a; 
        border-right: 1px solid #d4af37;
    }
    
    /* စာသားအရောင် */
    h1, h2, h3 { color: #d4af37 !important; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar အတွင်းတွင်သာ Menu ထားခြင်း ---
with st.sidebar:
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=100)
    except:
        st.write("💎")
        
    st.markdown("---")
    
    # Tool များကို Sidebar ထဲမှာပဲ Icon နဲ့ အလျားလိုက် (သို့မဟုတ်) ထောင်လိုက်ပြခြင်း
    selected = option_menu(
        "Tools", 
        ["ရွှေတွက်", "အချိုး", "ရွှေဈေး", "လက်စွပ်", "အမရာ"],
        icons=['calculator', 'percent', 'graph-up', 'gem', 'robot'],
        menu_icon="cast", default_index=None,
        styles={
            "nav-link-selected": {"background-color": "#d4af37", "color": "black"},
        }
    )

# --- Main Screen Logic ---
if selected == "ရွှေတွက်":
    st.header("💰 ရွှေတွက်ရန်")
elif selected == "အချိုး":
    st.header("📐 အချိုးအစား")
elif selected == "ရွှေဈေး":
    st.header("📈 ရွှေဈေး")
elif selected == "လက်စွပ်":
    st.header("💍 လက်စွပ်")
elif selected == "အမရာ":
    st.header("🤖 အမရာ AI")
else:
    # ဘာမှမရွေးထားရင် Main Screen က အလွတ်ပဲဖြစ်နေပါမယ်
    pass 

# Footer
st.markdown('<div style="text-align: center; color: #d4af37; font-size: 10px; margin-top: 50px;">App by MinThitSarAung</div>', unsafe_allow_html=True)
