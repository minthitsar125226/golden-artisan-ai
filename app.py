import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Page Config
st.set_page_config(page_title="The Golden Artisan", layout="centered")

# --- CUSTOM CSS (အနက်ရောင်နောက်ခံ၊ ရွှေရောင် Theme) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #e0e0e0; }
    
    /* Sidebar ကို အနက်ရောင်ထားခြင်း */
    [data-testid="stSidebar"] { 
        background-color: #0a0a0a; 
        border-right: 1px solid #d4af37;
    }
    
    /* စာသားများနှင့် Header */
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    
    /* Sidebar အတွင်းမှ ခေါင်းစဉ်များ */
    .sidebar-text { color: #d4af37; font-size: 14px; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar အတွင်းတွင် Logo နှင့် Tool များထည့်ခြင်း ---
with st.sidebar:
    # Logo ကို Sidebar အပေါ်ဆုံးတွင် ခပ်သေးသေး ပြခြင်း
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=100) # width 100 ဖြင့် ပိုသေးသွားအောင် ပြုလုပ်ခြင်း
    except:
        st.write("💎")
        
    st.markdown("---")
    
    # Sidebar တွင် Icon ဖြင့် Tool များ ပြခြင်း
    selected = option_menu(
        "Menu", 
        ["ရွှေတွက်", "အချိုး", "ရွှေဈေး", "လက်စွပ်", "အမရာ"],
        icons=['calculator', 'percent', 'graph-up', 'gem', 'robot'],
        menu_icon="cast", default_index=0,
        styles={
            "nav-link": {"color": "#e0e0e0"},
            "nav-link-selected": {"background-color": "#d4af37", "color": "black"},
        }
    )

# --- Navigation Logic ---
if selected == "ရွှေတွက်":
    st.header("💰 ရွှေတွက်ရန်")
elif selected == "အမရာ":
    st.header("🤖 အမရာ AI")

# အောက်ခြေ Brand Credit
st.markdown('<div style="text-align: center; color: #d4af37; font-size: 10px; margin-top: 50px;">App by MinThitSarAung</div>', unsafe_allow_html=True)
