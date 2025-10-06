import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv


load_dotenv()

# client = Groq(api_key="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")



chatbot = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)



chatbot = ChatGroq(
    model_name="llama-3.3-70b-versatile"
)



while True:

    user_msg = input("type here: ")

    print("user: ",user_msg)

    if user_msg.strip().lower() in ["exit", "quit", "bye"]:
        break

    response = chatbot.invoke({'messages': [HumanMessage(content=user_msg)]})

    print('ai: ', response['messages'][-1].content)
    

    
    


# client = Groq(api_key="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")

# chat_completion = client.chat.completions.create(
#     messages=[
#         # Set an optional system message. This sets the behavior of the
#         # assistant and can be used to provide specific instructions for
#         # how it should behave throughout the conversation.
#         {
#             "role": "system",
#             "content": "You are a helpful assistant."
#         },
#         # Set a user message for the assistant to respond to.
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],

#     # The language model which will generate the completion.
#     model="llama-3.3-70b-versatile"
# )

# # Print the completion returned by the LLM.
# print(chat_completion.choices[0].message.content)





