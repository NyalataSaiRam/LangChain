from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from nodes import call_func
from genai import tools

# this will execute the function tools decided by the llm
from langgraph.prebuilt import ToolNode, tools_condition

# initialize memory
memory: MemorySaver = MemorySaver()

# configure conversation id's
config = {"configurable": {"thread_id": "1"}}


sysMsg:SystemMessage = SystemMessage(content="you are math expert. you are AI Math Assistant");

# MessagesState is provided by langgraph, it is similar to our defined class State
graph_builder:StateGraph = StateGraph(state_schema=MessagesState)

graph_builder.add_node('call_func',call_func)

graph_builder.add_node("tools", ToolNode(tools=tools))


graph_builder.add_edge(START, 'call_func')

# if llm uses its tool then it generate response and Ends there is self.
graph_builder.add_conditional_edges('call_func', tools_condition)

# if the llm is using our tools then it will end here
graph_builder.add_edge('tools', 'call_func')

graph = graph_builder.compile(checkpointer=memory)


# added SystemMessage

while True:
    userInput = input("Enter Prompt: ")
    if(userInput == "q"):
        break
    # adding config as 2nd arg in graph.invoke()
    result = graph.invoke({"messages": [sysMsg, HumanMessage(content=userInput)]}, config)
    print(result["messages"][-1].content)










# START -> graph.invoke() -> (algorithm decided that it has to invoke tool) -> plus() -> result -> END