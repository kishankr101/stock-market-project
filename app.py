import streamlit as st

st.set_page_config(page_title="Stock Predictor", layout="wide")

# Session State
if "step" not in st.session_state:
    st.session_state.step = "Signup"

# Sidebar
st.sidebar.title("📊 Navigation")

# AFTER DASHBOARD → SHOW FULL MENU
if st.session_state.step == "Dashboard":

    menu = st.sidebar.radio("Go to", ["Home", "Profile", "Logout"])

    # LOGOUT
    if menu == "Logout":
        st.session_state.step = "Signup"
        st.rerun()

    # PROFILE EDIT
    elif menu == "Profile":
        st.title("👤 Edit Profile")

        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=100)
        region = st.text_input("Region")
        pan = st.text_input("PAN Card Number")
        aadhar = st.text_input("Aadhar Card Number")
        mobile = st.text_input("Mobile Number")

        if st.button("Update Profile"):
            st.success("Profile Updated!")

    # HOME / DASHBOARD
    elif menu == "Home":
        st.title("📊 Main Dashboard")

        # SEARCH BOX
        search = st.text_input("🔍 Search Stocks")

        if search:
            st.write(f"Showing results for: {search}")

        # INDIAN INDICES
        st.subheader("🇮🇳 Indian Indices")

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("NIFTY 50", "22,000", "+1.2%")
        col2.metric("SENSEX", "73,000", "+0.9%")
        col3.metric("BANK NIFTY", "48,000", "+1.5%")
        col4.metric("NIFTY IT", "35,000", "-0.5%")
        col5.metric("MIDCAP", "12,000", "+0.7%")

        # 20 STOCKS LIST
        st.subheader("🏢 Top Indian Companies")

        companies = [
            "Reliance", "TCS", "Infosys", "HDFC Bank", "ICICI Bank",
            "SBI", "Wipro", "HCL Tech", "LT", "ITC",
            "Bharti Airtel", "Asian Paints", "Maruti Suzuki", "Titan",
            "Sun Pharma", "Power Grid", "NTPC", "ONGC", "Adani Ports", "Coal India"
        ]

        cols = st.columns(4)
        for i, company in enumerate(companies):
            cols[i % 4].write(f"• {company}")

# BEFORE DASHBOARD FLOW (NO CHANGE LOGIC)
elif st.session_state.step == "Signup":
    st.title("📝 Signup")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        st.success("Signup Successful!")
        st.session_state.step = "Login"

elif st.session_state.step == "Login":
    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Login Successful!")
        st.session_state.step = "Profile"

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
