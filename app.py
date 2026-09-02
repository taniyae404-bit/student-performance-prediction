import streamlit as st
import pandas as pd
import joblib
from google import genai
st.set_page_config(page_title="Student Performance AI", page_icon="🎓", layout="wide")

st.markdown("""
<style>

/* ===== APP BACKGROUND ===== */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f5f7ff 0%, #eef6ff 50%, #f8f9ff 100%);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1e293b 100%);
}

[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

[data-testid="stSidebar"] .stRadio label {
    border-radius: 10px;
    padding: 8px 10px;
    transition: 0.2s ease;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.10);
}

/* ===== HERO CARD ===== */
.hero-card {
    padding: 34px;
    border-radius: 26px;
    margin-bottom: 30px;
    background: linear-gradient(135deg, #dbeafe 0%, #ede9fe 55%, #f0fdfa 100%);
    border: 1px solid rgba(148,163,184,0.25);
    box-shadow: 0 12px 35px rgba(30,41,59,0.08);
}

.hero-content {
    display: flex;
    align-items: center;
    gap: 24px;
}

.hero-icon {
    font-size: 58px;
    background: white;
    width: 85px;
    height: 85px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 22px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}

.hero-card h1 {
    margin: 0;
    font-size: 40px;
    font-weight: 750;
    color: #172554;
}

.hero-card p {
    margin-top: 10px;
    font-size: 17px;
    color: #475569;
    line-height: 1.6;
}

/* ===== HEADINGS ===== */
h1, h2, h3 {
    color: #172554;
}

[data-testid="stSubheader"] {
    color: #1e3a8a;
}

/* ===== METRIC CARDS ===== */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.88);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #dbe4f0;
    box-shadow: 0 8px 25px rgba(15,23,42,0.06);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(37,99,235,0.12);
}

[data-testid="stMetricLabel"] {
    color: #64748b !important;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #172554 !important;
    font-weight: 750;
}

/* ===== GENERAL CARDS ===== */
.small-card {
    padding: 24px;
    border-radius: 20px;
    background: rgba(255,255,255,0.9);
    border: 1px solid #e2e8f0;
    min-height: 175px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
    transition: 0.2s ease;
}

.small-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(37,99,235,0.10);
}

.small-card h3 {
    color: #1e3a8a;
    margin-bottom: 8px;
}

.small-card p {
    color: #64748b;
    line-height: 1.6;
}

/* ===== BUTTONS ===== */
.stButton > button {
    border-radius: 14px;
    min-height: 48px;
    font-weight: 700;
    border: none;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    box-shadow: 0 7px 18px rgba(37,99,235,0.20);
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(124,58,237,0.25);
}

/* ===== INPUTS ===== */
[data-baseweb="input"],
[data-baseweb="select"],
[data-baseweb="textarea"] {
    border-radius: 12px;
}

input {
    border-radius: 12px !important;
}

/* ===== INFO / SUCCESS / WARNING BOXES ===== */
[data-testid="stAlert"] {
    border-radius: 16px;
    border: none;
}

/* ===== DIVIDERS ===== */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        #cbd5e1,
        transparent
    );
    margin: 28px 0;
}

/* ===== PROGRESS BAR ===== */
[data-testid="stProgressBar"] > div > div {
    border-radius: 20px;
}

/* ===== FOOTER ===== */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)
# Google OAuth: add [auth] redirect_uri/client_id/client_secret/cookie_secret
# and [auth.google] client_id/client_secret in Streamlit secrets as required by your setup.
google_auth_enabled = False
try:
    google_auth_enabled = "auth" in st.secrets
except Exception:
    pass

if google_auth_enabled and not st.user.is_logged_in:
    st.markdown("""
    <div class="hero-card"><div class="hero-content"><div class="hero-icon">🎓</div><div>
    <h1>Student Performance AI</h1><p>Sign in with Google to access your personalised student dashboard.</p>
    </div></div></div>
    """, unsafe_allow_html=True)
    if st.button("🔐 Continue with Google", use_container_width=True):
        st.login("google")
    st.stop()

# Session state
defaults = {
    "average_marks": None, "attendance": None, "risk_probability": None,
    "risk_status": "Not Assessed", "study_hours": None, "sleep_hours": None,
    "mood": None, "stress": None,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Sidebar
st.sidebar.markdown("## 🎓 Student Performance AI")
st.sidebar.caption("Machine Learning Early-Warning System")
if google_auth_enabled and st.user.is_logged_in:
    name = getattr(st.user, "name", None) or getattr(st.user, "email", "Student")
    st.sidebar.success(f"Welcome, {name}")
    if st.sidebar.button("Log out", use_container_width=True): st.logout()
page = st.sidebar.radio("Navigate", ["🏠 Dashboard","📚 Academic Performance","⏱️ Study Tracker","😴 Sleep & Routine","💚 Well-being","🧠 Risk Assessment","💬 Ask Student AI"])
st.sidebar.divider(); st.sidebar.caption("Developed by Alishba Ejaz"); st.sidebar.caption("Machine Learning + Streamlit")

# Dashboard
if page == "🏠 Dashboard":
    st.markdown("""
    <div class="hero-card"><div class="hero-content"><div class="hero-icon">🎓</div><div>
    <h1>Student Performance AI</h1><p>Your personal academic companion for tracking performance, building better habits and identifying potential academic challenges early.</p>
    </div></div></div>""", unsafe_allow_html=True)
    st.subheader("📊 Student Overview")
    c1,c2,c3,c4=st.columns(4)
    with c1: st.metric("🧠 Risk Probability", f"{st.session_state.risk_probability:.1%}" if st.session_state.risk_probability is not None else "—")
    with c2: st.metric("📌 Academic Status", st.session_state.risk_status)
    with c3: st.metric("📚 Study Hours", f"{st.session_state.study_hours:.1f} hrs" if st.session_state.study_hours is not None else "—")
    with c4: st.metric("😴 Sleep", f"{st.session_state.sleep_hours:.1f} hrs" if st.session_state.sleep_hours is not None else "—")
    st.divider(); st.subheader("📚 Academic Snapshot")
    if st.session_state.average_marks is not None:
        c1,c2=st.columns(2)
        with c1:
            st.metric("Average Marks",f"{st.session_state.average_marks:.1f}/100")
            if st.session_state.average_marks>=75: st.success("🌟 Excellent performance!")
            elif st.session_state.average_marks>=50: st.info("👍 Your performance is satisfactory.")
            else: st.warning("⚠️ This area may need more attention.")
        with c2:
            st.metric("Attendance",f"{st.session_state.attendance:.0f}%")
            if st.session_state.attendance>=75: st.success("✅ Attendance is looking good.")
            else: st.warning("⚠️ Consider improving attendance.")
    else: st.info("📌 Complete the Academic Performance section to see your academic snapshot.")
    st.divider(); st.subheader("🚀 Quick Actions")
    c1,c2,c3=st.columns(3)
    cards=[("📚 Academic Performance","Record your marks and attendance and keep track of your academic progress."),("🧠 Risk Assessment","Use machine learning to identify potential academic risk early."),("💬 Ask Student AI","Get practical guidance for common academic challenges.")]
    for col,(title,txt) in zip((c1,c2,c3),cards):
        with col: st.markdown(f'<div class="small-card"><h3>{title}</h3><p>{txt}</p></div>',unsafe_allow_html=True)
    st.divider(); st.subheader("🌱 Your Student Journey")
    c1,c2=st.columns(2)
    with c1: st.markdown('<div class="small-card"><h3>📈 Track Your Progress</h3><p>Monitor marks, attendance and study habits to understand your academic journey.</p><br><h3>🎯 Set Better Goals</h3><p>Focus on small, realistic improvements instead of trying to change everything at once.</p></div>',unsafe_allow_html=True)
    with c2: st.markdown('<div class="small-card"><h3>🌙 Take Care of Yourself</h3><p>Sleep, routine and well-being can all influence how effectively you study.</p><br><h3>💬 Ask for Guidance</h3><p>When something feels difficult, use Student AI or speak with someone you trust.</p></div>',unsafe_allow_html=True)
    st.divider(); st.subheader("💡 Student Tip")
    if st.session_state.average_marks is None: st.info("🎯 Start by entering your marks and attendance in Academic Performance.")
    elif st.session_state.average_marks<50: st.warning("📚 Focus on the subjects where you are struggling most and practise them regularly.")
    elif st.session_state.study_hours is not None and st.session_state.study_hours<2: st.info("⏱️ Try adding a short focused study session to your daily routine.")
    elif st.session_state.sleep_hours is not None and st.session_state.sleep_hours<6: st.info("😴 Your sleep routine may need attention. Try to maintain a consistent sleep schedule.")
    else: st.success("🌟 Keep going! Consistency is one of the most important parts of academic progress.")

# Academic
elif page == "📚 Academic Performance":
    st.title("📚 Academic Performance"); st.write("Record your marks and attendance to understand your current academic performance."); st.divider(); st.subheader("📝 Test Performance")
    c1,c2,c3=st.columns(3)
    with c1: test1=st.number_input("Test 1 Marks",min_value=0,max_value=100,value=0,step=1)
    with c2: assignment=st.number_input("Assignment Marks",min_value=0,max_value=100,value=0,step=1)
    with c3: test2=st.number_input("Test 2 Marks",min_value=0,max_value=100,value=0,step=1)
    attendance=st.number_input("Attendance Percentage",min_value=0,max_value=100,value=0,step=1)
    st.divider()
    if st.button("📊 Analyze Performance",use_container_width=True):
        avg=(test1+assignment+test2)/3; st.session_state.average_marks=avg; st.session_state.attendance=attendance
        st.subheader("📈 Performance Summary"); c1,c2=st.columns(2)
        with c1: st.metric("Average Marks",f"{avg:.1f}/100")
        with c2: st.metric("Attendance",f"{attendance:.0f}%")
        if avg>=75: st.success("🌟 Excellent academic performance!")
        elif avg>=50: st.info("👍 Your performance is satisfactory. Keep working consistently.")
        else: st.warning("⚠️ Your marks may need additional attention.")

# Study
elif page == "⏱️ Study Tracker":
    st.title("⏱️ Study Tracker"); st.write("Keep track of your daily study hours and revision routine."); st.divider(); st.subheader("📚 Today's Study")
    c1,c2=st.columns(2)
    with c1: study=st.number_input("Study Hours",min_value=0.0,max_value=24.0,value=0.0,step=0.5)
    with c2: revision=st.selectbox("Did you revise today?",["Yes","No"])
    st.divider()
    if st.button("💾 Save Study Record",use_container_width=True):
        st.session_state.study_hours=study; st.success(f"✅ Study record saved: {study:.1f} hours.")
        st.info("📖 Great job! You kept up with revision today." if revision=="Yes" else "💡 Consider setting aside a little time for revision.")

# Sleep
elif page == "😴 Sleep & Routine":
    st.title("😴 Sleep & Routine"); st.write("Monitor your sleep routine and daily habits."); st.divider(); st.subheader("🌙 Sleep Information")
    sleep=st.number_input("Hours of Sleep",min_value=0.0,max_value=24.0,value=7.0,step=0.5)
    quality=st.slider("Sleep Quality",1,5,3,help="1 = Very poor, 5 = Excellent")
    st.divider()
    if st.button("💾 Save Sleep Record",use_container_width=True):
        st.session_state.sleep_hours=sleep; st.success("✅ Sleep information recorded."); c1,c2=st.columns(2)
        with c1: st.metric("Sleep",f"{sleep:.1f} hours")
        with c2: st.metric("Sleep Quality",f"{quality}/5")

# Well-being
elif page == "💚 Well-being":
    st.title("💚 Well-being"); st.write("Use a simple check-in to reflect on your mood and current stress level."); st.divider(); st.subheader("🌱 Weekly Check-in")
    c1,c2=st.columns(2)
    with c1: mood=st.slider("How are you feeling today?",1,5,3,help="1 = Very low, 5 = Very good")
    with c2: stress=st.slider("Current Stress Level",1,5,3,help="1 = Very low, 5 = Very high")
    st.divider()
    if st.button("💚 Save Check-in",use_container_width=True):
        st.session_state.mood=mood; st.session_state.stress=stress; st.success("💚 Your check-in has been recorded."); c1,c2=st.columns(2)
        with c1: st.metric("Mood",f"{mood}/5")
        with c2: st.metric("Stress",f"{stress}/5")
        if stress>=4: st.warning("🌿 Your stress level is high. Consider taking a break and talking to someone you trust.")
        else: st.info("🌱 Keep taking care of yourself and maintain a balanced routine.")

# Risk
elif page == "🧠 Risk Assessment":
    st.title("🧠 ML Risk Assessment"); st.write("Enter your academic, family, social and lifestyle information to estimate your potential academic risk."); st.info("This prediction is an early-warning indicator and should not replace teacher, counselor or professional judgment.")
    st.subheader("👤 Student Information"); c1,c2,c3=st.columns(3)
    with c1:
        sex_label=st.selectbox("Gender",["Female","Male"]); sex="F" if sex_label=="Female" else "M"; age=st.number_input("Age",15,25,17)
    with c2:
        address_label=st.selectbox("Area of Residence",["Urban","Rural"]); address="U" if address_label=="Urban" else "R"; fam_label=st.selectbox("Family Size",["3 or fewer members","More than 3 members"]); famsize="LE3" if fam_label=="3 or fewer members" else "GT3"; p_label=st.selectbox("Parents' Living Arrangement",["Living together","Living separately"]); pstatus="T" if p_label=="Living together" else "A"
    with c3:
        guardian_label=st.selectbox("Guardian",["Mother","Father","Other"]); guardian=guardian_label.lower(); reason_label=st.selectbox("Main Reason for Choosing School",["Course","School reputation","Close to home","Other"]); reason={"Course":"course","School reputation":"reputation","Close to home":"home","Other":"other"}[reason_label]; nursery_label=st.selectbox("Attended Nursery School",["Yes","No"]); nursery=nursery_label.lower()
    st.divider(); st.subheader("🎓 Academic & Family Factors"); c1,c2,c3=st.columns(3)
    with c1: medu=st.slider("Mother's Education",0,4,2); fedu=st.slider("Father's Education",0,4,2); studytime=st.slider("Weekly Study Time",1,4,2); failures=st.slider("Past Class Failures",0,4,0)
    with c2: mjob=st.selectbox("Mother's Job",["teacher","health","services","at_home","other"]); fjob=st.selectbox("Father's Job",["teacher","health","services","at_home","other"]); traveltime=st.slider("Travel Time to School",1,4,2); famrel=st.slider("Family Relationship Quality",1,5,4)
    with c3: schoolsup=st.selectbox("Extra School Support",["yes","no"]); famsup=st.selectbox("Family Educational Support",["yes","no"]); paid=st.selectbox("Extra Paid Classes",["yes","no"]); higher=st.selectbox("Wants Higher Education",["yes","no"])
    st.divider(); st.subheader("🌱 Social & Lifestyle Factors"); c1,c2,c3=st.columns(3)
    with c1: activities=st.selectbox("Extracurricular Activities",["yes","no"]); internet=st.selectbox("Internet Access",["yes","no"]); freetime=st.slider("Free Time After School",1,5,3)
    with c2: goout=st.slider("Going Out With Friends",1,5,3); health=st.slider("Current Health",1,5,3)
    with c3: absences = st.number_input("School Absences", 0, 100, 4)
    st.divider(); st.subheader("🤖 Academic Risk Prediction")
    if st.button("🔍 Assess Academic Risk",use_container_width=True):
        try:
            model=joblib.load("student_performance_model.pkl")
            # Hidden legacy fields keep compatibility with the original trained model.
            data=pd.DataFrame([{"school":"GP","sex":sex,"age":age,"address":address,"famsize":famsize,"Pstatus":pstatus,"Medu":medu,"Fedu":fedu,"Mjob":mjob,"Fjob":fjob,"reason":reason,"guardian":guardian,"traveltime":traveltime,"studytime":studytime,"failures":failures,"schoolsup":schoolsup,"famsup":famsup,"paid":paid,"activities":activities,"nursery":nursery,"higher":higher,"internet":internet,"romantic":"no","famrel":famrel,"freetime":freetime,"goout":goout,"Dalc":1,"Walc":1,"health":health,"absences":absences}])
            probs=model.predict_proba(data); classes=list(model.classes_)
            if "At Risk" not in classes: st.error("The model does not contain an 'At Risk' class. Please check the trained model.")
            else:
                risk=float(probs[0,classes.index("At Risk")]); threshold=.40; status="Potentially At Risk" if risk>=threshold else "Not At Risk"; st.session_state.risk_probability=risk; st.session_state.risk_status=status
                (st.error if risk>=threshold else st.success)(f"{'⚠️' if risk>=threshold else '✅'} {status}")
                st.subheader("📊 Prediction Results"); c1,c2,c3=st.columns(3)
                with c1: st.metric("Risk Probability",f"{risk:.1%}")
                with c2: st.metric("Status",status)
                with c3: st.metric("Decision Threshold",f"{threshold:.0%}")
                st.progress(risk)
                if risk>=threshold: st.warning("The model estimates that this student may benefit from additional academic attention and support.")
                else: st.info("The model does not currently flag this student as potentially at risk.")
                st.caption("Model: Logistic Regression | Risk threshold: 0.40")
        except FileNotFoundError: st.error("❌ student_performance_model.pkl was not found. Make sure the model file is in the same GitHub repository as app.py.")
        except Exception as e: st.error(f"⚠️ Prediction error: {e}")

# ============================================================
# ASK STUDENT AI
# ============================================================

elif page == "💬 Ask Student AI":

    st.title("💬 Ask Student AI")

    st.write(
        "Ask questions about your studies, exams, "
        "time management, attendance and student well-being."
    )

    st.info(
        "💡 Student AI provides general academic guidance. "
        "For serious personal, mental-health or safety concerns, "
        "please speak with a trusted adult or qualified professional."
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
        "Ask Student AI",
        placeholder=(
            "Example: I am studying regularly but my "
            "marks are still not improving. What should I do?"
        ),
        height=150
    )

    if st.button(
        "🤖 Ask Student AI",
        use_container_width=True
    ):

        if not question.strip():

            st.warning(
                "Please enter a question first."
            )

        else:

                client = genai.Client(
                         api_key=st.secrets["GEMINI_API_KEY"]
                )

              response = client.models.generate_content(
              model="gemini-3.6-flash",
              contents=(
            "You are Student AI, an academic support assistant "
            "inside a student performance early-warning application. "
            "Give clear, practical and encouraging answers to students. "
            "Focus on academic performance, study habits, exam preparation, "
            "attendance, motivation and general student well-being. "
            "Do not claim to diagnose mental-health conditions. "
            "If a student describes a serious safety or mental-health "
            "situation, encourage them to contact a trusted person or "
            "qualified professional.\n\n"
            f"Student selected topic: {topic}\n\n"
            f"Student question: {question}"
        )
    )

    st.subheader("💡 Student AI Response")
    st.write(response.text)

    
st.divider(); st.caption("Student Performance Early-Warning System | Machine Learning + Streamlit")
