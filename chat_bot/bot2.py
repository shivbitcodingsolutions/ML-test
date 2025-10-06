import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()

chatbot = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

system_prompt = SystemMessage(
    content="you are a helpful chatbot. Answer clearly and politely"
)


while True:
    user_msg = input("you: ").strip()

    if user_msg.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye")
        break

    response = chatbot.invoke([
        system_prompt,
        HumanMessage(content=user_msg)
    ])

    print("Bot:", response.content)
