
# Google Gemini-Pro Chat Application

This Streamlit web application enables users to converse with Google's advanced GenerativeAI, Gemini-Pro, providing a dynamic and interactive user experience.

## About The Project

The Google Gemini-Pro Chat Application leverages Streamlit to create a responsive web interface that allows users to engage in real-time dialogue with Google's GenerativeAI technology. This setup makes it easy for users to receive instant AI-generated responses to inquiries, ranging from simple questions to complex discussions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Google GenerativeAI
- Google API Key
- Streamlit

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rajprashantsharma/Gemini-ChatBot.git
   cd gemini-pro-chat

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API Key:

   - Create a project on the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the GenerativeAI API.
   - Create an API key and add it to your environment variables or a `.env` file.

4. Run the application:

   ```bash
   streamlit run app.py
   ```

   The application will be accessible at [http://localhost:8501/](http://localhost:8501/).

## Usage

1. Open your web browser and navigate to [http://localhost:8501/](http://localhost:8501/).
2. Enter your message in the chat input box.
3. Chat with Google Gemini-Pro and view the responses in real-time.