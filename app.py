import streamlit as st

st.set_page_config(
    page_title="Ahmed Asran Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ================= HEADER =================

st.title("🚀 Ahmed Asran")
st.subheader("Data Engineering Student")

st.write("""
Passionate about Data Engineering, Big Data, and Real-Time Analytics.
Interested in Kafka, Spark, Airflow, Python, and Streamlit.
""")

# ================= SIDEBAR =================

st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "Personal Info",
        "Education",
        "Skills",
        "Training",
        "Projects",
        "Contact"
    ]
)

# ================= PERSONAL INFO =================

if section == "Personal Info":

    st.header("👤 Personal Information")

    st.write("**Name:** Ahmed Asran")
    st.write("**Location:** Cairo, Egypt")
    st.write("**University:** Helwan University")
    st.write("**Major:** Computer Science")
    st.write("**Track:** Data Engineering")

# ================= EDUCATION =================

elif section == "Education":

    st.header("🎓 Education")

    st.write("""
    - Faculty of Computers and Artificial Intelligence
    - Helwan University
    - Level 2 Computer Science
    """)

# ================= SKILLS =================

elif section == "Skills":

    st.header("💻 Skills")

    skills = [
        "Python",
        "SQL",
        "Streamlit",
        "Pandas",
        "NumPy",
        "Kafka",
        "Spark",
        "Airflow",
        "Git & GitHub"
    ]

    for skill in skills:
        st.success(skill)

# ================= TRAINING =================

elif section == "Training":

    st.header("📚 Training & Courses")

    st.write("""
    - Data Engineering Fundamentals
    - Python Programming
    - SQL & Databases
    - Kafka Basics
    - Streamlit Development
    """)

# ================= PROJECTS =================

elif section == "Projects":

    st.header("🚀 Projects")

    st.subheader("1. Streamlit Portfolio App")
    st.write("Personal portfolio web application using Streamlit.")

    st.subheader("2. Data Engineering Dashboard")
    st.write("Analytics dashboard with charts and metrics.")

    st.subheader("3. Kafka Streaming Project")
    st.write("Real-time data streaming simulation.")

# ================= CONTACT =================

elif section == "Contact":

    st.header("📞 Contact")

    st.write("📧 Email: your-email@gmail.com")
    st.write("🔗 LinkedIn: linkedin.com/in/your-profile")
    st.write("💻 GitHub: github.com/Ahmedasran")

    st.success("Thank you for visiting my portfolio!")
