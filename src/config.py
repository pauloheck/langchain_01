from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv
import os

def init_llm():
    # Load environment variables
    load_dotenv()

    # Initialize the Azure OpenAI chat model
    llm = AzureChatOpenAI(
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        openai_api_version="2023-05-15",
    )
    return llm