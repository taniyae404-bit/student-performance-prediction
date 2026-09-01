import streamlit as st

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

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
        st.metric("Risk Probability", "—")

    with col2:
        st.metric("Academic Status", "Not Assessed")

    with col3:
        st.metric("Study Hours", "—")

    with col4:
        st.metric("Sleep", "—")


elif page == "📚 Academic Performance":

    st.title("📚 Academic Performance")

    st.write(
        "Track your test results and monitor your academic progress."
    )

    st.subheader("📝 Enter Your Test Results")

col1, col2 = st.columns(2)

with col1:
    test_1 = st.number_input(
        "Test 1 Marks",
        min_value=0,
        max_value=100,
        value=0
    )

    test_2 = st.number_input(
        "Test 2 Marks",
        min_value=0,
        max_value=100,
        value=0
    )

with col2:
    assignment = st.number_input(
        "Assignment Marks",
        min_value=0,
        max_value=100,
        value=0
    )

    attendance = st.number_input(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=75
    )

if st.button("📊 Analyse Performance", use_container_width=True):

    average_marks = (test_1 + test_2 + assignment) / 3

    st.subheader("📈 Performance Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Marks", f"{average_marks:.1f}%")

    with col2:
        st.metric("Attendance", f"{attendance:.0f}%")

    with col3:
        if average_marks >= 75:
            status = "Good"
        elif average_marks >= 50:
            status = "Needs Improvement"
        else:
            status = "At Risk"

        st.metric("Academic Status", status)

    if average_marks >= 75:
        st.success("🎉 Your academic performance is looking good. Keep maintaining your consistency!")

    elif average_marks >= 50:
        st.warning("📚 Your performance needs some improvement. Consider increasing your revision and practice time.")

    else:
        st.error("⚠️ Your current performance indicates a potential academic risk.")

    if attendance < 75:
        st.warning("📅 Your attendance is below 75%. Improving attendance may help your academic progress.")
    

elif page == "⏱️ Study Tracker":

    st.title("⏱️ Study Tracker")

    st.write(
        "Keep track of your study hours and revision routine."
    )

    st.subheader("📚 Record Your Study Session")

    col1, col2 = st.columns(2)

    with col1:

        study_hours = st.number_input(
            "Study Hours",
            min_value=0.0,
            max_value=24.0,
            value=2.0,
            step=0.5
        )

        subject = st.selectbox(
            "Subject",
            [
                "Mathematics",
                "Science",
                "English",
                "Computer Science",
                "Social Science",
                "Other"
            ]
        )

    with col2:

        revision = st.selectbox(
            "Did you revise today?",
            [
                "Yes",
                "No"
            ]
        )

        study_date = st.date_input(
            "Study Date"
        )

    st.divider()

    if st.button(
        "📊 Save Study Session",
        use_container_width=True
    ):

        st.success(
            f"Study session recorded! "
            f"You studied {study_hours} hours of {subject}."
        )

        st.subheader("📈 Study Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Study Hours",
                f"{study_hours:.1f} hrs"
            )

        with col2:
            st.metric(
                "Subject",
                subject
            )

        with col3:
            st.metric(
                "Revision",
                revision
            )

        if study_hours >= 4:
            st.info(
                "🌟 Great study effort! Keep maintaining a consistent routine."
            )

        elif study_hours >= 2:
            st.info(
                "👍 Good progress! Try to maintain your study routine regularly."
            )

        else:
            st.warning(
                "📚 Consider increasing your study time gradually."
            )

elif page == "😴 Sleep & Routine":

    st.title("😴 Sleep & Routine")

    st.write(
        "Monitor your sleep routine and daily habits."
    )

    st.subheader("🌙 Record Your Sleep")

    col1, col2 = st.columns(2)

    with col1:

        sleep_hours = st.number_input(
            "Sleep Hours",
            min_value=0.0,
            max_value=24.0,
            value=7.0,
            step=0.5
        )

        sleep_quality = st.selectbox(
            "Sleep Quality",
            [
                "Good",
                "Average",
                "Poor"
            ]
        )

    with col2:

        wake_up_time = st.time_input(
            "Wake-up Time"
        )

        sleep_date = st.date_input(
            "Sleep Date"
        )

    st.divider()

    if st.button(
        "💾 Save Sleep Record",
        use_container_width=True
    ):

        st.success(
            f"Sleep record saved! "
            f"You slept for {sleep_hours:.1f} hours."
        )

        st.subheader("📊 Sleep Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Sleep Hours",
                f"{sleep_hours:.1f} hrs"
            )

        with col2:
            st.metric(
                "Sleep Quality",
                sleep_quality
            )

        with col3:
            st.metric(
                "Wake-up Time",
                wake_up_time.strftime("%I:%M %p")
            )

        if sleep_hours >= 7:
            st.info(
                "🌟 Good sleep routine! "
                "Maintaining adequate sleep can support your daily routine."
            )

        elif sleep_hours >= 5:
            st.warning(
                "⚠️ Your sleep duration is a little low. "
                "Try to maintain a more consistent sleep schedule."
            )

        else:
            st.error(
                "🔴 Your sleep duration is quite low. "
                "Consider prioritising adequate rest."
            )


