from langgraph.graph import StateGraph, START, END
from states import State
from nodes import nodeOne


# graph Definition
graph_builder = StateGraph(state_schema=State)

# adding nodes
graph_builder.add_node('nodeOne', nodeOne)

#defining edges
graph_builder.add_edge(START, 'nodeOne')
graph_builder.add_edge('nodeOne', END)

# compile graph
graph = graph_builder.compile()


# invoking the graph
res = graph.invoke({"prompt": "define llm"})
print(res['output'])

