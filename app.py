import streamlit as st
import google.generativeai as genai
import random

# 1. CONFIGURATION
# Replace this with your actual Google Business link
GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review"

# 10 Random Fallback Comments for a Photo Studio
FALLBACK_REVIEWS = [
    "Amazing experience! The lighting and professional setup were top-notch. Highly recommend for portraits!",
    "Had a wonderful session. The photographer made us feel so comfortable and the edits are beautiful.",
    "Fast delivery and incredible quality. Best photo studio in the area, hands down!",
    "Great atmosphere and very creative posing help. We love our family photos!",
    "Very professional service from start to finish. The final results exceeded our expectations.",
    "Excellent attention to detail and very friendly staff. Will definitely be coming back for more shoots.",
    "A truly creative team! They captured the mood of our event perfectly. 5 stars!",
    "Smooth session and stunning results. The editing style is modern and very polished.",
    "They handled our newborn shoot with such patience and care. The photos are priceless gems.",
    "Top-tier photography! Efficient, professional, and very talented. Best investment for our brand."
]

# 2. AI SETUP
try:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel('gemini-2.0-flash')
except:
    st.error("Check your API Key in Secrets!")

# 3. PAGE DESIGN
st.set_page_config(page_title="Studio Review Assistant", page_icon="📸")
st.title("Photo Studio Review Helper 📸")
st.write("Help us share your experience! We'll draft a review for you.")

# Inputs
session = st.selectbox("What was your session?", ["Portrait", "Wedding", "Family", "Event", "Baby Shoot"])
highlights = st.multiselect("What was great?", ["Lighting", "Posing Help", "Fast Edits", "Professional", "Friendly Vibe"])

# 4. REVIEW GENERATION
if st.button("Generate Review"):
    with st.spinner("Writing..."):
        try:
            prompt = f"Write a natural 5-star Google review for a photo studio. Session: {session}. Highlights: {', '.join(highlights)}. Max 25 words."
            response = model.generate_content(prompt)
            st.session_state.final_draft = response.text
        except Exception as e:
            # IF AI IS BUSY OR ERROR OCCURS:
            if "429" in str(e) or "ResourceExhausted" in str(e):
                st.warning("AI is busy right now, so we picked a great review for you!")
                st.session_state.final_draft = random.choice(FALLBACK_REVIEWS)
            else:
                st.error("Something went wrong. Picking a review from our favorites...")
                st.session_state.final_draft = random.choice(FALLBACK_REVIEWS)

# 5. DISPLAY & ACTION
if 'final_draft' in st.session_state:
    st.divider()
    st.subheader("Your Review is Ready!")
    
    # Editable text area
    user_text = st.text_area("Final Review Text:", value=st.session_state.final_draft, height=120)
    
    # Native Copy Box
    st.write("### Step 1: Copy your review")
    st.code(user_text, language=None)
    
    # Post Button
    st.write("### Step 2: Post to Google")
    st.link_button("🚀 Post on Google Maps", GOOGLE_MAPS_LINK)
