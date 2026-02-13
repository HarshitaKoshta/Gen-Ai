from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.9, #diff o/p generation
    max_retries=2,
    )
# chatmodel=ChatOpenAI(model="gpt-5-nano", temperature=0.8)
message=[SystemMessage(content="You are a funny bot "),HumanMessage(content="tell me a joke about Gen Ai")]
# result =chatmodel.invoke(message)
result = model.invoke(message)
message.append(AIMessage(content=result.content))
print(message)