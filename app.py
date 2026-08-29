import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Student Performance Early-Warning System",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# Load trained model and threshold
# --------------------------------------------------

model = joblib.load("student_performance_model.pkl")
threshold = joblib.load("risk_threshold.pkl")

# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 1.2rem;
    }

    .developer {
        text-align: center;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    .footer {
        text-align: center;
        font-size: 0.9rem;
        margin-top: 2rem;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">'
    '🎓 Student Performance Early-Warning System'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'An AI-based tool for identifying students who may benefit '
    'from early academic support.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="developer">'
    '<b>Alishba Ejaz</b><br>'
    '<i>Developed using ML & Streamlit</i>'
    '</div>',
    unsafe_allow_html=True
)

st.info(
    "⚠️ This system is an early-warning support tool, not a definitive "
    "prediction of a student's future performance."
)

st.divider()

# --------------------------------------------------
# Student Information
# --------------------------------------------------

st.header("👤 Student Information")

col1, col2, col3 = st.columns(3)

with col1:
    school = st.selectbox("School", ["GP", "MS"])
    sex = st.selectbox("Sex", ["F", "M"])
    age = st.number_input(
        "Age",
        min_value=15,
        max_value=22,
        value=16
    )

with col2:
    address = st.selectbox("Address", ["U", "R"])
    famsize = st.selectbox("Family Size", ["GT3", "LE3"])
    Pstatus = st.selectbox("Parent Status", ["A", "T"])

with col3:
    Medu = st.selectbox(
        "Mother's Education",
        [0, 1, 2, 3, 4]
    )

    Fedu = st.selectbox(
        "Father's Education",
        [0, 1, 2, 3, 4]
    )

    guardian = st.selectbox(
        "Guardian",
        ["mother", "father", "other"]
    )

st.divider()

# --------------------------------------------------
# Academic & Family Factors
# --------------------------------------------------

st.header("📚 Academic & Family Factors")

col1, col2, col3 = st.columns(3)

with col1:
    Mjob = st.selectbox(
        "Mother's Job",
        ["teacher", "health", "services", "at_home", "other"]
    )

    Fjob = st.selectbox(
        "Father's Job",
        ["teacher", "health", "services", "at_home", "other"]
    )

with col2:
    reason = st.selectbox(
        "Reason for Choosing School",
        ["home", "reputation", "course", "other"]
    )

    traveltime = st.selectbox(
        "Travel Time",
        [1, 2, 3, 4]
    )

with col3:
    studytime = st.selectbox(
        "Weekly Study Time",
        [1, 2, 3, 4]
    )

    failures = st.number_input(
        "Past Class Failures",
        min_value=0,
        max_value=4,
        value=0
    )

st.divider()

# --------------------------------------------------
# Support & Activities
# --------------------------------------------------

st.header("🤝 Support & Activities")

col1, col2, col3, col4 = st.columns(4)

with col1:
    schoolsup = st.selectbox(
        "School Support",
        ["yes", "no"]
    )

with col2:
    famsup = st.selectbox(
        "Family Support",
        ["yes", "no"]
    )

with col3:
    paid = st.selectbox(
        "Paid Extra Classes",
        ["yes", "no"]
    )

with col4:
    activities = st.selectbox(
        "Extra Activities",
        ["yes", "no"]
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    nursery = st.selectbox(
        "Attended Nursery School",
        ["yes", "no"]
    )

with col2:
    higher = st.selectbox(
        "Wants Higher Education",
        ["yes", "no"]
    )

with col3:
    internet = st.selectbox(
        "Internet Access",
        ["yes", "no"]
    )

with col4:
    romantic = st.selectbox(
        "In a Romantic Relationship",
        ["yes", "no"]
    )

st.divider()

# --------------------------------------------------
# Lifestyle & Health
# --------------------------------------------------

st.header("🧠 Lifestyle & Health")

col1, col2, col3, col4 = st.columns(4)

with col1:
    famrel = st.slider(
        "Family Relationship Quality",
        1, 5, 4
    )

with col2:
    freetime = st.slider(
        "Free Time",
        1, 5, 3
    )

with col3:
    goout = st.slider(
        "Going Out",
        1, 5, 3
    )

with col4:
    health = st.slider(
        "Current Health",
        1, 5, 3
    )

col1, col2 = st.columns(2)

with col1:
    Dalc = st.slider(
        "Workday Alcohol Consumption",
        1, 5, 1
    )

with col2:
    Walc = st.slider(
        "Weekend Alcohol Consumption",
        1, 5, 1
    )

absences = st.number_input(
    "Number of Absences",
    min_value=0,
    max_value=100,
    value=5
)

st.divider()

# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.header("🔮 Early-Warning Prediction")

st.write(
    "Enter the student's information above and click the button "
    "below to generate an early-warning risk assessment."
)

if st.button(
    "🔍 Assess Student Risk",
    use_container_width=True
):

    # Create input dataframe with the exact feature names
    # expected by the trained model.

    student_data = pd.DataFrame([{
        "school": school,
        "sex": sex,
        "age": age,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "reason": reason,
        "guardian": guardian,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences
    }])

    # Get probability of being At Risk

    probabilities = model.predict_proba(student_data)

    classes = model.named_steps["classifier"].classes_

    at_risk_index = list(classes).index("At Risk")

    risk_probability = probabilities[0][at_risk_index]

    # --------------------------------------------------
    # Apply selected threshold
    # --------------------------------------------------

    if risk_probability >= threshold:

        st.error("🔴 Potentially At Risk")

        st.metric(
            "Estimated Risk Probability",
            f"{risk_probability:.1%}"
        )

        st.warning(
            "The model indicates that this student may benefit "
            "from additional academic support."
        )

    else:

        st.success("🟢 Not At Risk")

        st.metric(
            "Estimated Risk Probability",
            f"{risk_probability:.1%}"
        )

        st.success(
            "The model does not currently flag this student "
            "as potentially at risk."
        )

    st.caption(
        f"Prediction threshold used: {threshold:.2f}"
    )

    st.divider()

    st.subheader("📊 Model Output")

    st.write(
        f"Estimated probability of being At Risk: "
        f"**{risk_probability:.1%}**"
    )

    st.progress(float(risk_probability))

# --------------------------------------------------
# About the System
# --------------------------------------------------

st.divider()

with st.expander("ℹ️ About This System"):

    st.write(
        "This application uses a machine-learning model to estimate "
        "whether a student may be at risk of poor academic performance."
    )

    st.write(
        "The system considers academic, family, social, and lifestyle "
        "factors provided by the user."
    )

    st.write(
        f"The selected decision threshold is **{threshold:.0%}**. "
        "Students with an estimated risk probability at or above this "
        "threshold are flagged as potentially at risk."
    )

    st.warning(
        "The prediction should be used as an early-warning indicator "
        "and should not replace professional academic assessment or "
        "individual student support."
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    '<b>Student Performance Early-Warning System</b><br>'
    'Alishba Ejaz | Developed using ML & Streamlit'
    '</div>',
    unsafe_allow_html=True
)
