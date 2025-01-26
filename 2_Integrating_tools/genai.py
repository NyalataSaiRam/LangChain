from decouple import config
from tools import plus, divide
from langchain_google_genai import ChatGoogleGenerativeAI


genai_api_key = config('GENAI_API_KEY')

# llm
llm : ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
        api_key=genai_api_key,
        model= 'gemini-1.5-flash'
    )



# tools can be multiple, those are added in the tools list
tools = [plus, divide]


# bind_tools(tools:list), decides which function to be called, but it will not invoke the function
llm_call_tools = llm.bind_tools(tools=tools)