from chatbot import ChatBot

# Crie uma instância do ChatBot
myChatBot = ChatBot()
# Apenas carregar um modelo pronto
# myChatBot.loadModel()

# Criar o modelo
myChatBot.createModel()

print("Bem-vindo ao Chatbot PIPE")

pergunta = input("Como posso te ajudar?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + " [" + intencao[0]['intent'] + "]")

while (intencao[0]['intent'] != "despedida"):
    pergunta = input("Posso lhe ajudar com algo mais?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)

    #  intenção "etapas" e suas dependências
    if intencao[0]['intent'] == "etapas":
        pergunta_etapas = input("Você quer saber mais sobre qual Fase (Fase 1, Fase 2, ou Fase 3)?\n")
        if pergunta_etapas == "etapa1":
            resposta = "Fase 1: Verificação da viabilidade técnico-científica da proposta (até 9 meses de duração e orçamento de até R$ 300.000, mais Reserva Técnica e Benefícios Complementares)."
        elif pergunta_etapas == "etapa2":
            resposta = "Fase 2: Execução da pesquisa propriamente dita (até 24 meses de duração e orçamento de até R$ 1.500.000, mais Reserva Técnica e Benefícios Complementares)."
        elif pergunta_etapas == "etapa3":
            resposta = "Fase 3: Desenvolvimento comercial e industrial dos produtos, processos, sistemas e/ou serviços inovadores obtidos a partir de pesquisas anteriores realizadas pela pequena empresa."
        else:
            resposta = "Desculpe, não entendi qual fase você deseja saber mais."

    print(resposta + " [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
