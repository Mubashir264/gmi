import streamlit as st
import random  # NEW

st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")
st.title("🌱 Growth Mindset Challenge")

# NEW: Motivational quote
quotes = [
    "“The expert in anything was once a beginner.” — Helen Hayes",
    "“Mistakes are proof that you are trying.” — Unknown"
]
st.caption(f"*{random.choice(quotes)}*")  # NEW

st.markdown("""
## What is a Growth Mindset?
[... rest of original content ...]
""")

response = st.radio("Will you adopt the growth mindset?", 
                   ("Yes! I'm ready!", "Maybe, I need time.", "No, not now."))

if response == "Yes! I'm ready!":
    st.success("👏 That's amazing! Keep growing!")
    st.write("**Today's Challenge:** Learn one new thing outside your comfort zone!")  # NEW




