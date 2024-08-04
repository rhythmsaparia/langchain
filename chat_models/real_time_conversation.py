from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
load_dotenv()


llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

chat_history = []
system_message = SystemMessage(content="You are AI Assistant, you are opinionated, and always argue with what human has to say.")

chat_history.append(system_message)

while True:
    query = input("query: ")
    if query.lower() == "break":
        break
    chat_history.append(HumanMessage(content=query))
    result = llm.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    print("AI: ", response)




