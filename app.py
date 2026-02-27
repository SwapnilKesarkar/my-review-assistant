import streamlit as st
import google.generativeai as genai

# 1. SETUP - REPLACE THE LINK BELOW
# To get this link: Go to Google Business Profile -> Ask for Reviews -> Copy Link
GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review"

# 2. AI CONFIGURATION
try:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    # Using 2.0 Flash - stable and high free quota
    model = genai.GenerativeModel('gemini-2.0-flash')
except:
    st.error("API Key error. Check Streamlit Secrets.")

# 3. UI DESIGN
st.set_page_config(page_title="Studio Review Assistant", page_icon="📸")
st.title("Photo Studio Review Helper 📸")
st.write("We'll help you draft a professional review to post on Google!")

# Inputs
session = st.selectbox("What was your session?", ["Portrait", "Wedding", "Family", "Event"])
highlights = st.multiselect("What was great?", ["Lighting", "Posing Help", "Fast Edits", "Professional"])

if st.button("Generate Review"):
    with st.spinner("Drafting..."):
        try:
            prompt = f"Write a natural 5-star Google review for a photo studio. Session: {session}. Highlights: {', '.join(highlights)}. Max 25 words."
            response = model.generate_content(prompt)
            st.session_state.draft = response.text
        except:
            st.error("AI is busy. Please try again in 10 seconds.")

# 4. THE POSTING FLOW
if 'draft' in st.session_state:
    st.subheader("Your Review is Ready!")
    
    # 1. Show the text for the user to see
    final_review = st.text_area("Final Text:", value=st.session_state.draft, height=100)
    
    # 2. Provide a COPY box (Built-in Streamlit feature)
    st.write("Step 1: Click the copy icon in the top-right of this box:")
    st.code(final_review, language=None)
    
    st.write("---")
    
    # 3. The Jump Button
    st.write("Step 2: Click the button below. Once Google opens, **Paste** your text and hit **Post**.")
    st.link_button("🚀 Jump to Google Reviews", GOOGLE_MAPS_LINK)
