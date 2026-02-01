import streamlit as st
import pandas as pd

# Page Setting (ပုံစံလှပအောင်)
st.set_page_config(page_title="Kiln Equipment Search", layout="wide")

# Google Sheet Link ကို CSV အဖြစ် ပြောင်းလဲခြင်း
# အစ်ကို့ Sheet URL ကို ဒီမှာ အစားထိုးပါ
sheet_url = "https://docs.google.com/spreadsheets/d/1XhblvRtP-QTpzuL6FpOV2TklAAh5gGLJ65psSJF0ozA/edit?gid=0#gid=0"
csv_url = sheet_url.replace('/edit', '/export?format=csv')

# Title
st.title("Kiln Equipment (Live Sync)")

try:
    # ဒေတာဖတ်ခြင်း
    df = pd.read_csv(csv_url)
    
    # Search Box (ပုံထဲကလို အပေါ်မှာ ထားပါမယ်)
    search_query = st.text_input("Search Equipment Name", placeholder="ဥပမာ- FN03").strip()

    if search_query:
        # ပထမဆုံး Column မှာ ရှာဖွေခြင်း
        results = df[df.iloc[:, 0].astype(str).str.contains(search_query, case=False, na=False)]

        if not results.empty:
            for index, row in results.iterrows():
                # ပုံထဲကလို Card ပုံစံ Expander သုံးပါမယ်
                with st.expander(f"⚙️ {row.iloc[0]}", expanded=True):
                    # Column တွေကို ပုံထဲကလို တစ်ကြောင်းချင်း စီပြပါမယ်
                    for col_name, value in row.items():
                        if col_name != df.columns[0]: # အမည်ကို ခေါင်းစဉ်မှာ ပြပြီးသားမို့ ချန်ခဲ့ပါမယ်
                            st.write(f"**{col_name}**")
                            st.write(f"{value}")
                            st.write("---") # မျဉ်းတားလေးခြားပါမယ်
        else:
            st.error("❌ ရှာမတွေ့ပါ။ စာလုံးပေါင်း ပြန်စစ်ကြည့်ပါ။")
    else:
        st.info("ရှာဖွေလိုသည့် စက်အမည်ကို ရိုက်ထည့်ပါ။")

except Exception as e:
    st.error(f"ချိတ်ဆက်မှု အမှားရှိနေပါသည်- {e}")