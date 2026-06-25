import streamlit as st
import pickle
import numpy as np

# ---------------------
# PAGE CONFIG
# ---------------------

st.set_page_config(
    page_title="PhysIQ",
    page_icon="🔬",
    layout="centered"
)

# ---------------------
# CSS
# ---------------------

def load_css():
    with open("styles.css", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------------
# MODEL
# ---------------------

model = pickle.load(open("model.pkl", "rb")
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------------
# CHAPTER ICONS
# ---------------------

icons = {
    "UNIT 10: HEAT CAPACITY AND MODES OF HEAT TRANSFER": "🔥",
    "UNIT 11: THERMAL EXPANSION AND CHANGE OF STATE": "🌡️",
    "UNIT 12: WAVES": "🌊",
    "UNIT 13: SOUND": "🔊",
    "UNIT 14: OPTICS": "🔭",
    "UNIT 15: ELECTROSTATICS": "⚡",
    "UNIT 16: CURRENT ELECTRICITY": "🔌",
    "UNIT 17: ELECTRIC CIRCUITS": "🔋",
    "UNIT 18: ELECTRONICS": "💻",
    "UNIT 19: ELECTROMAGNETISM": "🧲",
    "UNIT 20: ELECTROMAGNETIC WAVES": "📡",
    "UNIT 21: NUCLEAR PHYSICS": "☢️"
}

chapters = list(icons.keys())

# ---------------------
# HEADER
# ---------------------

st.title("🔬 PhysIQ")

st.caption(
    "AI-powered classification of FBISE Physics questions"
)

# ---------------------
# METRICS
# ---------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Questions", "1497")

with col2:
    st.metric("Chapters", "12")

with col3:
    st.metric("Accuracy", "87%")

st.divider()

# ---------------------
# INPUT
# ---------------------

question = st.text_area(
    "Physics Question",
    placeholder="e.g "Compare longitudinal and transverse waves"
)

# ---------------------
# PREDICT
# ---------------------

if st.button("Classify Question"):

    if question.strip():

        vec = vectorizer.transform([question])

        prediction = model.predict(vec)[0]

        try:
            score = model.decision_function(vec)

            confidence = float(np.max(score))

            confidence_pct = min(
                max(confidence * 10, 0),
                100
            )

        except:
            confidence_pct = 0

        icon = icons.get(prediction, "📘")

        st.markdown(
            f"""
            <div class="result-card">
                <h4>Predicted Chapter</h4>
                <h2>{icon} {prediction}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(confidence_pct / 100)

        st.write(
            f"Confidence: {confidence_pct:.1f}%"
        )

    else:
        st.warning(
            "Please enter a question."
        )

# ---------------------
# CHAPTERS
# ---------------------

st.divider()

st.subheader("Available Chapters")

for chapter in chapters:
    st.markdown(
        f"""
        <span class="chapter-badge">
            {icons[chapter]} {chapter}
        </span>
        """,
        unsafe_allow_html=True
    )

# ---------------------
# FOOTER
# ---------------------

st.markdown(
    """
    <div class="footer">
        Built with Scikit-Learn + Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
