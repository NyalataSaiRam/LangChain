from langgraph.graph import MessagesState
from langchain_core.messages import RemoveMessage
from genai import llm_call_tools

# invokes the llm with userInput
def call_llm(state: MessagesState):
    return {"messages": llm_call_tools.invoke(state["messages"])}

# removes the messages from list except the last four
def removeMessages(state:MessagesState):
    filteredMsgs = [RemoveMessage(id = m.id) for m in state["messages"][:-4]]
    return {"messages":filteredMsgs}