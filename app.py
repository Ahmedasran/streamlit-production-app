import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Ahmed Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Ahmed Streamlit Production App")

st.sidebar.header("Settings")

option = st.sidebar.selectbox(
    "Choose View",
    ["Home", "Analytics", "Data"]
)

# ================= HOME =================
if option == "Home":
    st.header("Welcome")
    st.write("This is my production Streamlit application.")

    st.success("Application is running successfully!")

    st.subheader("💬 Write Anything")

    user_input = st.text_area(
        "Enter your message here",
        placeholder="Type something..."
    )

    if st.button("Send"):
        if user_input.strip() != "":
            st.balloons()
            st.success(f"You entered: {user_input}")
        else:
            st.warning("Please write something first.")

# ================= ANALYTICS =================
elif option == "Analytics":
    st.header("📊 Analytics Dashboard")

    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )

    st.line_chart(data)

    st.metric(label="Users", value="1,250", delta="+12%")
    st.metric(label="Revenue", value="$5,400", delta="+8%")

# ================= DATA =================
elif option == "Data":
    st.header("📁 Data Table")

    df = pd.DataFrame({
        "Name": ["Ahmed", "Ali", "Sara"],
        "Age": [21, 22, 20],
        "Department": ["Data", "AI", "Backend"]
    })

    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="⬇ Download Data",
        data=csv,
        file_name='data.csv',
        mime='text/csv',
    )