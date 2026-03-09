import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Page Configuration
st.set_page_config(page_title="The Golden Artisan", layout="wide")

# --- CUSTOM CSS: အနက်ရောင်နှင့် ရွှေရောင် Theme ---
st.markdown("""
    <style>
    /* အခြေခံနောက်ခံ အနက်ရောင် */
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* Sidebar ကို အနက်ရောင်ထားခြင်း */
    [data-testid="stSidebar"] { 
        background-color: #0a0a0a; 
        border-right: 1px solid #d4af37;
    }
    
    /* ခေါင်းစဉ်စာသားများ ရွှေရောင် */
    h1, h2, h3 { color: #d4af37 !important; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar အတွင်းတွင် Logo နှင့် Menu ထည့်ခြင်း ---
with st.sidebar:
    # Logo ကို Sidebar အပေါ်ဆုံးတွင် သေးသေးလေး ထည့်ခြင်း
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=100)
    except:
        st.write("💎")
        
    st.markdown("---")
    
    # Sidebar တွင် Tool များပြခြင်း (နှိပ်မှသာ အလုပ်လုပ်မည်)
    selected = option_menu(
        menu_title="Tools", 
        options=["ရွှေတွက်", "အချိုး", "ရွှေဈေး", "လက်စွပ်", "အမရာ"],
        icons=['calculator', 'percent', 'graph-up', 'gem', 'robot'],
        menu_icon="cast", 
        default_index=None, # အစတွင် ဘာမှ မရွေးထားပါ
        styles={
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

# အောက်ခြေ Brand Credit (စာမျက်နှာတိုင်းတွင် ပေါ်နေမည်)
st.markdown('<div style="text-align: center; color: #d4af37; font-size: 10px; margin-top: 50px;">App by MinThitSarAung</div>', unsafe_allow_html=True)
