
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

# --- Tab 5: AI လက်ထောက် (Smart Model Switching System) ---
with tab5:
    st.subheader("🤖 ပန်းတိမ်လက်ထောက် AI (Smart Mode)")
    api_key = st.sidebar.text_input("Gemini API Key ထည့်ပါ", type="password")
    
    if api_key:
        try:
            genai.configure(api_key=api_key)
            
            # အသုံးပြုမည့် Model စာရင်း (ဦးစားပေးအလိုက်)
            available_models = [
                'gemini-2.0-flash', 
                'gemini-2.0-flash-lite', 
                'gemini-1.5-flash-latest',
                'gemini-pro-latest'
            ]
            
            if "messages" not in st.session_state:
                st.session_state.messages = []
            
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])
            
            if prompt := st.chat_input("ရွှေပန်းတိမ်ဆိုင်ရာ ဘာများမေးချင်ပါသလဲ?"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)
                
                with st.chat_message("assistant"):
                    response_text = ""
                    success = False
                    
                    # Model များကို တစ်ခုပြီးတစ်ခု စမ်းသပ်ခြင်း
                    for model_name in available_models:
                        try:
                            model = genai.GenerativeModel(model_name)
                            response = model.generate_content(prompt)
                            response_text = response.text
                            success = True
                            # အောင်မြင်သွားရင် loop ထဲက ထွက်မယ်
                            break 
                        except Exception as e:
                            # ဒီ Model မရရင် နောက်တစ်ခုကို ဆက်စမ်းမယ်
                            continue
                    
                    if success:
                        st.markdown(response_text)
                        st.session_state.messages.append({"role": "assistant", "content": response_text})
                    else:
                        st.error("ရနိုင်သမျှ Model အားလုံး Quota ပြည့်နေပါသည်။ ခဏစောင့်ပြီးမှ ပြန်စမ်းပေးပါခင်ဗျာ။")
                
        except Exception as e:
            st.error(f"Error ဖြစ်နေသည်: {e}")
    else:
        st.warning("Sidebar တွင် API Key အရင်ထည့်ပေးပါ။")
