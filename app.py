import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide",
    # ============================================================
# PROFESSIONAL APP DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: #f7f9fc;
    }

    /* Main content */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e6eaf0;
    }

    /* Sidebar title */
    section[data-testid="stSidebar"] h1 {
        font-size: 1.35rem;
        font-weight: 700;
    }

    /* Headings */
    h1 {
        font-weight: 750 !important;
        letter-spacing: -0.5px;
    }

    h2 {
        font-weight: 700 !important;
    }

    h3 {
        font-weight: 650 !important;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e6eaf0;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
    }

    div[data-testid="stMetricLabel"] {
        font-weight: 600;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        min-height: 45px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 5px 12px rgba(0,0,0,0.10);
    }

    /* Input boxes */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    textarea {
        border-radius: 10px !important;
    }

    /* Info / success / warning cards */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* Divider */
    hr {
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

    /* Footer */
    .app-footer {
        text-align: center;
        color: #7a8494;
        font-size: 0.85rem;
        padding: 25px 0 10px 0;
    }

    /* Welcome banner */
    .welcome-card {
        background: linear-gradient(
            135deg,
            #eef4ff 0%,
            #f8fbff 100%
        );
        border: 1px solid #dbe7ff;
        border-radius: 18px;
        padding: 25px 28px;
        margin-bottom: 25px;
    }

    .welcome-title {
        font-size: 1.7rem;
        font-weight: 750;
        margin-bottom: 6px;
    }

    .welcome-text {
        color: #596579;
        font-size: 1rem;
    }

    /* Quick action cards */
    .feature-card {
        background: #ffffff;
        border: 1px solid #e6eaf0;
        border-radius: 16px;
        padding: 20px;
        min-height: 145px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.03);
    }

    .feature-title {
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 8px;
    }

    .feature-text {
        color: #667085;
        font-size: 0.92rem;
        line-height: 1.5;
    }

    </style>
    """,
    unsafe_allow_html=True
)
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #f8faff 0%,
            #eef4ff 50%,
            #f8f5ff 100%
        );
    }

    /* Main content */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #172554 0%,
            #312e81 100%
        );
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Titles */
    h1 {
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }

    h2, h3 {
        font-weight: 700 !important;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid rgba(99, 102, 241, 0.12);
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 8px 24px rgba(30, 41, 59, 0.07);
    }

    [data-testid="stMetricLabel"] {
        font-weight: 600;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        min-height: 48px;
        font-weight: 700;
        border: none;
        background: linear-gradient(
            90deg,
            #4f46e5,
            #7c3aed
        );
        color: white;
        box-shadow: 0 6px 16px rgba(79, 70, 229, 0.20);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.30);
    }

    /* Info / success / warning boxes */
    .stAlert {
        border-radius: 14px;
    }

    /* Inputs */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }

    /* Section cards */
    .section-card {
        background: rgba(255, 255, 255, 0.86);
        border-radius: 20px;
        padding: 24px;
        margin: 12px 0 22px 0;
        border: 1px solid rgba(99, 102, 241, 0.10);
        box-shadow: 0 8px 25px rgba(30, 41, 59, 0.06);
    }

    .hero-card {
        background: linear-gradient(
            135deg,
            #312e81,
            #4f46e5,
            #7c3aed
        );
        color: white;
        padding: 32px;
        border-radius: 24px;
        margin-bottom: 25px;
        box-shadow: 0 12px 30px rgba(49, 46, 129, 0.25);
    }

    .hero-card h1,
    .hero-card p {
        color: white !important;
    }

    .small-card {
        background: white;
        border-radius: 18px;
        padding: 20px;
        height: 100%;
        border: 1px solid rgba(99, 102, 241, 0.10);
        box-shadow: 0 7px 20px rgba(30, 41, 59, 0.06);
    }

    .small-card h3 {
        margin-top: 0;
    }

    .footer {
        text-align: center;
        padding: 25px 0 5px 0;
        color: #64748b;
        font-size: 0.9rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "average_marks": None,
    "attendance": None,
    "risk_probability": None,
    "risk_status": "Not Assessed",
    "study_hours": None,
    "sleep_hours": None,
    "mood": None,
    "stress": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        padding:10px 0 20px 0;
    ">
        <div style="font-size:42px;">🎓</div>
        <h2 style="margin:0;">Student Performance AI</h2>
        <p style="opacity:0.8;">
            Early-Warning & Student Support
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Dashboard",
        "📚 Academic Performance",
        "⏱️ Study Tracker",
        "😴 Sleep & Routine",
        "💚 Well-being",
        "🧠 Risk Assessment",
        "💬 Ask Student AI"
    ]
)

st.sidebar.divider()

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        opacity:0.85;
        padding-top:10px;
    ">
        <p>Developed by</p>
        <strong>Alishba Ejaz</strong>
        <p style="font-size:12px;">
            Machine Learning + Streamlit
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
        """
        <div class="hero-card">
            <h1>🎓 Student Performance AI</h1>
            <p>
                A smart early-warning platform designed to help
                students understand their academic progress,
                study habits and well-being.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("📊 Student Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.session_state.risk_probability is not None:
            st.metric(
    "Risk Probability",
    f"{st.session_state.risk_probability:.1%}",
    border=True
)
        else:
            st.metric(
                "Risk Probability",
                "—"
            )

    with col2:

        st.metric(
    "Academic Status",
    st.session_state.risk_status,
    border=True
)

    with col3:

        if st.session_state.study_hours is not None:
            st.metric(
    "Study Hours",
    f"{st.session_state.study_hours:.1f} hrs",
    border=True
)
        else:
            st.metric(
                "Study Hours",
                "—"
            )

    with col4:

        if st.session_state.sleep_hours is not None:
           st.metric(
    "Sleep",
    f"{st.session_state.sleep_hours:.1f} hrs",
    border=True
)
        else:
            st.metric(
                "Sleep",
                "—"
            )

    st.divider()

    st.subheader("📚 Academic Summary")

    if st.session_state.average_marks is not None:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Average Marks",
                f"{st.session_state.average_marks:.1f}/100"
            )

        with col2:

            st.metric(
                "Attendance",
                f"{st.session_state.attendance:.0f}%"
            )

    else:

        st.info(
            "📌 Complete the Academic Performance section "
            "to see your academic summary here."
        )

    st.divider()

    st.subheader("🚀 Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="small-card">
                <h3>📚 Academic Performance</h3>
                <p>
                    Record your marks and attendance
                    and review your academic progress.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="small-card">
                <h3>🧠 Risk Assessment</h3>
                <p>
                    Use the machine-learning model to
                    identify potential academic risk.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="small-card">
                <h3>💬 Ask Student AI</h3>
                <p>
                    Describe an academic difficulty and
                    receive practical guidance.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("🌱 How This App Helps")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="small-card">

            ### 📈 Track Progress

            Keep an eye on your marks, attendance,
            study routine and other important factors.

            ### 🧠 Identify Potential Risk

            The ML model provides an early-warning
            indication based on the information you enter.

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="small-card">

            ### 🌱 Build Better Habits

            Monitor sleep, study habits and well-being
            to understand factors that may affect your studies.

            ### 💬 Get Guidance

            Use Student AI for simple suggestions when
            you are facing academic difficulties.

            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.success(
        "💡 Regularly reviewing your academic progress "
        "can help identify areas that may need attention."
    )


# ============================================================
# ACADEMIC PERFORMANCE
# ============================================================

elif page == "📚 Academic Performance":

    st.title("📚 Academic Performance")

    st.write(
        "Record your marks and attendance to understand "
        "your current academic performance."
    )

    st.divider()

    st.subheader("📝 Test Performance")

    col1, col2, col3 = st.columns(3)

    with col1:

        test1 = st.number_input(
            "Test 1 Marks",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    with col2:

        assignment = st.number_input(
            "Assignment Marks",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    with col3:

        test2 = st.number_input(
            "Test 2 Marks",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    attendance = st.number_input(
        "Attendance Percentage",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    st.divider()

    if st.button(
        "📊 Analyze Performance",
        use_container_width=True
    ):

        average_marks = (
            test1 +
            assignment +
            test2
        ) / 3

        st.session_state.average_marks = average_marks
        st.session_state.attendance = attendance

        st.subheader("📈 Performance Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Average Marks",
                f"{average_marks:.1f}/100"
            )

        with col2:

            st.metric(
                "Attendance",
                f"{attendance:.0f}%"
            )

        if average_marks >= 75:

            st.success(
                "🌟 Excellent academic performance!"
            )

        elif average_marks >= 50:

            st.info(
                "👍 Your performance is satisfactory. "
                "Keep working consistently."
            )

        else:

            st.warning(
                "⚠️ Your marks may need additional attention."
            )


# ============================================================
# STUDY TRACKER
# ============================================================

elif page == "⏱️ Study Tracker":

    st.title("⏱️ Study Tracker")

    st.write(
        "Keep track of your daily study hours and revision routine."
    )

    st.divider()

    st.subheader("📚 Today's Study")

    col1, col2 = st.columns(2)

    with col1:

        study_hours = st.number_input(
            "Study Hours",
            min_value=0.0,
            max_value=24.0,
            value=0.0,
            step=0.5
        )

    with col2:

        revision = st.selectbox(
            "Did you revise today?",
            ["Yes", "No"]
        )

    st.divider()

    if st.button(
        "💾 Save Study Record",
        use_container_width=True
    ):

        st.session_state.study_hours = study_hours

        st.success(
            f"✅ Study record saved: "
            f"{study_hours:.1f} hours."
        )

        if revision == "Yes":

            st.info(
                "📖 Great job! You kept up with revision today."
            )

        else:

            st.info(
                "💡 Consider setting aside a little time "
                "for revision."
            )


# ============================================================
# SLEEP & ROUTINE
# ============================================================

elif page == "😴 Sleep & Routine":

    st.title("😴 Sleep & Routine")

    st.write(
        "Monitor your sleep routine and understand "
        "how consistently you are resting."
    )

    st.divider()

    st.subheader("🌙 Sleep Information")

    col1, col2 = st.columns(2)

    with col1:

        sleep_hours = st.number_input(
            "Hours of Sleep",
            min_value=0.0,
            max_value=24.0,
            value=7.0,
            step=0.5
        )

    with col2:

        sleep_quality = st.slider(
            "Sleep Quality",
            min_value=1,
            max_value=5,
            value=3,
            help="1 = Very poor, 5 = Excellent"
        )

    st.divider()

    if st.button(
        "💾 Save Sleep Record",
        use_container_width=True
    ):

        st.session_state.sleep_hours = sleep_hours

        st.success(
            "✅ Sleep information recorded."
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Sleep",
                f"{sleep_hours:.1f} hours"
            )

        with col2:

            st.metric(
                "Sleep Quality",
                f"{sleep_quality}/5"
            )

        if sleep_hours < 6:

            st.warning(
                "🌙 Your recorded sleep is quite low. "
                "Try to maintain a more consistent sleep routine."
            )

        elif sleep_hours >= 7:

            st.success(
                "🌟 Your recorded sleep duration looks healthy."
            )

        else:

            st.info(
                "💡 Try to maintain a consistent sleep schedule."
            )


# ============================================================
# WELL-BEING
# ============================================================

elif page == "💚 Well-being":

    st.title("💚 Well-being")

    st.write(
        "Use a simple check-in to reflect on your mood "
        "and current stress level."
    )

    st.divider()

    st.subheader("🌱 Weekly Check-in")

    col1, col2 = st.columns(2)

    with col1:

        mood = st.slider(
            "How are you feeling today?",
            min_value=1,
            max_value=5,
            value=3,
            help="1 = Very low, 5 = Very good"
        )

    with col2:

        stress = st.slider(
            "Current Stress Level",
            min_value=1,
            max_value=5,
            value=3,
            help="1 = Very low, 5 = Very high"
        )

    st.divider()

    if st.button(
        "💚 Save Check-in",
        use_container_width=True
    ):

        st.session_state.mood = mood
        st.session_state.stress = stress

        st.success(
            "💚 Your check-in has been recorded."
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Mood",
                f"{mood}/5"
            )

        with col2:

            st.metric(
                "Stress",
                f"{stress}/5"
            )

        if stress >= 4:

            st.warning(
                "🌿 Your stress level is high. "
                "Consider taking a break and talking "
                "to someone you trust."
            )

        else:

            st.info(
                "🌱 Keep taking care of yourself and "
                "maintain a balanced routine."
            )


# ============================================================
# RISK ASSESSMENT
# ============================================================

elif page == "🧠 Risk Assessment":

    st.title("🧠 ML Risk Assessment")

    st.write(
        "Enter academic, family, social and lifestyle "
        "information to estimate potential academic risk."
    )

    st.info(
        "ℹ️ This prediction is an early-warning indicator. "
        "It should not replace teacher, counselor or "
        "professional judgment."
    )

    # --------------------------------------------------------
    # STUDENT INFORMATION
    # --------------------------------------------------------

    st.subheader("👤 Student Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        sex_label = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        sex = (
            "F"
            if sex_label == "Female"
            else "M"
        )

        age = st.number_input(
            "Age",
            min_value=15,
            max_value=25,
            value=17
        )

    with col2:

        address_label = st.selectbox(
            "Area of Residence",
            ["Urban", "Rural"]
        )

        address = (
            "U"
            if address_label == "Urban"
            else "R"
        )

        family_size_label = st.selectbox(
            "Family Size",
            [
                "3 or fewer members",
                "More than 3 members"
            ]
        )

        family_size = (
            "LE3"
            if family_size_label == "3 or fewer members"
            else "GT3"
        )

        parent_label = st.selectbox(
            "Parents' Living Arrangement",
            [
                "Living together",
                "Living separately"
            ]
        )

        parent_cohabitation = (
            "T"
            if parent_label == "Living together"
            else "A"
        )

    with col3:

        guardian_label = st.selectbox(
            "Guardian",
            [
                "Mother",
                "Father",
                "Other"
            ]
        )

        guardian_mapping = {
            "Mother": "mother",
            "Father": "father",
            "Other": "other"
        }

        guardian = guardian_mapping[guardian_label]

        reason_label = st.selectbox(
            "Main Reason for Choosing School",
            [
                "Course",
                "School reputation",
                "Close to home",
                "Other"
            ]
        )

        reason_mapping = {
            "Course": "course",
            "School reputation": "reputation",
            "Close to home": "home",
            "Other": "other"
        }

        reason = reason_mapping[reason_label]

        nursery_label = st.selectbox(
            "Attended Nursery School",
            ["Yes", "No"]
        )

        nursery = nursery_label.lower()

    st.divider()

    # --------------------------------------------------------
    # ACADEMIC & FAMILY FACTORS
    # --------------------------------------------------------

    st.subheader("🎓 Academic & Family Factors")

    col1, col2, col3 = st.columns(3)

    with col1:

        medu = st.slider(
            "Mother's Education",
            0,
            4,
            2,
            help="0 = No formal education, 4 = Higher education"
        )

        fedu = st.slider(
            "Father's Education",
            0,
            4,
            2,
            help="0 = No formal education, 4 = Higher education"
        )

        studytime = st.slider(
            "Weekly Study Time",
            1,
            4,
            2
        )

        failures = st.slider(
            "Past Class Failures",
            0,
            4,
            0
        )

    with col2:

        mjob = st.selectbox(
            "Mother's Job",
            [
                "teacher",
                "health",
                "services",
                "at_home",
                "other"
            ]
        )

        fjob = st.selectbox(
            "Father's Job",
            [
                "teacher",
                "health",
                "services",
                "at_home",
                "other"
            ]
        )

        traveltime = st.slider(
            "Travel Time to School",
            1,
            4,
            2
        )

        famrel = st.slider(
            "Family Relationship Quality",
            1,
            5,
            4
        )

    with col3:

        schoolsup = st.selectbox(
            "Extra School Support",
            ["yes", "no"]
        )

        famsup = st.selectbox(
            "Family Educational Support",
            ["yes", "no"]
        )

        paid = st.selectbox(
            "Extra Paid Classes",
            ["yes", "no"]
        )

        higher = st.selectbox(
            "Wants Higher Education",
            ["yes", "no"]
        )

    st.divider()

    # --------------------------------------------------------
    # SOCIAL & LIFESTYLE
    # --------------------------------------------------------

    st.subheader("🌱 Social & Lifestyle Factors")

    col1, col2, col3 = st.columns(3)

    with col1:

        activities = st.selectbox(
            "Extracurricular Activities",
            ["yes", "no"]
        )

        internet = st.selectbox(
            "Internet Access",
            ["yes", "no"]
        )

        romantic = st.selectbox(
            "Romantic Relationship",
            ["yes", "no"]
        )

        freetime = st.slider(
            "Free Time After School",
            1,
            5,
            3
        )

    with col2:

        goout = st.slider(
            "Going Out With Friends",
            1,
            5,
            3
        )

        Dalc = st.slider(
            "Weekday Alcohol Consumption",
            1,
            5,
            1
        )

        Walc = st.slider(
            "Weekend Alcohol Consumption",
            1,
            5,
            1
        )

        health = st.slider(
            "Current Health",
            1,
            5,
            3
        )

    with col3:

        absences = st.number_input(
            "School Absences",
            min_value=0,
            max_value=100,
            value=4,
            step=1
        )

        st.info(
            "💡 The information above corresponds "
            "to factors used by the trained ML model."
        )

    st.divider()

    # --------------------------------------------------------
    # RISK PREDICTION
    # --------------------------------------------------------

    st.subheader("🤖 Academic Risk Prediction")

    if st.button(
        "🔍 Assess Academic Risk",
        use_container_width=True
    ):

        try:

            model = joblib.load(
                "student_performance_model.pkl"
            )

            # ------------------------------------------------
            # IMPORTANT:
            # School is NOT displayed to the student.
            #
            # The original model may require the "school"
            # feature because it was trained with that feature.
            #
            # We detect whether the saved model expects it.
            # ------------------------------------------------

            student_values = {
                "sex": sex,
                "age": age,
                "address": address,
                "famsize": family_size,
                "Pstatus": parent_cohabitation,
                "Medu": medu,
                "Fedu": fedu,
                "Mjob": mjob,
                "Fjob": fjob,
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
            }

            # Detect expected features when available
            expected_features = getattr(
                model,
                "feature_names_in_",
                None
            )

            if expected_features is not None:

                expected_features = list(
                    expected_features
                )

                # If the model was trained with school,
                # provide it internally only.
                if "school" in expected_features:

                    student_values["school"] = "GP"

                student_data = pd.DataFrame(
                    [student_values]
                )

                # Match the model's expected column order.
                student_data = student_data[
                    expected_features
                ]

            else:

                # Fallback for the current saved pipeline.
                student_values["school"] = "GP"

                student_data = pd.DataFrame(
                    [student_values]
                )

            # ------------------------------------------------
            # PREDICTION
            # ------------------------------------------------

            probabilities = model.predict_proba(
                student_data
            )

            class_names = list(
                model.classes_
            )

            if "At Risk" not in class_names:

                st.error(
                    "The saved model does not contain "
                    "the expected 'At Risk' class."
                )

            else:

                at_risk_index = class_names.index(
                    "At Risk"
                )

                risk_probability = float(
                    probabilities[
                        0,
                        at_risk_index
                    ]
                )

                threshold = 0.40

                # ------------------------------------------------
                # STATUS
                # ------------------------------------------------

                if risk_probability >= threshold:

                    status = "Potentially At Risk"

                    st.error(
                        f"⚠️ {status}"
                    )

                else:

                    status = "Not At Risk"

                    st.success(
                        f"✅ {status}"
                    )

                # ------------------------------------------------
                # SAVE FOR DASHBOARD
                # ------------------------------------------------

                st.session_state.risk_probability = (
                    risk_probability
                )

                st.session_state.risk_status = (
                    status
                )

                # ------------------------------------------------
                # RESULTS
                # ------------------------------------------------

                st.subheader("📊 Prediction Results")

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Risk Probability",
                        f"{risk_probability:.1%}"
                    )

                with col2:

                    st.metric(
                        "Status",
                        status
                    )

                with col3:

                    st.metric(
                        "Decision Threshold",
                        f"{threshold:.0%}"
                    )

                st.progress(
                    min(
                        max(
                            risk_probability,
                            0.0
                        ),
                        1.0
                    )
                )

                if risk_probability >= threshold:

                    st.warning(
                        "The model estimates that this student "
                        "may benefit from additional academic "
                        "attention and support."
                    )

                else:

                    st.info(
                        "The model does not currently flag this "
                        "student as potentially at risk."
                    )

                st.caption(
                    "Model: Logistic Regression | "
                    "Risk threshold: 0.40"
                )

        except FileNotFoundError:

            st.error(
                "❌ student_performance_model.pkl was not found. "
                "Make sure the model file is in the same "
                "GitHub repository as app.py."
            )

        except Exception as e:

            st.error(
                f"⚠️ Prediction error: {e}"
            )


# ============================================================
# ASK STUDENT AI
# ============================================================

elif page == "💬 Ask Student AI":

    st.markdown(
        """
        <div class="hero-card">
            <h1>💬 Ask Student AI</h1>
            <p>
                Tell us what you're struggling with and
                get simple, practical guidance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "💡 This assistant provides general academic and "
        "student-support guidance. For serious personal, "
        "mental-health or safety concerns, please speak "
        "with a trusted person or qualified professional."
    )

    st.subheader("📝 What do you need help with?")

    topic = st.selectbox(
        "Choose an area",
        [
            "Academic Performance",
            "Study & Time Management",
            "Exam Preparation",
            "Attendance",
            "Stress & Well-being",
            "Motivation",
            "Other"
        ]
    )

    question = st.text_area(
        "Describe your problem",
        placeholder=(
            "Example: I am studying regularly but my "
            "marks are still not improving."
        ),
        height=160
    )

    st.divider()

    if st.button(
        "🤖 Get Guidance",
        use_container_width=True
    ):

        if not question.strip():

            st.warning(
                "Please describe what you are struggling with."
            )

        else:

            text = question.lower()

            st.subheader("💡 Student AI Guidance")

            if (
                "mark" in text
                or "grade" in text
                or "score" in text
                or topic == "Academic Performance"
            ):

                st.write(
                    "If your marks are not improving, begin by "
                    "identifying the subjects or topics causing "
                    "the most difficulty."
                )

                st.markdown(
                    """
                    **Try this:**

                    - Review your recent test mistakes.
                    - Identify 2–3 topics needing the most attention.
                    - Practise those topics instead of only rereading notes.
                    - Ask your teacher for clarification when you are stuck.
                    - Track your marks over time.
                    """
                )

            elif (
                "study" in text
                or "time" in text
                or "schedule" in text
                or topic == "Study & Time Management"
            ):

                st.write(
                    "A consistent study routine is usually more "
                    "effective than trying to study everything at once."
                )

                st.markdown(
                    """
                    **Try this:**

                    - Set a small daily study goal.
                    - Divide large subjects into smaller topics.
                    - Use focused study sessions with short breaks.
                    - Keep your phone away during focused sessions.
                    - Review what you learned at the end.
                    """
                )

            elif (
                "exam" in text
                or "test" in text
                or topic == "Exam Preparation"
            ):

                st.write(
                    "For exam preparation, focus on active practice "
                    "rather than only reading your notes."
                )

                st.markdown(
                    """
                    **Try this:**

                    - Make a realistic revision timetable.
                    - Practise previous questions or sample papers.
                    - Focus on difficult topics.
                    - Review mistakes.
                    - Get enough sleep before the exam.
                    """
                )

            elif (
                "absent" in text
                or "attendance" in text
                or topic == "Attendance"
            ):

                st.write(
                    "Regular attendance can make it easier to "
                    "keep up with lessons and assignments."
                )

                st.markdown(
                    """
                    **Try this:**

                    - Identify the reason for missed classes.
                    - Speak with your teacher if you have fallen behind.
                    - Collect missed notes and assignments.
                    - Create a plan for more consistent attendance.
                    - Ask your school for support when needed.
                    """
                )

            elif (
                "stress" in text
                or "anxious" in text
                or "anxiety" in text
                or "overwhelmed" in text
                or topic == "Stress & Well-being"
            ):

                st.write(
                    "Academic stress can make concentration difficult. "
                    "Try focusing on one manageable step at a time."
                )

                st.markdown(
                    """
                    **Try this:**

                    - Break your workload into smaller tasks.
                    - Take short breaks between study sessions.
                    - Maintain a regular sleep routine.
                    - Talk to someone you trust.
                    - If stress becomes overwhelming or persistent,
                      consider speaking with a qualified professional.
                    """
                )

            elif (
                "motivat" in text
                or "lazy" in text
                or "procrast" in text
                or topic == "Motivation"
            ):

                st.write(
                    "You do not need to feel motivated before starting. "
                    "Beginning with a very small task can help build momentum."
                )

                st.markdown(
                    """
                    **Try this:**

                    - Choose one small task.
                    - Set a short timer and start.
                    - Remove distractions.
                    - Track completed tasks.
                    - Reward yourself after finishing an important task.
                    """
                )

            else:

                st.write(
                    "Thanks for sharing your concern. Start by "
                    "breaking the problem into smaller parts and "
                    "identifying one thing you can improve first."
                )

                st.markdown(
                    """
                    **You could try:**

                    - Write down the specific problem.
                    - Identify what is within your control.
                    - Choose one small action to take today.
                    - Ask a teacher, mentor or trusted person for help.
                    - Check your progress after a few days.
                    """
                )

            st.success(
                "🌱 Small, consistent improvements can make a big difference."
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        <strong>Student Performance Early-Warning System</strong><br>
        Machine Learning + Streamlit<br>
        Developed by Alishba Ejaz
    </div>
    """,
    unsafe_allow_html=True
            )
