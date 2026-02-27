import streamlit as st
import google.generativeai as genai
import random

# 1. YOUR STUDIO DETAILS
GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review" # <-- Replace with your link
STUDIO_NAME = "SK Photo Studio" # <-- Replace with your studio name

# 10 Professional Fallback Reviews (if AI is busy)
FALLBACK_REVIEWS = [
    f"Amazing experience at {STUDIO_NAME}! The lighting was top-notch. Highly recommend for portraits!",
    "Had a wonderful photoshoot. They made us feel so comfortable and the edits are beautiful.",
    "Fast delivery and incredible quality. Best photo studio in the area!",
    "Great atmosphere and very creative posing help. We love our family photos!",
    "Very professional service. The final results exceeded our expectations.",
    "Excellent attention to detail and very friendly staff. Will be back!",
    "A truly creative team! They captured the mood perfectly. 5 stars!",
    "Smooth session and stunning results. Very polished editing style.",
    "They handled our shoot with such patience and care. The photos are gems.",
    f"Top-tier photography at {STUDIO_NAME}! Efficient and very talented."
]

# 2. AI SETUP
try:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel('gemini-2.0-flash')
except:
    st.error("API Key error. Check Streamlit Secrets.")

# 3. SMARTY-STYLE UI
st.set_page_config(page_title="AI Review Standee", page_icon="⭐")

# Custom CSS to make it look like a professional app
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("AI Review Assistant 📸")
st.write(f"Welcome to **{STUDIO_NAME}**! Tap the tags below to generate your AI review.")

# "Top Keywords" feature (Like the video)
st.subheader("Select what you liked:")
keywords = st.multiselect(
    "Tap to add to review:",
    ["Creative Lighting", "Posing Help", "Fast Delivery", "Professionalism", "Friendly Staff", "Beautiful Edits", "Comfortable Studio", "Great Price"],
    default=["Professionalism"]
)

# Optional Custom Note
extra_detail = st.text_input("Anything else? (e.g. Photographer name)", placeholder="Optional...")

# 4. GENERATION LOGIC
if st.button("✨ Generate My AI Review"):
    with st.spinner("AI is writing your review..."):
        try:
            prompt = f"Write a natural 5-star Google review for {STUDIO_NAME}. Include these keywords: {', '.join(keywords)}. Extra details: {extra_detail}. Keep it warm and under 25 words."
            response = model.generate_content(prompt)
            st.session_state.final_draft = response.text
        except Exception as e:
            # Fallback if busy (429 Error)
            st.warning("AI is busy, but we've prepared a great draft for you!")
            st.session_state.final_draft = random.choice(FALLBACK_REVIEWS)

# 5. POST FLOW
if 'final_draft' in st.session_state:
    st.success("Review Generated!")
    
    # Editable Text Box
    user_review = st.text_area("You can edit this:", value=st.session_state.final_draft, height=120)
    
    # Step 1: Copy
    st.write("### 1. Copy Review")
    st.code(user_review, language=None)
    
    # Step 2: Post
    st.write("### 2. Post on Google")
    st.link_button("🚀 Open Google Maps & Paste", GOOGLE_MAPS_LINK)
    
    st.caption("Copy the text, click the button, paste, and post! Thank you! ❤️")


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
