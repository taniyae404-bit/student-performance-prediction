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

    st.info("Academic tracking will be added in the next step.")


elif page == "⏱️ Study Tracker":

    st.title("⏱️ Study Tracker")

    st.write(
        "Keep track of your study hours and revision routine."
    )

    st.info("Study tracking will be added in the next step.")


elif page == "😴 Sleep & Routine":

    st.title("😴 Sleep & Routine")

    st.write(
        "Monitor your sleep routine and daily habits."
    )

    st.info("Sleep and routine tracking will be added in the next step.")


elif page == "💚 Well-being":

    st.title("💚 Well-being")

    st.write(
        "Record simple weekly check-ins about your mood and stress levels."
    )

    st.info("Well-being tracking will be added in the next step.")


elif page == "🧠 Risk Assessment":

    st.title("🧠 ML Risk Assessment")

    st.write(
        "The machine-learning model estimates whether a student "
        "may be potentially at risk of poor academic performance."
    )

    st.info(
        "The revised Logistic Regression model will be connected here next."
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
