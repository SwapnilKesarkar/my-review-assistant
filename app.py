import streamlit as st
import random

# ==============================
# 1. CONFIGURATION
# ==============================

GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review"
STUDIO_NAME = "SK Photo Studio"

st.set_page_config(
    page_title="AI Review Assistant",
    page_icon="⭐",
    layout="centered"
)

# ==============================
# 2. UI STYLING
# ==============================

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 600px;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3.2em;
    font-size: 16px;
    font-weight: 600;
    background-color: #4CAF50;
    color: white;
    border: none;
}

.stButton>button:hover {
    background-color: #45a049;
}

.custom-box {
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# 3. HEADER
# ==============================

st.title("⭐ Review Assistant")
st.markdown(f"Generate a genuine 5-star review for **{STUDIO_NAME}**")
st.divider()

# ==============================
# 4. EXPERIENCE SELECTION
# ==============================

st.subheader("Step 1️⃣: What did you like?")

options_list = [
    "Professionalism",
    "Creative Posing",
    "Pro Lighting",
    "Fast Delivery",
    "Friendly Staff",
    "Beautiful Edits",
    "Great Studio"
]

keywords = st.multiselect(
    "Select your experience:",
    options=options_list,
    default=["Professionalism", "Creative Posing"]
)

# ==============================
# 5. SMART TEMPLATE ENGINE
# ==============================

def generate_review(selected_keywords):

    openings = [
        f"Amazing experience at {STUDIO_NAME}!",
        f"Had a wonderful time at {STUDIO_NAME}.",
        f"Highly impressed with {STUDIO_NAME}.",
        f"Great experience overall at {STUDIO_NAME}!"
    ]

    experience_lines = [
        "The team was extremely professional.",
        "The staff was friendly and supportive.",
        "Everything was handled smoothly.",
        "The service exceeded expectations."
    ]

    keyword_line_templates = [
        "Loved the {keywords}.",
        "Really appreciated the {keywords}.",
        "The {keywords} made it special.",
        "{keywords} were outstanding."
    ]

    closings = [
        "Highly recommended!",
        "Will definitely visit again.",
        "Absolutely worth it.",
        "Five stars from me!"
    ]

    opening = random.choice(openings)
    experience = random.choice(experience_lines)
    keyword_line = random.choice(keyword_line_templates)
    closing = random.choice(closings)

    keyword_text = ", ".join(selected_keywords)

    keyword_sentence = keyword_line.format(keywords=keyword_text)

    review = f"{opening} {experience} {keyword_sentence} {closing}"

    return review

# ==============================
# 6. GENERATE BUTTON
# ==============================

st.subheader("Step 2️⃣: Generate Review")

if st.button("✨ Generate Review"):

    if not keywords:
        st.warning("Please select at least one option.")
        st.stop()

    st.session_state.final_draft = generate_review(keywords)

# ==============================
# 7. EDIT & POST
# ==============================

if "final_draft" in st.session_state:

    st.divider()
    st.subheader("Step 3️⃣: Edit & Post")

    st.success("Your Review is Ready 🎉")

    final_text = st.text_area(
        "You can edit before posting:",
        value=st.session_state.final_draft,
        height=120
    )

    st.markdown('<div class="custom-box">📋 Copy the review below</div>', unsafe_allow_html=True)
    st.code(final_text)

    st.markdown("### 🚀 Final Step")

    st.link_button("Open Google Maps & Paste Review", GOOGLE_MAPS_LINK)

    st.markdown("""
    <div class="custom-box">
    <strong>How to Post:</strong><br>
    1️⃣ Copy the review<br>
    2️⃣ Click the button above<br>
    3️⃣ Paste into Google review box<br>
    4️⃣ Submit ⭐⭐⭐⭐⭐
    </div>
    """, unsafe_allow_html=True)


# import streamlit as st
# import google.generativeai as genai
# import random

# # 1. SETUP - Replace with your details
# GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review"
# STUDIO_NAME = "SK Photo Studio"

# # 2. AI SETUP
# try:
#     genai.configure(api_key=st.secrets["GEMINI_KEY"])
#     model = genai.GenerativeModel('gemini-2.0-flash')
# except:
#     st.error("API Key error. Check Streamlit Secrets.")

# # 3. PAGE UI
# st.set_page_config(page_title="AI Review Assistant", page_icon="⭐")

# # Custom Styling
# st.markdown("""
#     <style>
#     .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; background-color: #4CAF50; color: white; font-weight: bold; }
#     </style>
#     """, unsafe_allow_html=True)

# st.title("AI Review Assistant 📸")
# st.write(f"Generate your 5-star review for **{STUDIO_NAME}**")

# # FIXED KEYWORDS (Default must be inside the list)
# options_list = ["Professionalism", "Creative Posing", "Pro Lighting", "Fast Delivery", "Friendly Staff", "Beautiful Edits", "Great Studio"]

# keywords = st.multiselect(
#     "Select what you liked:",
#     options=options_list,
#     default=["Professionalism", "Creative Posing"] # These now match the options_list
# )

# # 4. GENERATION
# if st.button("✨ Generate AI Review"):
#     try:
#         prompt = f"Write a natural 5-star Google review for {STUDIO_NAME} mentioning {', '.join(keywords)}. Max 20 words."
#         response = model.generate_content(prompt)
#         st.session_state.final_draft = response.text
#     except:
#         st.session_state.final_draft = "Amazing experience! The photos turned out beautiful and the staff was very professional. Highly recommended!"

# # 5. THE "VIDEO STYLE" FLOW
# if 'final_draft' in st.session_state:
#     st.success("Review Ready!")
    
#     # Editable Text Area
#     final_text = st.text_area("Your Review:", value=st.session_state.final_draft, height=100)

#     # SMARTY STYLE COPY BOX
#     st.info("Step 1: Click the copy icon in the box below")
#     st.code(final_text, language=None)
    
#     st.write("Step 2: Click below to post. (Paste when Google opens!)")
    
#     # THE BIG POST BUTTON
#     st.link_button("🚀 Copy & Open Google Maps", GOOGLE_MAPS_LINK)

#     st.markdown("""
#         <div style="background-color: #fff3cd; padding: 10px; border-radius: 10px; font-size: 0.9em;">
#         <strong>How to post:</strong> 1. Copy above. 2. Click button. 3. Paste on Google!
#         </div>
#     """, unsafe_allow_html=True)


# import streamlit as st
# import google.generativeai as genai
# import random

# # 1. CONFIGURATION
# # Replace this with your actual Google Business link
# GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review"

# # 10 Random Fallback Comments for a Photo Studio
# FALLBACK_REVIEWS = [
#     "Amazing experience! The lighting and professional setup were top-notch. Highly recommend for portraits!",
#     "Had a wonderful session. The photographer made us feel so comfortable and the edits are beautiful.",
#     "Fast delivery and incredible quality. Best photo studio in the area, hands down!",
#     "Great atmosphere and very creative posing help. We love our family photos!",
#     "Very professional service from start to finish. The final results exceeded our expectations.",
#     "Excellent attention to detail and very friendly staff. Will definitely be coming back for more shoots.",
#     "A truly creative team! They captured the mood of our event perfectly. 5 stars!",
#     "Smooth session and stunning results. The editing style is modern and very polished.",
#     "They handled our newborn shoot with such patience and care. The photos are priceless gems.",
#     "Top-tier photography! Efficient, professional, and very talented. Best investment for our brand."
# ]

# # 2. AI SETUP
# try:
#     genai.configure(api_key=st.secrets["GEMINI_KEY"])
#     model = genai.GenerativeModel('gemini-2.0-flash')
# except:
#     st.error("Check your API Key in Secrets!")

# # 3. PAGE DESIGN
# st.set_page_config(page_title="Studio Review Assistant", page_icon="📸")
# st.title("Photo Studio Review Helper 📸")
# st.write("Help us share your experience! We'll draft a review for you.")

# # Inputs
# session = st.selectbox("What was your session?", ["Portrait", "Wedding", "Family", "Event", "Baby Shoot"])
# highlights = st.multiselect("What was great?", ["Lighting", "Posing Help", "Fast Edits", "Professional", "Friendly Vibe"])

# # 4. REVIEW GENERATION
# if st.button("Generate Review"):
#     with st.spinner("Writing..."):
#         try:
#             prompt = f"Write a natural 5-star Google review for a photo studio. Session: {session}. Highlights: {', '.join(highlights)}. Max 25 words."
#             response = model.generate_content(prompt)
#             st.session_state.final_draft = response.text
#         except Exception as e:
#             # IF AI IS BUSY OR ERROR OCCURS:
#             if "429" in str(e) or "ResourceExhausted" in str(e):
#                 st.warning("AI is busy right now, so we picked a great review for you!")
#                 st.session_state.final_draft = random.choice(FALLBACK_REVIEWS)
#             else:
#                 st.error("Something went wrong. Picking a review from our favorites...")
#                 st.session_state.final_draft = random.choice(FALLBACK_REVIEWS)

# # 5. DISPLAY & ACTION
# if 'final_draft' in st.session_state:
#     st.divider()
#     st.subheader("Your Review is Ready!")
    
#     # Editable text area
#     user_text = st.text_area("Final Review Text:", value=st.session_state.final_draft, height=120)
    
#     # Native Copy Box
#     st.write("### Step 1: Copy your review")
#     st.code(user_text, language=None)
    
#     # Post Button
#     st.write("### Step 2: Post to Google")
#     st.link_button("🚀 Post on Google Maps", GOOGLE_MAPS_LINK)
