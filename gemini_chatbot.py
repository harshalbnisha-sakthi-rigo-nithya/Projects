import streamlit as st
from openai import OpenAI
import os

# -----------------------------
# ⚙️ Streamlit Page Setup
# -----------------------------
st.set_page_config(
    page_title="Gemini-like Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# 🎨 Custom Gemini-style UI
# -----------------------------
st.markdown("""
    <style>
        body {
            background-color: #0E1117;
            color: #FFFFFF;
        }
        .stChatMessage {
            padding: 1rem;
            border-radius: 1rem;
            margin-bottom: 0.5rem;
            max-width: 80%;
        }
        .user-bubble {
            background-color: #005CFF;
            color: white;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #1E1E1E;
            border: 1px solid #333;
        }
        .stTextInput > div > div > input {
            background-color: #1E1E1E;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 🔐 API Key Setup
# -----------------------------
# ✅ Option 1 — Put your API key directly here
api_key = "sk-your_openai_api_key_here"

# ✅ Option 2 — Load from .streamlit/secrets.toml if available
try:
    if not api_key or api_key.startswith("sk-your"):
        api_key = st.secrets["openai"]["api_key"]
except Exception:
    pass

# ✅ Option 3 — Load from environment variable if available
if not api_key or api_key.startswith("sk-your"):
    api_key = os.getenv("OPENAI_API_KEY")

# ❌ Stop if no valid key found
if not api_key or api_key.startswith("sk-your"):
    st.error("❌ OpenAI API key not found. Please add it directly in the code or in `.streamlit/secrets.toml`.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# -----------------------------
# 💬 Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey there 👋, I’m your Gemini-style AI assistant. How can I help you today?"}
    ]

# -----------------------------
# 🪄 Display Chat History
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"<div class='stChatMessage user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        with st.chat_message("assistant"):
            st.markdown(f"<div class='stChatMessage bot-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

# -----------------------------
# 🧠 User Input & AI Response
# -----------------------------
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user bubble
    with st.chat_message("user"):
        st.markdown(f"<div class='stChatMessage user-bubble'>{prompt}</div>", unsafe_allow_html=True)

    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Choose model you have access to
            stream = client.chat.completions.create(
                model="gpt-4o",  # ✅ Use "gpt-4o" or "gpt-3.5-turbo" if GPT-4 isn't available
                messages=st.session_state.messages,
                stream=True,
            )

            for chunk in stream:
                if chunk.choices[0].delta.get("content"):
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(
                        f"<div class='stChatMessage bot-bubble'>{full_response}▌</div>",
                        unsafe_allow_html=True
                    )

            message_placeholder.markdown(
                f"<div class='stChatMessage bot-bubble'>{full_response}</div>",
                unsafe_allow_html=True
            )

        except Exception as e:
            full_response = f"⚠️ Error: {str(e)}"
            message_placeholder.markdown(
                f"<div class='stChatMessage bot-bubble'>{full_response}</div>",
                unsafe_allow_html=True
            )

    # Save assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
