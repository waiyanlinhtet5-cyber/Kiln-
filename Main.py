import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Kiln Equipment Search", layout="centered")

st.title("🔍 Kiln Equipment Inventory")

# Data loading
try:
    # GitHub ထဲမှာ data.csv ရှိနေဖို့ လိုပါတယ်
    df = pd.read_csv("data.csv")
    
    search_query = st.text_input("စက်အမည် ရိုက်ပါ (ဥပမာ- Motor)", "").strip()

    if st.button("Search"):
        if search_query:
            # စက်အမည် column ထဲမှာ ရှာဖွေခြင်း
            # Note: Column name က 'Machine' ဖြစ်ရပါမယ်။ (အစ်ကို့ csv ထဲကအတိုင်း ပြင်နိုင်ပါတယ်)
            results = df[df.iloc[:, 0].str.contains(search_query, case=False, na=False)]

            if not results.empty:
                for index, row in results.iterrows():
                    with st.container():
                        st.subheader(f"⚙️ {row.iloc[0]}")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**🛢️ Oil:** {row.get('Oil', 'N/A')}")
                            st.write(f"**🔧 Wrench:** {row.get('Wrench', 'N/A')}")
                        with col2:
                            st.write(f"**🛠️ Spanner:** {row.get('Spanner', 'N/A')}")
                            st.write(f"**⛽ Grease:** {row.get('Grease', 'N/A')}")
                        st.divider()
            else:
                st.warning("❌ ရှာမတွေ့ပါ။ စာလုံးပေါင်း ပြန်စစ်ကြည့်ပါ။")
        else:
            st.info("ရှာဖွေလိုသည့် အမည်ကို ရိုက်ထည့်ပေးပါ။")

except Exception as e:
    st.error(f"Error loading data: {e}")