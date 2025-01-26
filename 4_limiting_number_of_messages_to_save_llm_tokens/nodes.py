from langgraph.graph import MessagesState
from langchain_core.messages import trim_messages
from genai import llm_call_tools, llm

# invokes the llm with userInput
def call_llm(state: MessagesState):
    trimmed_msgs = trim_messages(
        state["messages"],
        strategy = "last",
        token_counter =llm,
        max_tokens = 100,
        start_on = 'human',
        end_on = ('human', 'tool'),
        include_system = False
    )
    return {"messages": llm_call_tools.invoke(trimmed_msgs)}
