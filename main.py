import streamlit as st
from streamlit_chat import message
from workflow.graph import graph 

st.header("QA Chatbot")

prompt = st.text_input("Prompt", placeholder="Enter your question here.")

if (
    "user_prompt_history" not in st.session_state
    and "chat_answers_history" not in st.session_state
):
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_answers_history"] = []

if prompt:
    with st.spinner("Generating response..."):
        response = graph.invoke({"question": prompt})

        answer = response["answer"]

        st.session_state.user_prompt_history.append(prompt)
        st.session_state.chat_answers_history.append(answer)


if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)
