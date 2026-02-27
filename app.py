import streamlit as st
import google.generativeai as genai
from st_copy import copy_button

# 1. CONFIGURATION
GOOGLE_MAPS_LINK = "https://g.page/r/CcgQczb7P9guEAE/review"

# 2. AI SETUP
try:
    # Use the 2026 stable free model: Gemini 2.5 Flash-Lite
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
except Exception as e:
    st.error("Setup Error: Please check your API Key in Streamlit Secrets.")

# 3. PAGE DESIGN
st.set_page_config(page_title="Studio Review Assistant", page_icon="📸")

st.title("Capture Your Thoughts! 📸")
st.write("We hope you enjoyed your photoshoot. Let's help you write a quick review!")

# Photo Studio Specific Inputs
col1, col2 = st.columns(2)
with col1:
    session_type = st.selectbox("What was the occasion?", 
                                ["Portrait", "Wedding", "Family", "Product", "Event", "Baby Shoot"])
with col2:
    rating = st.select_slider("Rating", options=["4", "5"], value="5")

highlights = st.multiselect("What did you love?", 
                            ["Lighting", "Professionalism", "Posing Help", "Fast Delivery", "Editing Quality", "Friendly Atmosphere"])

extra_detail = st.text_input("Anything specific to mention? (e.g., photographer name)")

# 4. REVIEW GENERATION LOGIC
if st.button("Generate Review Draft"):
    if not highlights:
        st.warning("Please select at least one thing you loved!")
    else:
        with st.spinner("Writing your studio review..."):
            try:
                # Specialized prompt for a Photo Studio
                prompt = (f"Write a natural 5-star Google review for a photography studio. "
                          f"Session: {session_type}. Highlights: {', '.join(highlights)}. "
                          f"Details: {extra_detail}. Keep it warm, professional, and max 30 words.")
                
                response = model.generate_content(prompt)
                review_text = response.text
                
                # Save to session state so it stays on screen
                st.session_state.final_draft = review_text
                
            except Exception as e:
                if "429" in str(e):
                    st.error("The free AI is currently busy. Please wait 10 seconds and try again!")
                else:
                    st.error("AI Error. Please try clicking the button again.")

# 5. DISPLAY AND ACTION
if 'final_draft' in st.session_state:
    st.subheader("Your AI Draft:")
    
    # Text area for editing
    user_edited_text = st.text_area("You can tweak the text here:", 
                                     value=st.session_state.final_draft, height=120)
    
    # Copy Button (New Feature!)
    copy_button(user_edited_text, label="📋 Copy Review Text", copied_label="✅ Copied!")
    
    st.write("---")
    st.info("Step 1: Click the 'Copy' button above.\nStep 2: Click the button below to paste on Google!")
    st.link_button("🚀 Post on Google Maps", GOOGLE_MAPS_LINK)
