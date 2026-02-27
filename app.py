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
# HUMAN STYLE SENTENCE POOLS
# ==============================

openings = [
    "Absolutely loved my experience here 😍",
    "Had such a wonderful time at SK Photo Studio 📸",
    "From start to finish, everything was perfect ✨",
    "So happy I chose this studio ❤️",
    "What an amazing photoshoot experience! 🎉",
    "Truly impressed with the professionalism 🙌",
    "It was such a smooth and enjoyable session 😊",
    "I couldn’t be happier with the results 💯"
]

experience_lines = [
    "The team made me feel completely comfortable.",
    "They guided us patiently throughout the shoot.",
    "The attention to detail really stood out.",
    "Lighting and setup were handled beautifully.",
    "The entire process felt premium and organized.",
    "The creativity during the shoot was amazing.",
    "Everything was managed so smoothly.",
    "Their friendly approach made it even better.",
    "The editing quality exceeded expectations.",
    "Delivery was faster than I expected."
]

emotional_lines = [
    "You can truly see the passion in their work 💖",
    "Every shot captured our special moments perfectly 📷",
    "They really know how to bring out your best look 🌟",
    "The final photos made us so emotional 🥹",
    "Such positive energy throughout the session ✨",
    "It felt more like fun than a formal shoot 😄",
    "They paid attention to even the smallest details 👌",
    "The results honestly surprised me in the best way!"
]

closings = [
    "Highly recommended! ⭐⭐⭐⭐⭐",
    "Would definitely visit again! 💫",
    "Five stars without a doubt ⭐",
    "Totally worth it! 👍",
    "Can’t wait for my next shoot here! 😍",
    "Big thanks to the amazing team! 🙏",
    "Absolutely satisfied with everything! 💕",
    "If you’re thinking about booking, just do it! 😉"
]

# ==============================
# GENERATOR (2–5 HUMAN LINES)
# ==============================

def generate_review(previous=None):

    while True:
        lines = []

        # Opening
        lines.append(random.choice(openings))

        # Random number of middle lines (1–3)
        middle_count = random.randint(1, 3)

        combined_pool = experience_lines + emotional_lines
        middle_lines = random.sample(combined_pool, middle_count)

        lines.extend(middle_lines)

        # Closing
        lines.append(random.choice(closings))

        review = "\n\n".join(lines)

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
    height=220
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

# ==============================
# UNIQUE COUNT ESTIMATE
# ==============================

approx_unique = len(openings) * (len(experience_lines) + len(emotional_lines))**3 * len(closings)

st.caption("💡 Thousands of unique human-style combinations possible.")
