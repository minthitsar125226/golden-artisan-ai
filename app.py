
import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="မြန်မာ့ရွှေပန်းတိမ် လက်ထောက်", layout="wide")

st.title("⚖️ မြန်မာ့ရွှေပန်းတိမ် လက်ထောက် App")

# Tabs ကြေညာခြင်း
tab1, tab2, tab3, tab4, tab5 = st.tabs(["ရွှေ/ငွေ တွက်စက်", "အချိုးအစား", "ရွှေဈေး", "အတိုင်းအတာ", "AI လက်ထောက်"])

# --- Tab 1: ရွှေ/ငွေ တွက်စက် ---
with tab1:
    st.subheader("ရွှေ/ငွေ တွက်ချက်ခြင်း")
    weight = st.number_input("အလေးချိန် (ကျပ်သား):", value=1.0)
    price = st.number_input("ဈေးနှုန်း (ကျပ်):", value=5000000)
    st.write(f"စုစုပေါင်း: {weight * price:,.0f} ကျပ်")

# --- Tab 2: အချိုးအစား ---
with tab2:
    st.subheader("ရွှေအချိုးအစား တွက်ချက်ခြင်း")

# --- Tab 3: ရွှေဈေး ---
with tab3:
    st.subheader("ကမ္ဘာ့ရွှေဈေးနှုန်း")

# --- Tab 4: အတိုင်းအတာ (၁၆ ပဲစနစ်) ---
with tab4:
    st.subheader("💍 လက်စွပ် နှင့် လက်ကောက် အတိုင်းအတာ (၁၆ ပဲစနစ်)")
    choice = st.radio("ဘာကို တိုင်းတာမှာလဲ:", ["လက်စွပ် (Ring)", "လက်ကောက် (Bangle)"], horizontal=True)
    pe_options = list(range(16))
    
    if choice == "လက်စွပ် (Ring)":
        r_inch = st.selectbox("လက်မ:", [1, 2], index=0, key="r1")
        r_pe = st.selectbox("ပဲ:", pe_options, index=12, key="r2")
        total = r_inch + (r_pe / 16)
        st.write(f"လုံးပတ်: {total:.2f} လက်မ ({total * 25.4:.1f} mm)")
    else:
        b_inch = st.selectbox("လက်မ:", [1, 2], index=1, key="b1")
        b_pe = st.selectbox("ပဲ:", pe_options, index=4, key="b2")
        total = b_inch + (b_pe / 16)
        st.write(f"အချင်း: {total:.2f} လက်မ")

# --- Tab 5: AI လက်ထောက် (All-Model Access System) ---
with tab5:
    st.subheader("🤖 ပန်းတိမ်လက်ထောက် AI (Multi-Model)")
    api_key = st.sidebar.text_input("Gemini API Key ထည့်ပါ", type="password")
    
    if api_key:
        try:
            genai.configure(api_key=api_key)
            
            # လူကြီးမင်းပေးထားတဲ့ စာရင်းထဲက အကောင်းဆုံးမော်ဒယ်များကို ဦးစားပေးအလိုက် စီထားပါတယ်
            full_model_list = [
                'gemini-3-flash-preview',      # အသစ်ဆုံး Model
                'gemini-2.0-flash-lite',       # Quota သက်သာသော Model
                'gemini-2.0-flash',            # အမြန်ဆုံး Model
                'gemma-3-27b-it',              # Gemma Series
                'gemini-1.5-flash-latest',     # Stable ဖြစ်သော Model
                'gemini-pro-latest'            # Pro Version
            ]
            
            if "messages" not in st.session_state:
                st.session_state.messages = []
            
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]): st.markdown(msg["content"])
            
            if prompt := st.chat_input("မေးခွန်းမေးပါ..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"): st.markdown(prompt)
                
                with st.chat_message("assistant"):
                    response_text = ""
                    success = False
                    tried_models = []

                    # Model အားလုံးကို တစ်ခုပြီးတစ်ခု ပတ်စမ်းခြင်း
                    for m_name in full_model_list:
                        try:
                            tried_models.append(m_name)
                            model = genai.GenerativeModel(m_name)
                            response = model.generate_content(prompt)
                            response_text = response.text
                            success = True
                            break 
                        except Exception:
                            continue 
                    
                    if success:
                        st.markdown(response_text)
                        st.session_state.messages.append({"role": "assistant", "content": response_text})
                        # ဘယ် Model နဲ့ အောင်မြင်သွားလဲဆိုတာကို အောက်ခြေမှာ သေးသေးလေး ပြပေးထားပါမယ်
                        st.caption(f"Used Model: {tried_models[-1]}")
                    else:
                        st.error("⚠️ စမ်းသပ်ခဲ့သော Model အားလုံး Quota ပြည့်နေပါသည်။")
                        st.write("စမ်းသပ်ခဲ့သည့် Model များ -")
                        st.json(tried_models)
                        st.info("💡 အချိန်ခဏစောင့်ဆိုင်းခြင်း သို့မဟုတ် API Key အသစ်လဲလှယ်ခြင်းဖြင့် ပြန်လည်စမ်းသပ်ပါ။")
                
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Sidebar တွင် API Key အရင်ထည့်ပေးပါ။")
