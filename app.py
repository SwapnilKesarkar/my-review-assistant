import streamlit as st
import google.generativeai as genai

# 1. SETUP
# Replace with your actual Google Business Review link
GOOGLE_REVIEW_URL = "https://g.page/r/YOUR_STUDIO_ID/review"

# 2. AI CONFIGURATION
try:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception as e:
    st.error("API Key missing! Add GEMINI_KEY to Streamlit Secrets.")

# 3. UI DESIGN
st.set_page_config(page_title="Studio Review Assistant", page_icon="📸")
st.title("Photo Studio Review Assistant 📸")
st.write("Help us share your experience! Pick a few details below.")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    session = st.selectbox("Shoot Type", ["Portrait", "Wedding", "Event", "Family", "Newborn"])
with col2:
    vibe = st.multiselect("Highlights", ["Creative Lighting", "Posing Help", "Professional", "Fast Delivery", "Friendly"])

details = st.text_input("Any specific names or details? (Optional)")

if st.button("Generate Review"):
    if not vibe:
        st.warning("Please select at least one highlight!")
    else:
        with st.spinner("Drafting your review..."):
            try:
                prompt = f"Write a natural 5-star Google review for a photo studio. Session: {session}. Highlights: {', '.join(vibe)}. Details: {details}. Max 30 words."
                response = model.generate_content(prompt)
                st.session_state.draft = response.text
            except Exception as e:
                st.error("AI is busy. Please try again in 10 seconds.")

# 4. STABLE COPY AREA
if 'draft' in st.session_state:
    st.subheader("Your AI Draft:")
    
    # Text area for minor editing
    final_text = st.text_area("Edit if you like:", value=st.session_state.draft, height=100)
    
    # The Stable Copy Box
    st.write("Click the **copy icon** in the top-right of the box below:")
    st.code(final_text, language=None)
    
    st.write("---")
    st.info("Step 1: Copy the text above.\nStep 2: Click the button below to paste on Google!")
    st.link_button("🚀 Open Google Reviews", GOOGLE_REVIEW_URL)
