import streamlit as st
from src import enhancer

st.title("⚡ PromptPolish")
st.subheader("",divider= "rainbow")

st.subheader("😎 Perfect your prompts with precision and speed.")

st.markdown("PromptPolish ✨ is a cutting-edge tool designed to enhance and refine prompts for large language models (LLMs). By optimizing prompt clarity and relevance, PromptPolish ensures that AI interactions are more accurate and effective, enabling better outcomes for your natural language processing tasks. 🚀")


# Create a text area for user input
user_prompt = st.text_area(
    label="Enter your prompt:",
    placeholder="Type your prompt here...",
)

btn = st.button("Enhance")

if btn:
# Display the entered prompt
    if user_prompt:
        st.write("💬 You entered:")
        st.write(user_prompt)

        st.markdown("---")
        refined_prompt = enhancer.groq_enhancer(user_prompt)
        st.write("💡 Refined prompt: << gemini-1.5-flash >>")
        st.write(refined_prompt)

        st.markdown("---")
        refined_prompt = enhancer.gemini_enhancer(user_prompt)
        st.write("💡 Refined prompt: << llama-3.1-8b-instant >>")
        st.write(refined_prompt)