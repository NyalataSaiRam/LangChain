from langgraph.graph import MessagesState
from genai import llm_call_tools


def call_func(state: MessagesState):
    return {"messages": llm_call_tools.invoke(state["messages"])}



