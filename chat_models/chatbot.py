from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(git add .gitignore
    model="gemini-2.5-flash", 
    temperature=0.9,
    max_tokens=None,
    max_retries=2 ,
    )
role = input("Enter the role of the bot:\n")
history = [SystemMessage(content=f"You are a {role} bot")]
print("You can start chatting with the bot now! (type 'quit' to exit)")
while True:
    text = input("Enter your question (or 'quit' to exit):\n ")
    history.append(HumanMessage(content=text))
    if text  == "quit":
        break

    result = model.invoke(history)
    history.append(AIMessage(content=result.content))
    print("BOT", result.content,"\n\n")