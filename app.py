# ============================================================
# ACADEMIC PERFORMANCE
# ============================================================

elif page == "📚 Academic Performance":

    st.title("📚 Academic Performance")

    st.write(
        "Record your recent academic performance and "
        "identify subjects that may need more attention."
    )

    st.divider()

    # --------------------------------------------------------
    # SUBJECT PERFORMANCE
    # --------------------------------------------------------

    st.subheader("📝 Enter Your Performance")

    col1, col2 = st.columns(2)

    with col1:
        subject = st.selectbox(
            "Select Subject",
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
        assessment = st.text_input(
            "Assessment / Exam Name",
            placeholder="e.g. Unit Test 1"
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        marks_obtained = st.number_input(
            "Marks Obtained",
            min_value=0.0,
            step=1.0
        )

    with col2:
        total_marks = st.number_input(
            "Total Marks",
            min_value=1.0,
            value=100.0,
            step=1.0
        )

    with col3:
        target_percentage = st.number_input(
            "Target Percentage",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=1.0
        )

    # --------------------------------------------------------
    # CALCULATE PERFORMANCE
    # --------------------------------------------------------

    if st.button(
        "📊 Analyse Performance",
        use_container_width=True
    ):

        percentage = (
            marks_obtained / total_marks
        ) * 100

        st.divider()

        st.subheader("📈 Performance Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Percentage",
                f"{percentage:.1f}%"
            )

        with col2:
            st.metric(
                "Target",
                f"{target_percentage:.1f}%"
            )

        with col3:
            difference = percentage - target_percentage

            st.metric(
                "Difference",
                f"{difference:+.1f}%"
            )

        st.progress(
            min(percentage / 100, 1.0)
        )

        # ----------------------------------------------------
        # PERSONALIZED FEEDBACK
        # ----------------------------------------------------

        if percentage >= target_percentage:

            st.success(
                f"🎉 Good work! Your performance in "
                f"**{subject}** is meeting your target."
            )

            st.write(
                "Keep revising regularly and maintain "
                "your current study routine."
            )

        elif percentage >= 50:

            st.warning(
                f"⚠️ Your performance in **{subject}** "
                f"is below your target."
            )

            st.write(
                "Consider revising the chapters where "
                "you are making mistakes and practising "
                "more questions."
            )

        else:

            st.error(
                f"🔴 **{subject}** may need additional attention."
            )

            st.write(
                "Try identifying the topics you find difficult, "
                "revise the relevant chapters, and practise "
                "questions regularly."
            )

        # ----------------------------------------------------
        # SAVE SESSION INFORMATION
        # ----------------------------------------------------

        st.info(
            "💡 This performance information can be used "
            "alongside your study routine and AI guidance "
            "to help identify areas that need attention."
        )

    st.divider()

    # --------------------------------------------------------
    # PERFORMANCE TIPS
    # --------------------------------------------------------

    st.subheader("💡 Academic Tips")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "📖 **Revise Weak Topics**\n\n"
            "Focus on chapters where your performance "
            "is consistently lower."
        )

    with col2:
        st.info(
            "✏️ **Practise Questions**\n\n"
            "Regular practice can help improve "
            "understanding and accuracy."
        )

    with col3:
        st.info(
            "📅 **Track Progress**\n\n"
            "Compare your results over time instead "
            "of focusing on a single test."
        )
