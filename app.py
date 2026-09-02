import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# PROFESSIONAL APP DESIGN
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #f7f9fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e6eaf0;
    }

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

    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e6eaf0;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
    }

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        min-height: 45px;
    }

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    .hero-card {
        background: linear-gradient(
            135deg,
            #eef4ff 0%,
            #f8fbff 100%
        );
        border: 1px solid #dbe7ff;
        border-radius: 18px;
        padding: 28px;
        margin-bottom: 25px;
    }

    .small-card {
        background: #ffffff;
        border: 1px solid #e6eaf0;
        border-radius: 16px;
        padding: 20px;
        min-height: 145px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.03);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "average_marks" not in st.session_state:
    st.session_state.average_marks = None

if "attendance" not in st.session_state:
    st.session_state.attendance = None

if "risk_probability" not in st.session_state:
    st.session_state.risk_probability = None

if "risk_status" not in st.session_state:
    st.session_state.risk_status = "Not Assessed"

if "study_hours" not in st.session_state:
    st.session_state.study_hours = None

if "sleep_hours" not in st.session_state:
    st.session_state.sleep_hours = None

if "mood" not in st.session_state:
    st.session_state.mood = None

if "stress" not in st.session_state:
    st.session_state.stress = None


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

    # --------------------------------------------------------
    # HERO SECTION
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-content">
                <div class="hero-icon">🎓</div>
                <div>
                    <h1>Student Performance AI</h1>
                    <p>
                        Your personal academic companion for tracking
                        performance, building better habits and
                        identifying potential academic challenges early.
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # OVERVIEW
    # --------------------------------------------------------

    st.subheader("📊 Student Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.session_state.risk_probability is not None:
            st.metric(
                "🧠 Risk Probability",
                f"{st.session_state.risk_probability:.1%}"
            )
        else:
            st.metric(
                "🧠 Risk Probability",
                "—"
            )

    with col2:

        st.metric(
            "📌 Academic Status",
            st.session_state.risk_status
        )

    with col3:

        if st.session_state.study_hours is not None:
            st.metric(
                "📚 Study Hours",
                f"{st.session_state.study_hours:.1f} hrs"
            )
        else:
            st.metric(
                "📚 Study Hours",
                "—"
            )

    with col4:

        if st.session_state.sleep_hours is not None:
            st.metric(
                "😴 Sleep",
                f"{st.session_state.sleep_hours:.1f} hrs"
            )
        else:
            st.metric(
                "😴 Sleep",
                "—"
            )

    # --------------------------------------------------------
    # ACADEMIC SNAPSHOT
    # --------------------------------------------------------

    st.divider()

    st.subheader("📚 Academic Snapshot")

    if st.session_state.average_marks is not None:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Average Marks",
                f"{st.session_state.average_marks:.1f}/100"
            )

            if st.session_state.average_marks >= 75:

                st.success(
                    "🌟 Excellent performance!"
                )

            elif st.session_state.average_marks >= 50:

                st.info(
                    "👍 Your performance is satisfactory."
                )

            else:

                st.warning(
                    "⚠️ This area may need more attention."
                )

        with col2:

            st.metric(
                "Attendance",
                f"{st.session_state.attendance:.0f}%"
            )

            if st.session_state.attendance >= 75:

                st.success(
                    "✅ Attendance is looking good."
                )

            else:

                st.warning(
                    "⚠️ Consider improving attendance."
                )

    else:

        st.info(
            "📌 Complete the Academic Performance section "
            "to see your academic snapshot."
        )

    # --------------------------------------------------------
    # QUICK ACTIONS
    # --------------------------------------------------------

    st.divider()

    st.subheader("🚀 Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="small-card">
                <div class="card-icon">📚</div>
                <h3>Academic Performance</h3>
                <p>
                    Record your marks and attendance
                    and keep track of your progress.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="small-card">
                <div class="card-icon">🧠</div>
                <h3>Risk Assessment</h3>
                <p>
                    Use machine learning to identify
                    potential academic risk early.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="small-card">
                <div class="card-icon">💬</div>
                <h3>Ask Student AI</h3>
                <p>
                    Get practical guidance for
                    common academic challenges.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

   # --------------------------------------------------------
# STUDENT WELL-BEING
# --------------------------------------------------------

st.divider()

st.subheader("🌱 Your Student Journey")

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        <div class="small-card">
            <h3>📈 Track Your Progress</h3>
            <p>Monitor marks, attendance and study habits
            to understand your academic journey.</p>
            <br>
            <h3>🎯 Set Better Goals</h3>
            <p>Focus on small, realistic improvements
            instead of trying to change everything at once.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="small-card">
            <h3>🌙 Take Care of Yourself</h3>
            <p>Sleep, routine and well-being can all
            influence how effectively you study.</p>
            <br>
            <h3>💬 Ask for Guidance</h3>
            <p>When something feels difficult, use
            Student AI or speak with someone you trust.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    # --------------------------------------------------------
    # PERSONALIZED TIP
    # --------------------------------------------------------

    st.divider()

    st.subheader("💡 Student Tip")

    if st.session_state.average_marks is None:

        st.info(
            "🎯 Start by entering your marks and attendance "
            "in Academic Performance."
        )

    elif st.session_state.average_marks < 50:

        st.warning(
            "📚 Focus on the subjects where you are struggling "
            "most and practise them regularly."
        )

    elif (
        st.session_state.study_hours is not None
        and st.session_state.study_hours < 2
    ):

        st.info(
            "⏱️ Try adding a short focused study session "
            "to your daily routine."
        )

    elif (
        st.session_state.sleep_hours is not None
        and st.session_state.sleep_hours < 6
    ):

        st.info(
            "😴 Your sleep routine may need attention. "
            "Try to maintain a consistent sleep schedule."
        )

    else:

        st.success(
            "🌟 Keep going! Consistency is one of the most "
            "important parts of academic progress."
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