elif page == "💚 Well-being":

    st.title("💚 Well-being")

    st.write(
        "Record simple weekly check-ins about your mood and stress levels."
    )

    st.subheader("🌱 Weekly Well-being Check-in")

    col1, col2 = st.columns(2)

    with col1:

        mood = st.selectbox(
            "How is your mood today?",
            [
                "😊 Very Good",
                "🙂 Good",
                "😐 Okay",
                "🙁 Low",
                "😔 Very Low"
            ]
        )

        stress_level = st.slider(
            "Stress Level",
            min_value=1,
            max_value=10,
            value=5
        )

    with col2:

        energy_level = st.slider(
            "Energy Level",
            min_value=1,
            max_value=10,
            value=5
        )

        checkin_date = st.date_input(
            "Check-in Date"
        )

    st.divider()

    if st.button(
        "💚 Save Check-in",
        use_container_width=True
    ):

        st.success(
            "Your well-being check-in has been recorded."
        )

        st.subheader("📊 Well-being Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Mood",
                mood
            )

        with col2:
            st.metric(
                "Stress Level",
                f"{stress_level}/10"
            )

        with col3:
            st.metric(
                "Energy Level",
                f"{energy_level}/10"
            )

        if stress_level <= 3 and energy_level >= 7:

            st.success(
                "🌟 You seem to be doing well. "
                "Keep maintaining healthy habits and routines."
            )

        elif stress_level <= 6:

            st.info(
                "💙 Your stress level is moderate. "
                "Remember to take breaks and give yourself time to recharge."
            )

        else:

            st.warning(
                "💛 Your stress level seems high. "
                "Consider taking some time to rest, talk to someone you trust, "
                "and focus on activities that help you feel better."
            )

elif page == "🧠 Risk Assessment":

    st.title("🧠 ML Risk Assessment")

    st.write(
        "Enter your academic, family, social and lifestyle information "
        "to estimate your potential academic risk."
    )

    st.info(
        "This prediction is an early-warning indicator and should not "
        "replace teacher, counselor or professional judgment."
    )

    st.subheader("👤 Student Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        sex = st.selectbox(
            "Sex",
            ["F", "M"]
        )

        age = st.number_input(
            "Age",
            min_value=15,
            max_value=25,
            value=17
        )

    with col2:
        address = st.selectbox(
            "Address",
            ["U", "R"]
        )

        famsize = st.selectbox(
            "Family Size",
            ["LE3", "GT3"]
        )

        pstatus = st.selectbox(
            "Parent Cohabitation",
            ["T", "A"]
        )

    with col3:
        guardian = st.selectbox(
            "Guardian",
            ["mother", "father", "other"]
        )

        reason = st.selectbox(
            "Reason for Choosing School",
            ["course", "reputation", "home", "other"]
        )

        nursery = st.selectbox(
            "Attended Nursery School",
            ["yes", "no"]
        )

    st.divider()

    st.subheader("🎓 Academic & Family Factors")

    col1, col2, col3 = st.columns(3)

    with col1:
        medu = st.slider(
            "Mother's Education",
            0, 4, 2
        )

        fedu = st.slider(
            "Father's Education",
            0, 4, 2
        )

        studytime = st.slider(
            "Weekly Study Time",
            1, 4, 2
        )

        failures = st.slider(
            "Past Class Failures",
            0, 4, 0
        )

    with col2:
        mjob = st.selectbox(
            "Mother's Job",
            ["teacher", "health", "services", "at_home", "other"]
        )

        fjob = st.selectbox(
            "Father's Job",
            ["teacher", "health", "services", "at_home", "other"]
        )

        traveltime = st.slider(
            "Travel Time to School",
            1, 4, 2
        )

        famrel = st.slider(
            "Family Relationship Quality",
            1, 5, 4
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
            1, 5, 3
        )

    with col2:
        goout = st.slider(
            "Going Out With Friends",
            1, 5, 3
        )

        Dalc = st.slider(
            "Weekday Alcohol Consumption",
            1, 5, 1
        )

        Walc = st.slider(
            "Weekend Alcohol Consumption",
            1, 5, 1
        )

        health = st.slider(
            "Current Health",
            1, 5, 3
        )

    with col3:
        absences = st.number_input(
            "School Absences",
            min_value=0,
            max_value=100,
            value=4
        )

        st.write("")
        st.write("")
        st.write("")
        st.write(
            "💡 These inputs correspond to factors used "
            "by the trained ML model."
        )

    st.divider()

    if st.button(
        "🔍 Assess Academic Risk",
        use_container_width=True
    ):

        try:

            model = joblib.load(
                "student_performance_model.pkl"
            )

            student_data = pd.DataFrame([{
                "school": school,
                "sex": sex,
                "age": age,
                "address": address,
                "famsize": famsize,
                "Pstatus": pstatus,
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

            at_risk_index = list(class_names).index(
                "At Risk"
            )

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
                "❌ student_performance_model.pkl "
                "was not found. Make sure the model file "
                "is in the same GitHub repository as app.py."
            )

        except Exception as e:

            st.error(
                f"⚠️ Prediction error: {e}"
            )

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

    if st.button("Get Guidance", use_container_width=True):

        if question.strip():

            st.info(
                "The student-support assistant will be connected here next."
            )

        else:

            st.warning(
                "Please describe what you are struggling with."
            )


st.divider()

st.caption(
    "Student Performance Early-Warning System | "
    "Machine Learning + Streamlit"
)
