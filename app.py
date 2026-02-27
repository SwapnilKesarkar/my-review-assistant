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
h1 { text-align: center; }
.stButton>button {
    width: 100%;
    height: 3em;
    border-radius: 10px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# HUMAN SENTENCE POOLS
# ==============================

openings = [
    "Absolutely loved my experience here 😍",
    "Had such a wonderful time at SK Photo Studio 📸",
    "From start to finish, everything was perfect ✨",
    "So happy I chose this studio ❤️",
    "What an amazing photoshoot experience! 🎉",
    "Truly impressed with the professionalism 🙌"
]

experience_lines = [
    "The team made me feel completely comfortable and confident.",
    "They guided us patiently throughout the entire shoot.",
    "The attention to detail really stood out.",
    "The lighting and setup were handled beautifully.",
    "Everything was managed so smoothly from beginning to end.",
    "The editing quality exceeded my expectations."
]

emotional_lines = [
    "You can truly see the passion in their work 💖",
    "Every shot captured our special moments perfectly 📷",
    "They really know how to bring out your best look 🌟",
    "The final photos honestly surprised me in the best way!",
    "Such positive energy throughout the entire session ✨",
    "It felt more like fun than a formal shoot 😄"
]

closings = [
    "Highly recommended! ⭐⭐⭐⭐⭐",
    "Would definitely visit again! 💫",
    "Five stars without a doubt ⭐",
    "Totally worth it! 👍",
    "Big thanks to the amazing team! 🙏"
]

# ==============================
# PARAGRAPH GENERATOR
# ==============================

def generate_review(previous=None):
    while True:
        opening = random.choice(openings)

        # choose 2–3 middle sentences
        middle_pool = experience_lines + emotional_lines
        middle_count = random.randint(2, 3)
        middle_sentences = random.sample(middle_pool, middle_count)

        closing = random.choice(closings)

        review = " ".join([opening] + middle_sentences + [closing])

        if review != previous:
            return review

# ==============================
# INIT
# ==============================

if "review_text" not in st.session_state:
    st.session_state.review_text = generate_review()

# ==============================
# UI
# ==============================

st.title("⭐ Review SK Photo Studio")
st.divider()

if st.button("🔄 Change Review"):
    st.session_state.review_text = generate_review(
        st.session_state.review_text
    )

review_text = st.text_area(
    "Your Review:",
    value=st.session_state.review_text,
    height=180
)

st.session_state.review_text = review_text

# ==============================
# COPY BUTTON
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
style="width:100%;height:3em;border-radius:10px;font-size:16px;">
📋 Copy Review
</button>
"""

components.html(copy_script, height=70)

st.link_button("🚀 Post on Google", GOOGLE_MAPS_LINK)

st.caption("💡 Generates thousands of natural human-style variations.")
