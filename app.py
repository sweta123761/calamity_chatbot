import streamlit as st

st.set_page_config(page_title="Relief Chatbot", layout="centered")

st.title("🤖 Relief Support Chatbot")
st.markdown("This chatbot is designed to support survivors of natural calamities across India.")

# Session state to keep chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Expanded response dictionary
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! How can I assist you?",
    "food": "Food supplies are being distributed at nearby relief camps. Please carry your ID if possible.",
    "water": "Clean drinking water is available at designated distribution points near shelters.",
    "shelter": "Temporary shelters are set up at community halls, schools, and stadiums.",
    "medical": "First aid and medical help are available at mobile clinics and relief centers.",
    "missing": "Please report missing persons at the nearest relief center or helpline 1098.",
    "volunteer": "You can register as a volunteer on the official disaster relief website or local centers.",
    "clothes": "Clothing donations are being distributed at collection points in community centers.",
    "evacuation": "Evacuation transport is arranged in low-lying areas. Listen to local announcements.",
    "thank you": "You're welcome! Stay safe and take care.",
    "electricity": "Power outages are being addressed. Generators are provided at shelters.",
    "donate": "You can donate through verified platforms listed on the official government site.",
    "ngo": "To locate NGOs helping in your area, visit [NGO Darpan](https://ngodarpan.gov.in) — a government portal that lists verified NGOs in India. You can search by state, district, or service type.",
    "location": "You can share your pin code or district name so we can suggest local NGOs and help centers.",
    "website": "To use this website, simply type your query in the input box. For example, try typing 'food', 'shelter', 'medical', or 'ngo'. The bot will assist you based on available resources.",
    "how to use": "Just enter your concern like 'I need food' or 'Where can I find shelter?' and I’ll try to guide you. You can also ask about NGO help, donations, or volunteer options.",
    "ngo predictor": "The NGO Predictor is a tool to forecast resource needs like food, water, shelter, or volunteers based on crisis data. It helps NGOs manage supplies efficiently. Visit the 'NGO Resource Dashboard' section of the site to use it.",
    "resource management": "To manage NGO resources smartly, use our AI-based predictor tool. It analyzes disaster data to suggest how many resources (like food kits or volunteers) may be needed in each region."
}

# Function to get chatbot response
def get_response(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return responses[key]
    return "I'm here to help. Please provide more details or try rephrasing your query."

# Input box
user_input = st.text_input("You:", "")

# Handle input
if user_input:
    user_text = f"🧑‍💬 You: {user_input}"
    bot_text = f"🤖 Bot: {get_response(user_input)}"
    st.session_state.chat_history.append(user_text)
    st.session_state.chat_history.append(bot_text)

# Display chat history
for msg in st.session_state.chat_history:
    st.write(msg)

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
