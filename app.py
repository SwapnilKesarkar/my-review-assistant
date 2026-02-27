import streamlit as st
import random

# ==============================
# CONFIG
# ==============================

GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review"
STUDIO_NAME = "SK Photo Studio"

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

.copy-success {
    color: green;
    font-size: 14px;
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
# INITIAL AUTO GENERATE
# ==============================

if "review_text" not in st.session_state:
    st.session_state.review_text = generate_review()

# ==============================
# TITLE
# ==============================

st.title("⭐ Review SK Photo Studio")

st.divider()

# ==============================
# DIRECT EDITOR
# ==============================

review_text = st.text_area(
    "Your Review:",
    value=st.session_state.review_text,
    height=120
)

# Update session state if edited
st.session_state.review_text = review_text

# ==============================
# CHANGE BUTTON
# ==============================

if st.button("🔄 Change Review"):
    st.session_state.review_text = generate_review()
    st.rerun()

# ==============================
# COPY BUTTON
# ==============================

if st.button("📋 Copy Review"):
    st.write("Copy the text above and paste on Google.")
    st.markdown('<p class="copy-success">✔ Ready to paste</p>', unsafe_allow_html=True)

# ==============================
# POST BUTTON
# ==============================

st.link_button("🚀 Post on Google", GOOGLE_MAPS_LINK)

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
