
import streamlit as st
from PIL import Image

# Page Config
st.set_page_config(page_title="The Golden Artisan", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #d4af37; }
    
    /* Header Style */
    .custom-header {
        color: #d4af37;
        font-size: 18px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 20px;
        text-align: center;
        letter-spacing: 1px;
    }

    /* Content Card Style (Facebook Card ဆန်ဆန်) */
    .content-card {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    
    /* Sidebar Button Style */
    div.stButton > button {
        width: 100%;
        background-color: transparent;
        color: #e0e0e0;
        border: 1px solid #d4af37;
        margin-bottom: 10px;
        text-align: left;
        border-radius: 10px;
        padding: 10px;
        transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #d4af37; color: black; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=80)
    except:
        st.write("💎")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if 'page' not in st.session_state:
        st.session_state.page = None

    if st.button("💰 ရွှေတွက်ရန်"): st.session_state.page = "GOLD_CALC"
    if st.button("📐 အချိုးအစား"): st.session_state.page = "RATIO_CALC"
    if st.button("📈 ရွှေဈေးနှုန်း"): st.session_state.page = "MARKET_PRICE"
    if st.button("💍 လက်စွပ်အတိုင်း"): st.session_state.page = "RING_SIZE"
    if st.button("🤖 အမရာ AI"): st.session_state.page = "AMARA_AI"

# --- Main Screen Content ---
if st.session_state.page == "GOLD_CALC":
    st.markdown('<p class="custom-header">ရွှေတွက်ရန်</p>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        # ဒီနေရာမှာ ရွှေတွက်စက် Formula များ ထည့်ပါမည်
        st.write("ရွှေအလေးချိန်နှင့် ဈေးနှုန်းတွက်ချက်မှုများ...")
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "RATIO_CALC":
    st.markdown('<p class="custom-header">အချိုးအစားတွက်ရန်</p>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.write("ရွှေအချိုးအစားနှင့် အရောအနှောတွက်ချက်မှုများ...")
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "MARKET_PRICE":
    st.markdown('<p class="custom-header">ယနေ့ရွှေဈေးနှုန်း</p>', unsafe_allow_html=True)
    # Card နှစ်ခုယှဉ်ပြခြင်း
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="content-card" style="text-align:center;"><small>အခေါက်ရွှေ</small><h4>10,7xx,xxx</h4></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="content-card" style="text-align:center;"><small>၁၅ ပဲရည်</small><h4>10,1xx,xxx</h4></div>', unsafe_allow_html=True)

elif st.session_state.page == "RING_SIZE":
    st.markdown('<p class="custom-header">လက်စွပ်အတိုင်းအတာ</p>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">လက်စွပ်တိုင်းတာရန် လမ်းညွှန်ချက်များ...</div>', unsafe_allow_html=True)

elif st.session_state.page == "AMARA_AI":
    st.markdown('<p class="custom-header">အမရာ AI Assistant</p>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">မင်္ဂလာပါ၊ ကျွန်မ အမရာပါ။ ဘာများကူညီပေးရမလဲရှင်။</div>', unsafe_allow_html=True)

else:
    # အစပိုင်းတွင် ပေါ်မည့် မျက်နှာပြင် (Welcome Message သို့မဟုတ် Logo အကြီး)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; opacity:0.5;">Menu မှ Tool တစ်ခုကို ရွေးချယ်ပါ</div>', unsafe_allow_html=True)

# Footer
st.markdown(f'<div style="text-align: center; color: #d4af37; font-size: 10px; margin-top: 50px;">App by MinThitSarAung</div>', unsafe_allow_html=True)
