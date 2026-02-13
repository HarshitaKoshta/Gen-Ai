from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.9,
    max_retries=2 ,
    )
prompt = PromptTemplate(
    template="Create 3 medium-level math word problems based on the topic: {topic}",
    input_variables=["topic"]
)
parser = StrOutputParser()
# Pipeline → prompt → model → parser. # | => pipe symbol /runnable operator
chain = prompt | model | parser
result = chain.invoke({"topic": "Time and Work"})
print(result)
# Show graph 
chain.get_graph().print_ascii()