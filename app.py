import streamlit as st

st.set_page_config(page_title="Stock Predictor", layout="wide")

# Session State (to control flow)
if "step" not in st.session_state:
    st.session_state.step = "Signup"

# Sidebar (locked navigation)
st.sidebar.title("📊 Navigation")

# SHOW ONLY CURRENT STEP
st.sidebar.write(f"Current Step: {st.session_state.step}")

# STEP 1: SIGNUP
if st.session_state.step == "Signup":
    st.title("📝 Signup")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        st.success("Signup Successful!")
        st.session_state.step = "Login"

# STEP 2: LOGIN
elif st.session_state.step == "Login":
    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Login Successful!")
        st.session_state.step = "Profile"

# STEP 3: PROFILE DETAILS
elif st.session_state.step == "Profile":
    st.title("👤 Complete Your Profile")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    region = st.text_input("Region")
    pan = st.text_input("PAN Card Number")
    aadhar = st.text_input("Aadhar Card Number")
    mobile = st.text_input("Mobile Number")

    if st.button("Save Profile"):
        st.success("Profile Saved Successfully!")
        st.session_state.step = "Dashboard"

# STEP 4: DASHBOARD (ONLY AFTER ALL STEPS)
elif st.session_state.step == "Dashboard":
    st.title("📊 Welcome the stock market world")

    st.success("Welcome to Main Dashboard!")

    st.subheader("🔥 Trending Stocks")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Apple", "$175", "+2.5%")

    with col2:
        st.metric("Tesla", "$240", "-1.2%")

    with col3:
        st.metric("Amazon", "$130", "+1.8%")
