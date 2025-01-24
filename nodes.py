from states import State
# from genai import llm
from random import randint

def nodeOne(state:State):

    # res = llm.invoke(state["prompt"])
    # return {"output": res.content}

    return {"output": "From node one"}


def nodeTwo(state:State):

    return {"output": "From node two"}

def nodeThree(state:State):

    return {"output": "From node three"}

def conditionalNode(state:State):

    # generate random integer between 1 and 2
    intVal : int = randint(1,2)

    if intVal == 1:
        return "nodeTwo"
    
    return "nodeThree"




