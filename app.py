import streamlit as st
import google.generativeai as genai

# 1. CONFIGURATION
# IMPORTANT: Replace the URL below with your actual "Ask for Review" link from Google
GOOGLE_MAPS_LINK = "https://g.page/r/YOUR_STUDIO_ID/review" 

# 2. AI SETUP
try:
    # Using 2.0 Flash as it is the most stable free model in early 2026
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel('gemini-2.0-flash')
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

extra_detail = st.text_input("Anything specific to mention? (Optional)")

# 4. REVIEW GENERATION LOGIC
if st.button("Generate Review Draft"):
    if not highlights:
        st.warning("Please select at least one thing you loved!")
    else:
        with st.spinner("Writing your studio review..."):
            try:
                prompt = (f"Write a natural 5-star Google review for a photography studio. "
                          f"Session: {session_type}. Highlights: {', '.join(highlights)}. "
                          f"Details: {extra_detail}. Keep it warm and professional. Max 30 words.")
                
                response = model.generate_content(prompt)
                st.session_state.final_draft = response.text
                
            except Exception as e:
                if "429" in str(e):
                    st.error("The AI is busy. Please wait 10 seconds and try again!")
                else:
                    st.error("Something went wrong. Please try again.")

# 5. THE POST FLOW (Copy & Redirect)
if 'final_draft' in st.session_state:
    st.divider()
    st.subheader("Your AI Draft is Ready!")
    
    # Text area for user to make final edits
    user_edited_text = st.text_area("Edit your review if needed:", 
                                     value=st.session_state.final_draft, height=120)
    
    # STABLE COPY METHOD: Built-in Streamlit code block with copy icon
    st.write("### Step 1: Copy your review")
    st.info("Click the 'Copy' icon in the top-right of the box below:")
    st.code(user_edited_text, language=None)
    
    # THE REDIRECT BUTTON
    st.write("### Step 2: Post to Google")
    st.write("Click the button below. Once Google opens, **Paste** your review and hit **Post**!")
    st.link_button("🚀 Open Google & Paste Review", GOOGLE_MAPS_LINK)
    
    if st.button("Clear and Start Over"):
        del st.session_state.final_draft
        st.rerun()
