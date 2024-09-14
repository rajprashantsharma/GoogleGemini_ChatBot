import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Google Gemini-Pro!",
    page_icon=":robot_face:",  # Emoji as favicon
    layout="wide",  # Streamlit layout option
)

# Configure Gemini-Pro with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Function to map Gemini-Pro roles to Streamlit display roles
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Initialize chat session if it doesn't exist
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Set page title
st.title("Chat with Google Gemini-Pro!")

# Display past chat messages
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input box for user to send new messages
if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    # Display user's submitted message
    st.chat_message("user").markdown(prompt)
    
    # Send the message to Gemini-Pro and receive response
    response = st.session_state.chat.send_message(prompt)
    
    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(response.text)
