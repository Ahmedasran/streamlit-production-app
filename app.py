import streamlit as st
import time

st.set_page_config(
    page_title="Ahmed Asran Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ================= ANIMATION =================

progress = st.progress(0)

for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

progress.empty()

# ================= HEADER =================

st.markdown("""
# 🚀 Ahmed Mohamed Asran
### Data Engineering Student | Kafka | Spark | Airflow
""")

st.info("Aspiring Data Engineer passionate about Real-Time Streaming & Big Data Engineering.")

# ================= SIDEBAR =================

st.sidebar.title("📌 Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "About",
        "Education",
        "Training",
        "Projects",
        "Skills",
        "Contact"
    ]
)

# ================= ABOUT =================

if section == "About":

    st.header("👨‍💻 About Me")

    st.write("""
Aspiring Data Engineer with hands-on experience building real-time streaming pipelines
and ETL/ELT workflows using Kafka, Spark, Airflow, Hadoop, and Hive.

Currently pursuing a B.Sc. in Information Systems and advancing practical skills through
the Digital Egypt Pioneers Initiative (DEPI).
""")

# ================= EDUCATION =================

elif section == "Education":

    st.header("🎓 Education")

    st.subheader("Capital University – Helwan")
    st.write("📍 Cairo, Egypt")
    st.write("B.Sc. in Information Systems")
    st.write("Sep 2023 – Jun 2027")

    st.success("Relevant Areas")
    st.write("""
- Databases
- Data Structures
- Big Data Engineering
- Data Mining
- Programming Languages
""")

    st.divider()

    st.subheader("The American University in Cairo (AUC)")
    st.write("English Language Program – Level B1")

# ================= TRAINING =================

elif section == "Training":

    st.header("📚 Training")

    st.subheader("Digital Egypt Pioneers Initiative (DEPI)")
    st.write("Data Engineering Track")

    st.write("""
- Built end-to-end data pipelines
- Streaming & Real-Time Processing
- ETL / ELT Workflows
""")

    st.info("""
Technologies:
Python | SQL | Kafka | Spark | Airflow | Hive | Hadoop
""")

# ================= PROJECTS =================

elif section == "Projects":

    st.header("🚀 Projects")

    # Project 1
    with st.container():

        st.subheader("🎬 Real-Time Movie Ratings Analytics")

        st.write("""
Designed an end-to-end real-time streaming pipeline
to collect and analyze movie ratings data.
""")

        st.success("Tech Stack")
        st.write("""
Kafka | Apache NiFi | Spark | SQL | NoSQL
""")

    st.divider()

    # Project 2
    with st.container():

        st.subheader("🚗 Real-Time Traffic Accident Analytics")

        st.write("""
Built a real-time streaming pipeline to ingest and analyze traffic accident data.
""")

        st.success("Features")
        st.write("""
- Geospatial Analysis
- High-Risk Area Detection
- Peak Accident Times
""")

    st.divider()

    # Project 3
    with st.container():

        st.subheader("🩺 Disease Prediction Models")

        st.write("""
Built Machine Learning classification models
using Scikit-learn and Pandas.
""")

        st.success("Algorithms")
        st.write("""
KNN | Logistic Regression | SVM | Random Forest
""")

# ================= SKILLS =================

elif section == "Skills":

    st.header("💻 Skills")

    st.subheader("Programming")

    st.progress(90, text="Python")
    st.progress(80, text="SQL")
    st.progress(60, text="Java")

    st.divider()

    st.subheader("Big Data & Streaming")

    st.progress(85, text="Kafka")
    st.progress(80, text="Spark")
    st.progress(75, text="Airflow")
    st.progress(70, text="Hadoop")
    st.progress(70, text="Hive")

    st.divider()

    st.subheader("Databases")

    st.progress(80, text="SQL Databases")
    st.progress(70, text="MongoDB / NoSQL")

# ================= CONTACT =================

elif section == "Contact":

    st.header("📞 Contact")

    st.write("📧 ahmedmohammedasran839@gmail.com")
    st.write("📱 01120580571")

    st.write("🔗 LinkedIn")
    st.write("💻 GitHub: github.com/Ahmedasran")

    st.balloons()

    st.success("Thank you for visiting my portfolio 🚀")
