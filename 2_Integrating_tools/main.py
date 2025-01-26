
from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import HumanMessage
from nodes import call_func
from genai import tools

# this will execute the function tools decided by the llm
from langgraph.prebuilt import ToolNode, tools_condition


# MessagesState is provided by langgraph, it is similar to our defined class State
graph_builder:StateGraph = StateGraph(state_schema=MessagesState)

graph_builder.add_node('call_func',call_func)

graph_builder.add_node("tools", ToolNode(tools=tools))


graph_builder.add_edge(START, 'call_func')

# if llm uses its tool then it generate response and Ends there is self.
graph_builder.add_conditional_edges('call_func', tools_condition)

# if the llm is using our tools then it will end here
graph_builder.add_edge('tools', END)

graph = graph_builder.compile()

result = graph.invoke({"messages": HumanMessage(content="2+3")})

for m in result["messages"]:
    print(m.content)










# START -> graph.invoke() -> (algorithm decided that it has to invoke tool) -> plus() -> result -> END