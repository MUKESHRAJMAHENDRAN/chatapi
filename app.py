import streamlit as st
import requests

st.title("Chatbot")

# Initialize session state for messages and chatbot model
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Type your message and press Enter"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the user input to FastAPI and get the response
    try:
        response = requests.post(
            "http://127.0.0.1:8000/chat",  # FastAPI URL
            json={"input_text": prompt},
        )

        if response.status_code == 200:
            response_data = response.json()
            assistant_reply = response_data['output_text']
        else:
            assistant_reply = f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        assistant_reply = f"Failed to connect to FastAPI: {e}"

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
