from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI


genai_api_key = config('GENAI_API_KEY')

# llm
llm : ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
        api_key=genai_api_key,
        model= 'gemini-1.5-flash'
    )