import streamlit as st
from pipeline import get_answer

st.set_page_config(page_title="Answerly - Document Search Assistant")

st.title("Answerly - AI Assistant for Word and PDF Docs")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def show_chat():
    for sender, message in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {message}")

def user_input():
    return st.text_input("Ask your question about the uploaded documents:")

query = user_input()

if query:
    with st.spinner("Searching..."):
        answer = get_answer(query)
        st.session_state.chat_history.append(("You", query))
        st.session_state.chat_history.append(("Answely", answer))

show_chat()
