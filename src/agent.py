from langchain.agents import  initialize_agent
from langchain.memory import ConversationBufferMemory
from config import init_llm
from tool import ferramentas

modelo = init_llm()
memoria = ConversationBufferMemory()

agente = initialize_agent(
    ferramentas,
    modelo,
    agent="zero-shot-react-description",
    verbose=True
)