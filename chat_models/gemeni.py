from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.9, #diff o/p generation
    max_tokens=None, #
    max_retries=2,
    )
result = model.invoke("What is life?")
print("\n\n\n\n")
print(result)   
print("\n\n\n\n")
