import streamlit as st

# Page Config
st.set_page_config(page_title="Stock Predictor", layout="wide")

# Sidebar Navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to", [
    "Home",
    "Login",
    "Signup",
    "Dashboard",
    "Search",
    "Prediction",
    "Profile",
    "Settings",
    "Admin"
])

# Home Page
if page == "Home":
    st.title("📈 Stock Market Prediction App")
    st.write("Welcome! Predict stock trends using smart analysis.")

    st.subheader("🔥 Trending Stocks")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Apple", "$175", "+2.5%")

    with col2:
        st.metric("Tesla", "$240", "-1.2%")

    with col3:
        st.metric("Amazon", "$130", "+1.8%")

# Login Page
elif page == "Login":
    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Logged in successfully!")

# Signup Page
elif page == "Signup":
    st.title("📝 Signup")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        st.success("Account created!")

# Dashboard
elif page == "Dashboard":
    st.title("📊 Dashboard")

    st.subheader("Market Overview")
    st.metric("NIFTY 50", "22,000", "+1.2%")

    st.subheader("Your Watchlist")
    st.write("AAPL, TSLA, AMZN")

# Search Page
elif page == "Search":
    st.title("🔍 Search Stocks")

    stock = st.text_input("Enter Stock Name")

    if stock:
        st.write(f"Showing results for: {stock}")
        st.button("View Details")

# Prediction Page
elif page == "Prediction":
    st.title("🤖 Stock Prediction")

    stock = st.text_input("Enter Stock Symbol")

    if st.button("Predict"):
        st.success("📈 Stock likely to go UP")

# Profile
elif page == "Profile":
    st.title("👤 Profile")
    st.write("User details will appear here")

# Settings
elif page == "Settings":
    st.title("⚙️ Settings")
    st.write("Theme, preferences, etc.")

# Admin Panel
elif page == "Admin":
    st.title("🛠 Admin Panel")
    st.write("Manage users and stocks")
