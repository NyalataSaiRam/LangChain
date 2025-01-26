from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from classes import State
from nodes import call_model, summarize_conversation, should_summarize
from langchain_core.messages import HumanMessage

# internal storage of conversations
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

# maintains different session for different thread_id
conn = sqlite3.connect('checkpoint.sqlite', check_same_thread=False)

# initialize memory
memory = SqliteSaver(conn)

# configure conversation id's
config = {"configurable": {"thread_id": "1"}}


workFlow = StateGraph(state_schema = State)

# nodes
workFlow.add_node('conversation',  call_model)
workFlow.add_node(summarize_conversation)

# flow
workFlow.add_edge(START, 'conversation')
workFlow.add_conditional_edges('conversation', should_summarize)
workFlow.add_edge('summarize_conversation', END)

graph = workFlow.compile(checkpointer = memory)

while True :
    userInput = input('Enter prompt : ')
    if userInput == 'q' :
        break

    res = graph.invoke({"messages" : [HumanMessage( content = userInput )]}, config = config)

    print(res['messages'][-1].content)
    print('\n')
