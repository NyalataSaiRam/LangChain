from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

# add_messages() it is from langgraph. 
# it is reducer, states are maintained, 
# not overwritten. it maintains a list

class State(TypedDict):
   messages: Annotated[list, add_messages]
