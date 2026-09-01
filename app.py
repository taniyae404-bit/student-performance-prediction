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
# SIDEBAR
# ============================================================

st.sidebar.title("🎓 Student Performance AI")

st.sidebar.caption(
    "Machine Learning Early-Warning System"
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

st.sidebar.caption("Developed by Alishba Ejaz")
st.sidebar.caption("Developed using Machine Learning & Streamlit")


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.title("🎓 Student Performance AI")

    st.write(
        "Welcome! This platform helps students monitor "
        "their academic progress and identify potential "
        "academic risk early."
    )

    st.divider()

    st.subheader("📊 Student Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Risk Probability",
            "—"
        )

    with col2:
        st.metric(
            "Academic Status",
            "Not Assessed"
        )

    with col3:
        st.metric(
            "Study Hours",
            "—"
        )

    with col4:
        st.metric(
            "Sleep",
            "—"
        )

    st.divider()

    st.subheader("🚀 Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "📚 **Academic Performance**\n\n"
            "Record and review your academic results."
        )

    with col2:
        st.info(
            "⏱️ **Study Tracker**\n\n"
            "Track your study and revision routine."
        )

    with col3:
        st.info(
            "🧠 **Risk Assessment**\n\n"
            "Use the ML model to assess academic risk."
        )

    st.divider()

    st.success(
        "💡 Regular tracking can help you identify "
        "areas that may need attention early."
    )


# ============================================================
# ACADEMIC PERFORMANCE
# ============================================================

elif page == "📚 Academic Performance":

    st.title("📚 Academic Performance")

    st.write(
        "Track your test results and monitor your "
        "academic progress."
    )

    st.subheader("📝 Test Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        test1 = st.number_input(
            "Test 1 Marks",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=1.0
        )

    with col2:
        assignment = st.number_input(
            "Assignment Marks",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=1.0
        )

    with col3:
        test2 = st.number_input(
            "Test 2 Marks",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=1.0
        )

    attendance = st.number_input(
        "Attendance Percentage",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
    )

    if st.button(
        "📊 Analyze Performance",
        use_container_width=True
    ):

        average_marks = (
            test1 +
            assignment +
            test2
        ) / 3

        st.subheader("📈 Performance Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Average Marks",
                f"{average_marks:.1f}"
            )

        with col2:
            st.metric(
                "Attendance",
                f"{attendance:.0f}%"
            )

        if average_marks >= 75:
            st.success(
                "🌟 Excellent academic performance."
            )

        elif average_marks >= 50:
            st.info(
                "👍 Your performance is satisfactory."
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
        "Keep track of your study hours and revision routine."
    )

    st.subheader("📚 Today's Study")

    study_hours = st.number_input(
        "Study Hours",
        min_value=0.0,
        max_value=24.0,
        value=0.0,
        step=0.5
    )

    revision = st.selectbox(
        "Did you revise today?",
        ["Yes", "No"]
    )

    if st.button(
        "Save Study Record",
        use_container_width=True
    ):

        st.success(
            f"✅ Study record saved: "
            f"{study_hours:.1f} hours."
        )

        if revision == "Yes":
            st.info("📖 Great job keeping up with revision!")
        else:
            st.info(
                "💡 Consider setting aside some time for revision."
            )


# ============================================================
# SLEEP & ROUTINE
# ============================================================

elif page == "😴 Sleep & Routine":

    st.title("😴 Sleep & Routine")

    st.write(
        "Monitor your sleep routine and daily habits."
    )

    st.subheader("🌙 Sleep Information")

    sleep_hours = st.number_input(
        "Hours of Sleep",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.5
    )

    sleep_quality = st.slider(
        "Sleep Quality",
        min_value=1,
        max_value=5,
        value=3
    )

    if st.button(
        "Save Sleep Record",
        use_container_width=True
    ):

        st.success(
            "✅ Sleep information recorded."
        )

        st.metric(
            "Sleep",
            f"{sleep_hours:.1f} hours"
        )

        st.metric(
            "Sleep Quality",
            f"{sleep_quality}/5"
        )


# ============================================================
# WELL-BEING
# ============================================================

elif page == "💚 Well-being":

    st.title("💚 Well-being")

    st.write(
        "Record simple weekly check-ins about your "
        "mood and stress levels."
    )

    st.subheader("🌱 Weekly Check-in")

    mood = st.slider(
        "How are you feeling today?",
        min_value=1,
        max_value=5,
        value=3
    )

    stress = st.slider(
        "Current Stress Level",
        min_value=1,
        max_value=5,
        value=3
    )

    if st.button(
        "Save Check-in",
        use_container_width=True
    ):

        st.success(
            "💚 Your check-in has been recorded."
        )

        if stress >= 4:
            st.warning(
                "You may benefit from taking a break "
                "and talking to someone you trust."
            )

        else:
            st.info(
                "Keep taking care of yourself and "
                "maintain a healthy routine."
            )


# ============================================================
# RISK ASSESSMENT
# ============================================================

elif page == "🧠 Risk Assessment":

    st.title("🧠 ML Risk Assessment")

    st.write(
        "Enter your academic, family, social and lifestyle "
        "information to estimate your potential academic risk."
    )

    st.info(
        "This prediction is an early-warning indicator and should "
        "not replace teacher, counselor or professional judgment."
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

        guardian = guardian_label.lower()

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
            2
        )

        fedu = st.slider(
            "Father's Education",
            0,
            4,
            2
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
    # SOCIAL & LIFESTYLE FACTORS
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
            value=4
        )

        st.write("")

        st.info(
            "💡 These inputs correspond to factors "
            "used by the trained ML model."
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

            # The current trained model expects the
            # original dataset's school feature.
            # School is NOT shown to the student.
            school = "GP"

            student_data = pd.DataFrame([{

                "school": school,

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

            }])

            probabilities = model.predict_proba(
                student_data
            )

            class_names = model.classes_

            at_risk_index = list(
                class_names
            ).index("At Risk")

            risk_probability = probabilities[
                0,
                at_risk_index
            ]

            threshold = 0.40

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
                float(risk_probability)
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

    st.title("💬 Ask Student AI")

    st.write(
        "Need help deciding what to focus on? "
        "Tell us about your academic difficulty."
    )

    question = st.text_area(
        "What are you struggling with?",
        placeholder=(
            "Example: I'm struggling with Mathematics "
            "and my marks aren't improving."
        )
    )

    if st.button(
        "Get Guidance",
        use_container_width=True
    ):

        if question.strip():

            st.info(
                "The student-support assistant will be "
                "connected here next."
            )

        else:

            st.warning(
                "Please describe what you are struggling with."
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Student Performance Early-Warning System | "
    "Machine Learning + Streamlit"
)
