from langchain.tools import BaseTool

#Exemplo de ferramenta pesonalizada
class MinhaFerramenta(BaseTool):
    name = "Calculadora Pesonalizada"
    description = "Realizar cálculos simples"

    def _run(self, query: str):
        try:
            return eval(query)
        except Exception as e:
            return f"Erro ao realizar cálculo: {str(e)}"
    
    def _arun(self, quety: str):
        raise NotImplementedError("Async não implementado")
    #Lista de ferramentas
ferramentas = [
    MinhaFerramenta(),
]