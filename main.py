import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "YOUR_API_KEY"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """I'm truly sorry to hear that you're experiencing these thoughts. Your well-being is my top priority, and I'm here to support you through this difficult time. Remember, you don't have to face this alone. Reaching out to a mental health professional or a trusted person in your life can provide the support and guidance you need. It takes courage to seek help, and I want to encourage you to prioritize your safety and well-being. You are not alone in this journey, and there are resources available to help you find hope and healing. Please consider talking to someone who can offer understanding and assistance. Your life is valuable, and there is a path towards brighter days. Take care of yourself, and know that there are people who care about you. How can I continue to support you today?
"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state
