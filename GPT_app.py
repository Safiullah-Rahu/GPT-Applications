import streamlit as st

# Import the OpenAI GPT-3 library
import openai
openai.api_key = "api_key"

# Create a function to generate text using GPT-3
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

# Create the Streamlit UI
st.title("GPT-3 Text Generator")
prompt = st.text_input("Enter your prompt:")

if st.button("Generate Text"):
    result = generate_text(prompt)
    st.success(result)
