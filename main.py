from langgraph.graph import StateGraph, START, END
from states import State
from nodes import nodeOne, nodeTwo, nodeThree, conditionalNode


# graph Definition
graph_builder = StateGraph(state_schema=State)

# adding nodes
graph_builder.add_node('nodeOne', nodeOne)
graph_builder.add_node('nodeTwo', nodeTwo)
graph_builder.add_node('nodeThree', nodeThree)
graph_builder.add_node('conditionalNode', conditionalNode)


# flow
# START --> nodeONe --> conditionalNode --> either to nodeTwo or nodeThree --> END


#defining edges
# add_edge(arg1 : str, arg2 : str)
graph_builder.add_edge(START, 'nodeOne')

# add_conditional_edges(arg1 : str, arg2 : callable -> str)
graph_builder.add_conditional_edges('nodeOne', conditionalNode)
graph_builder.add_edge('nodeTwo', END)
graph_builder.add_edge('nodeThree', END)

# compile graph
graph = graph_builder.compile()


# invoking the graph
# invoke(arg : State)
res = graph.invoke({"prompt": "define llm"})
print(res['output'])

