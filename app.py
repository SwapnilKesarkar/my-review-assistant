import streamlit as st
import google.generativeai as genai

# Replace with your actual Google Business Review Link
GOOGLE_MAPS_URL = "https://g.page/r/YOUR_BUSINESS_ID/review"

# Configure the AI
genai.configure(api_key=st.secrets["GEMINI_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# UI Design
st.set_page_config(page_title="Review Helper", page_icon="📝")
st.title("How was your visit? ✨")
st.write("Pick a few details and we'll help you draft a review!")

# Inputs
col1, col2 = st.columns(2)
with col1:
    rating = st.selectbox("Rating", ["5 Stars ⭐⭐⭐⭐⭐", "4 Stars ⭐⭐⭐⭐"])
with col2:
    service = st.multiselect("What was great?", ["Service", "Food", "Price", "Atmosphere", "Speed"])

custom_note = st.text_input("Anything specific to add? (Optional)")

if st.button("Generate My Review"):
    # The Prompt - This tells the AI how to behave
    prompt = f"Write a natural, friendly Google review for a business. Rating: {rating}. Highlights: {', '.join(service)}. Specifics: {custom_note}. Keep it under 40 words. Don't use hashtags."
    
    response = model.generate_content(prompt)
    draft = response.text
    
    st.subheader("Your Draft:")
    # Text area allows user to edit
    final_review = st.text_area("You can edit this text:", value=draft, height=150)
    
    st.info("Step 1: Copy the text above. \nStep 2: Click the button below to paste it on Google!")
    
    # Button to open Google
    st.link_button("Go to Google Reviews", GOOGLE_MAPS_URL)
