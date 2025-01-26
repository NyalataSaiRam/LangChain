from langchain_core.messages import HumanMessage, SystemMessage, RemoveMessage
from langmodel import llm
from classes import State
from langgraph.graph import END

# invokes the llm
def call_model(state : State):
    summary = state.get('summary','')

    if summary :
        system_msg = f'summary of the conversation earlier {summary}'
        messages = [SystemMessage( content=system_msg )] + state['messages']
    else :
        messages = state['messages']
    
    response = llm.invoke(messages)

    return {"messages" : [response]}


# decides when to summarize
def should_summarize(state : State) :
    """Return the next node to execute"""

    messages = state['messages']

    if len(messages) > 6 :
        return "summarize_conversation"
    
    return END


# summarizes the conversation
def summarize_conversation(state: State) :
    summary = state.get('summary','')

    if summary :
        summary_msg = (
            f'This is summary of the conversation to date : {summary}\n\n'
            "Extend the summary by taking into account the new messages above"
        )
    else :
        summary_msg = 'create a summary of the conversation above.'

    messages = state['messages'] + [HumanMessage(content=summary_msg)]

    response = llm.invoke(messages)

    remainingMsgs = [RemoveMessage( id = m.id) for m in state['messages'][:-2]]

    return {
        "summary" : response.content,
        "messages" : remainingMsgs
    }
