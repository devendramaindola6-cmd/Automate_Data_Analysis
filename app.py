import streamlit as st
import pandas as pd
import sweetviz
import tempfile
import os

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="Local Data Analysis AI",
    page_icon="📊",
    layout="wide"
)

# --------------------------
# CUSTOM CSS
# --------------------------
st.markdown("""
<style>

.stApp {
    background-color: #f7f9fc;
}

div.block-container {
    padding-top: 2rem;
}

.sidebar .sidebar-content {
    background: #1a1a2e;
}

span, label {
    font-size: 16px !important;
}

/* Header */
.big-header {
    font-size: 38px;
    font-weight: 700;
    color: #1a1a2e;
    padding-bottom: 10px;
}

.sub-header {
    font-size: 20px;
    font-weight: 500;
    color: #36454F;
}

/* Cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* Buttons */
.stButton>button {
    background-color: #4a47a3;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 18px;
    font-size: 16px;
}

.stButton>button:hover {
    background-color: #6c63ff;
}

</style>
""", unsafe_allow_html=True)


# --------------------------
# SIDEBAR
# --------------------------

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2099/2099074.png", width=80)
    st.markdown("<h2 style='color:white;'>Data Analysis AI</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color:#d0d0d0;'>Your local AI-powered data analysis assistant.</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown("<p style='color:#d0d0d0;'>Upload CSV → Auto-analyze → Download reports.</p>",
                unsafe_allow_html=True)
    st.markdown("---")


# --------------------------
# MAIN APP
# --------------------------

st.markdown("<div class='big-header'>📊 Local Data Analysis AI Tool</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Upload your dataset and let AI analyze, profile and summarize it automatically.</div><br>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("### 🧾 Preview Your Data")
    st.dataframe(df, use_container_width=True)

    st.markdown("### 📈 Basic Dataset Info")
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("<div class='card'>📋 **Rows:** " + str(df.shape[0]) + "</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='card'>📌 **Columns:** " + str(df.shape[1]) + "</div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div class='card'>📁 **Missing Values:** " + str(df.isnull().sum().sum()) + "</div>", unsafe_allow_html=True)

    st.markdown("### 🤖 Ask AI About Your Dataset")

    user_query = st.text_input("Example: 'What are the key trends?', 'Summarize this dataset', 'Find insights'")

    if user_query:
        # SIMPLE RULE-BASED AI (improve later)
        st.markdown("#### 🧠 AI Response")
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        if "summary" in user_query.lower():
            st.write(df.describe(include='all'))

        elif "missing" in user_query.lower():
            st.write(df.isnull().sum())

        else:
            st.write("Here are some quick insights:")
            st.write(df.head())

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 📊 Auto-Generate Analysis Report")

    if st.button("Generate Sweetviz Report"):
        with st.spinner("Generating Report... Please wait..."):
            report = sweetviz.analyze(df)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
                report_file = tmp.name

            report.show_html(filepath=report_file, open_browser=False)

        st.success("Report generated successfully! 🎉")

        with open(report_file, "rb") as f:
            st.download_button(
                label="⬇ Download Sweetviz Report (HTML)",
                data=f,
                file_name="sweetviz_report.html",
                mime="text/html"
            )

