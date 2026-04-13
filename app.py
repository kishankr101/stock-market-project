import streamlit as st

st.set_page_config(page_title="Stock Predictor", layout="wide")

# ---------- CUSTOM UI (BLUE/GREEN THEME) ----------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.stApp {
    background: linear-gradient(135deg, #0f172a, #022c22);
    color: white;
}
h1, h2, h3 {
    color: #22c55e;
}
.stButton>button {
    background-color: #22c55e;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION ----------
if "step" not in st.session_state:
    st.session_state.step = "Signup"

# ---------- SIDEBAR ----------
st.sidebar.title("📊 Navigation")

# ---------- DASHBOARD ----------
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

    # HOME
    elif menu == "Home":
        st.title("📊 Main Dashboard")

        # SEARCH
        search = st.text_input("🔍 Search Stocks")

        if search:
            st.write(f"Showing results for: {search}")

        # ---------- TOP 10 PERFORMING STOCKS ----------
        st.subheader("🚀 Top 10 Performing Stocks")

        top_stocks = [
            "Reliance", "TCS", "Infosys", "HDFC Bank", "ICICI Bank",
            "SBI", "Wipro", "HCL Tech", "LT", "ITC"
        ]

        cols = st.columns(5)
        for i, stock in enumerate(top_stocks):
            cols[i % 5].success(stock)

        # ---------- INDICES SELECTION ----------
        st.subheader("📊 Select Indices")

        index_option = st.selectbox(
            "Choose Index",
            ["NIFTY 50", "SENSEX", "BANK NIFTY", "NIFTY IT", "MIDCAP"]
        )

        # ---------- INDEX BASED COMPANIES ----------
        st.subheader(f"🏢 Companies in {index_option}")

        index_data = {
            "NIFTY 50": ["Reliance", "TCS", "Infosys", "HDFC Bank"],
            "SENSEX": ["HDFC Bank", "ICICI Bank", "ITC", "LT"],
            "BANK NIFTY": ["SBI", "HDFC Bank", "ICICI Bank", "Axis Bank"],
            "NIFTY IT": ["TCS", "Infosys", "Wipro", "HCL Tech"],
            "MIDCAP": ["Adani Power", "Jindal Steel", "Voltas", "Page Industries"]
        }

        companies = index_data.get(index_option, [])

        cols = st.columns(2)
        for i, company in enumerate(companies):
            cols[i % 2].write(f"• {company}")

# ---------- SIGNUP ----------
elif st.session_state.step == "Signup":
    st.title("📝 Signup")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        st.success("Signup Successful!")
        st.session_state.step = "Login"

# ---------- LOGIN ----------
elif st.session_state.step == "Login":
    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Login Successful!")
        st.session_state.step = "Profile"

# ---------- PROFILE ----------
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
