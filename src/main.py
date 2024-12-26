from  agent import agente

def main():

    
    print("Iniciando o processo...")
    pergunta = "Quanto é 5 *5 +10"
    resposta = agente.run(pergunta)
    print("A resposta do agente:", resposta)

if __name__ == "__main__":
    main()
