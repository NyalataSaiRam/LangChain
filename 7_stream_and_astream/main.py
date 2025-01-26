from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from classes import State
from nodes import call_model, summarize_conversation, should_summarize
from langchain_core.messages import HumanMessage
import asyncio

# initialize memory
memory = MemorySaver()

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

async def main():
    while True :
        userInput = input('Enter prompt : ')
        if userInput == 'q' :
            break

        async for event in graph.astream_events({"messages" : [HumanMessage( content = userInput )]}, config = config, version="v1"):
            if event['event'] == 'on_chain_stream' and event['name'] == 'conversation' :
                for m in event['data']['chunk']['messages']:
                    print(m.content)

        
    
asyncio.run(main())