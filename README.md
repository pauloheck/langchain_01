# LangChain Agent com Azure OpenAI

Este projeto demonstra a implementação de um agente inteligente usando LangChain e Azure OpenAI. O agente é capaz de realizar cálculos matemáticos simples através de uma ferramenta personalizada.

## Estrutura do Projeto

```
langchain_01/
├── src/
│   ├── agent.py      # Configuração do agente LangChain
│   ├── config.py     # Configuração do modelo Azure OpenAI
│   ├── main.py       # Ponto de entrada da aplicação
│   └── tool.py       # Definição de ferramentas personalizadas
├── .env.example      # Template para variáveis de ambiente
├── pyproject.toml    # Configuração do Poetry e dependências
└── README.md         # Esta documentação
```

## Componentes Principais

### 1. Configuração (config.py)
- Inicializa o modelo Azure OpenAI
- Gerencia variáveis de ambiente usando `python-dotenv`
- Configura o modelo de chat com os parâmetros do Azure

### 2. Ferramentas (tool.py)
- Define uma ferramenta personalizada `MinhaFerramenta` para cálculos matemáticos
- Herda de `BaseTool` do LangChain
- Implementa métodos `_run` para execução síncrona
- Suporta operações matemáticas básicas através da função `eval`

### 3. Agente (agent.py)
- Inicializa o agente LangChain
- Configura memória de conversação
- Utiliza o modelo "zero-shot-react-description"
- Integra as ferramentas personalizadas com o modelo de linguagem

### 4. Aplicação Principal (main.py)
- Ponto de entrada da aplicação
- Demonstra o uso do agente com um exemplo de cálculo matemático
- Processa e exibe as respostas do agente

## Configuração do Ambiente

1. Clone o repositório
2. Copie `.env.example` para `.env` e configure suas credenciais:
   ```
   AZURE_OPENAI_API_KEY=sua_chave_api
   AZURE_OPENAI_ENDPOINT=seu_endpoint
   AZURE_OPENAI_DEPLOYMENT_NAME=nome_do_deployment
   ```

## Instalação e Execução

```bash
# Instalar dependências
poetry install

# Ativar ambiente virtual
poetry shell

# Executar o projeto
poetry run python src/main.py
```

## Dependências Principais

- `langchain`: Framework para desenvolvimento de aplicações com LLMs
- `openai`: Cliente Python para Azure OpenAI
- `python-dotenv`: Gerenciamento de variáveis de ambiente
- `poetry`: Gerenciamento de dependências e ambiente virtual

## Exemplo de Uso

O projeto atualmente demonstra um caso de uso simples onde o agente realiza um cálculo matemático:
```python
pergunta = "Quanto é 5 * 5 + 10"
resposta = agente.run(pergunta)
```

O agente irá:
1. Analisar a pergunta
2. Identificar que precisa usar a ferramenta de cálculo
3. Executar o cálculo
4. Retornar o resultado formatado