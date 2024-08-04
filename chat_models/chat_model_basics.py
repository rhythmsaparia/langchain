from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()


llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


messages = [
    SystemMessage(content="You answer answers in short one sentences, you are decisive and opinionated"),
    HumanMessage(content="what is the best cuisine?")
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)



