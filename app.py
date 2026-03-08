
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

# --- Tab 5: AI လက်ထောက် (Public Mode) ---
with tab5:
    st.subheader("🤖 ပန်းတိမ်လက်ထောက် AI (အမရာ)")
    
    # Sidebar မှာ Key တောင်းတာကို ဖျက်ပြီး secrets ကနေ တိုက်ရိုက်ယူပါမယ်
    try:
        # 'GEMINI_API_KEY' ဆိုတဲ့ နာမည်နဲ့ Secrets ထဲမှာ သိမ်းရမှာဖြစ်ပါတယ်
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        instruction = "သင့်နာမည်က 'အမရာ' ဖြစ်သည်။ သင်သည် 'ကိုမင်းသစ္စာအောင်' တီထွင်ထားသော 'ပန်းတိမ်လက်ထောက် AI' ဖြစ်သည်။ အသုံးပြုသူက နှုတ်ဆက်လျှင် 'ကျမက အမရာ ပါ ဒီ app ကို တီထွင်သူ ကိုမင်းသစ္စာအောင်ရဲ့ ပန်းတိမ်လက်ထောက် AI ဖြစ်ပါတယ် ဘာများကူညီပေးရမလဲ ရှင့်' ဟု ယဉ်ကျေးစွာ စတင်ဖြေကြားပါ။"
        
        mega_model_list = [
            'gemini-3-flash-preview', 'gemini-2.0-flash-lite', 
            'gemini-2.0-flash', 'gemini-1.5-flash-latest'
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
                for m_name in mega_model_list:
                    try:
                        model = genai.GenerativeModel(model_name=m_name, system_instruction=instruction)
                        response = model.generate_content(prompt)
                        response_text = response.text
                        success = True
                        break 
                    except Exception:
                        continue 
                
                if success:
                    st.markdown(response_text)
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                else:
                    st.error("⚠️ လက်ရှိတွင် AI ဝန်ဆောင်မှု ခေတ္တပြတ်တောက်နေပါသည်။")
                    
    except KeyError:
        st.error("API Key ကို App Settings (Secrets) မှာ မထည့်ရသေးပါဘူးခင်ဗျာ။")
    except Exception as e:
        st.error(f"Error: {e}")
