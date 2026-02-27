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
# STYLE
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
    border-radius: 8px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# SENTENCE POOLS
# ==============================

openings = [
    "Amazing experience at SK Photo Studio.",
    "Had a wonderful time at the studio.",
    "Truly impressed with the service.",
    "It was such a great experience.",
    "Highly satisfied with my visit.",
    "Fantastic team and atmosphere.",
    "Very professional setup.",
    "Absolutely loved my photoshoot."
]

middles = [
    "The team was extremely friendly.",
    "Everything was handled smoothly.",
    "The photographers were very creative.",
    "The lighting setup was excellent.",
    "Delivery was quick and hassle-free.",
    "They guided us throughout the shoot.",
    "Very cooperative and supportive staff.",
    "The editing quality was top-notch.",
    "The entire process felt premium.",
    "Great attention to detail."
]

highlights = [
    "The photos turned out beautiful.",
    "The final results exceeded expectations.",
    "The creativity really stood out.",
    "Every shot looked amazing.",
    "Loved the professionalism.",
    "The studio ambiance was great.",
    "The quality was outstanding.",
    "Very happy with the outcome."
]

closings = [
    "Highly recommended!",
    "Would definitely visit again.",
    "Five stars from me.",
    "Great overall experience.",
    "Absolutely worth it.",
    "Looking forward to next session.",
    "Totally satisfied.",
    "Thanks to the amazing team."
]

# ==============================
# REVIEW GENERATOR (2–5 LINES)
# ==============================

def generate_review(previous=None):

    while True:
        lines = []

        # Always start with opening
        lines.append(random.choice(openings))

        # Add 1–3 middle/highlight lines randomly
        extra_lines_count = random.randint(1, 3)

        pool = middles + highlights
        lines.extend(random.sample(pool, extra_lines_count))

        # Add closing
        lines.append(random.choice(closings))

        review = "\n".join(lines)

        # Ensure new review is different
        if review != previous:
            return review

# ==============================
# INIT
# ==============================

if "review_text" not in st.session_state:
    st.session_state.review_text = generate_review()

# ==============================
# TITLE
# ==============================

st.title("⭐ Review SK Photo Studio")
st.divider()

# ==============================
# CHANGE BUTTON
# ==============================

if st.button("🔄 Change Review"):
    st.session_state.review_text = generate_review(
        st.session_state.review_text
    )

# ==============================
# EDITOR
# ==============================

review_text = st.text_area(
    "Your Review:",
    value=st.session_state.review_text,
    height=150
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
style="width:100%;height:3em;border-radius:8px;font-size:16px;">
📋 Copy Review
</button>
"""

components.html(copy_script, height=70)

# ==============================
# POST BUTTON
# ==============================

st.link_button("🚀 Post on Google", GOOGLE_MAPS_LINK)

# ==============================
# UNIQUE COUNT INFO
# ==============================

unique_count = (
    len(openings)
    * (len(middles) + len(highlights)) ** 3
    * len(closings)
)

st.caption(f"💡 Possible unique combinations: 20,000+")
