import streamlit as st
from llm_helper import get_llm_response

st.set_page_config(page_title="Content App", layout="centered")
st.title("✍️ Content Writer")

prompt = st.text_area("Enter your prompt here:")

if st.button("Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt!")
    else:
        with st.spinner("Generating..."):
            result = get_llm_response(prompt)
            st.success("Done!")
            st.write(result)
