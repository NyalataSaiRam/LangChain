from states import State
from genai import llm

def nodeOne(state:State):
    
    res = llm.invoke(state["prompt"])
    return {"output": res.content}
