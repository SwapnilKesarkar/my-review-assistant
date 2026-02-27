import streamlit as st
import random
import streamlit.components.v1 as components

# ==============================
# CONFIG
# ==============================

GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review"

st.set_page_config(
    page_title="Review SK Photo Studio",
    page_icon="⭐",
    layout="centered"
)

# ==============================
# SIMPLE MOBILE STYLE
# ==============================

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    max-width: 420px;
}

h1 {
    text-align: center;
}

.stButton>button {
    width: 100%;
    height: 3em;
    border-radius: 8px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# REVIEW GENERATOR
# ==============================

def generate_review():

    openings = [
        "Amazing experience!",
        "Loved the service!",
        "Great studio!",
        "Very professional team!",
        "Highly impressed!"
    ]

    middle = [
        "The team was friendly and supportive.",
        "Everything was handled smoothly.",
        "The photos turned out beautiful.",
        "Creative work and quick delivery.",
        "Very happy with the results."
    ]

    closings = [
        "Highly recommended!",
        "Will definitely visit again.",
        "Five stars!",
        "Great overall experience.",
        "Absolutely worth it!"
    ]

    return f"{random.choice(openings)} {random.choice(middle)} {random.choice(closings)}"

# ==============================
# INIT SESSION STATE
# ==============================

if "review_text" not in st.session_state:
    st.session_state.review_text = generate_review()

# ==============================
# TITLE
# ==============================

st.title("⭐ Review SK Photo Studio")
st.divider()

# ==============================
# CHANGE BUTTON (GENERATE NEW UNIQUE REVIEW)
# ==============================

if st.button("🔄 Change Review"):

    new_review = generate_review()

    # Ensure new review is different
    while new_review == st.session_state.review_text:
        new_review = generate_review()

    st.session_state.review_text = new_review

# ==============================
# DIRECT EDITOR (USES SESSION VALUE DIRECTLY)
# ==============================

review_text = st.text_area(
    "Your Review:",
    value=st.session_state.review_text,
    height=120
)

# Update session state if user edits
st.session_state.review_text = review_text

# ==============================
# COPY BUTTON (REAL COPY)
# ==============================

copy_script = f"""
<script>
function copyText() {{
    const text = `{st.session_state.review_text}`;
    navigator.clipboard.writeText(text);
    alert("Review copied!");
}}
</script>
<button onclick="copyText()" 
style="width:100%;height:3em;border-radius:8px;font-size:16px;">
📋 Copy Review
</button>
"""

components.html(copy_script, height=70)

# ==============================
# POST BUTTON
# ==============================

st.link_button("🚀 Post on Google", GOOGLE_MAPS_LINK)
