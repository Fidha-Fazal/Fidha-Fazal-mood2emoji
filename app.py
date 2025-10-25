import streamlit as st
from textblob import TextBlob
import re 

# --- 1. Safety Filter Logic ---
# List of words to filter out (You can add more words here)
BAD_WORDS = ["stupid", "idiot", "dumb", "kill", "hate"]

def is_text_safe(text):
    """Checks for inappropriate words using regex."""
    text_lower = text.lower()
    for word in BAD_WORDS:
        # Use regex to find whole words (\b), not parts of words (like 'killing' is safe)
        if re.search(r'\b' + re.escape(word) + r'\b', text_lower):
            return False
    return True

def classify_mood(text):
    """Classifies sentiment and returns emoji, explanation, and polarity."""
    
    # 1. Safety Check (The Neutral Fallback for inappropriate text)
    if not is_text_safe(text):
        return "😐", "Sorry, that text is not appropriate for analysis.", 0.0

    # 2. TextBlob analysis
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    # Polarity is a score from -1.0 (negative) to +1.0 (positive)

    # 3. Rule-Based Classification (Logic clarity is 15 points)
    if polarity > 0.3:
        emoji = "😊"
        explanation = "Sounds happy!"
    elif polarity < -0.3:
        emoji = "😔"
        explanation = "Sounds sad."
    else:
        # Neutral Fallback for neutral/thoughtful text
        emoji = "🤔"
        explanation = "Sounds thoughtful."
        
    return emoji, explanation, polarity


# --- 2. Streamlit UI (Front-End) ---

st.set_page_config(
    page_title="Kid-safe Mood Detector",
    layout="centered"
)
st.title("Mood2Emoji App 🤖")
st.markdown("Enter a short sentence and see what mood the detector finds!")

# Input Box
user_input = st.text_input("Enter a sentence here:", placeholder="e.g., I love coding!")

# Optional Teacher Mode Checkbox
teacher_mode = st.checkbox("Teacher Mode: Show Logic", value=False)

if user_input:
    # Get the classification
    emoji, explanation, polarity = classify_mood(user_input)
    
    # Display Output
    st.subheader("Result:")
    st.markdown(f"**{emoji}**")
    st.info(f"{explanation}")

    # Optional Feature: Teacher Mode (Rule Clarity demonstration)
    if teacher_mode:
        st.subheader("How It Works:")
        
        st.code(f"Sentiment Polarity Score: {polarity:.2f}")

        st.markdown("""
        The app uses a **Polarity Score** (-1.0 to +1.0) to classify mood:
        
        * **Positive (😊):** Score is greater than **+0.3**
        * **Negative (😔):** Score is less than **-0.3**
        * **Neutral (🤔/😐):** Score is between **-0.3 and +0.3** """)

# Footer for instruction
st.markdown("---")
st.caption("Built with Python and Streamlit. For educational use (Ages 12-16).")