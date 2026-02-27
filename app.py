import streamlit as st
import google.generativeai as genai

# 1. SETUP - Replace the link below with your actual Google Business Link
GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review"

# 2. AI CONFIGURATION
# We use 'try/except' so the app doesn't crash if the Key is missing
try:
    api_key = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("API Key is missing! Please add GEMINI_KEY to Streamlit Secrets.")

# 3. USER INTERFACE
st.title("Review Assistant ⭐")
st.write("Tell us about your experience and we'll help you write a review!")

# Input fields
service_type = st.multiselect("What did you like?", ["Food", "Service", "Atmosphere", "Price", "Cleanliness"])
user_comments = st.text_input("Any specific details? (Optional)")

if st.button("Generate Review Draft"):
    if not service_type:
        st.warning("Please select at least one thing you liked!")
    else:
        prompt = f"Write a 5-star Google review. Mention: {', '.join(service_type)}. Details: {user_comments}. Natural tone, no hashtags, max 30 words."
        
        response = model.generate_content(prompt)
        review_text = response.text
        
        st.subheader("Your AI Draft:")
        # The text area allows the user to edit the text
        final_text = st.text_area("Edit this text if you want:", value=review_text, height=150)
        
        st.info("Copy the text above, then click the button below to paste it on Google!")
        st.link_button("Open Google Reviews", GOOGLE_MAPS_LINK)
