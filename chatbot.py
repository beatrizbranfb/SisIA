import os
from time import sleep
from core import Core

def menu():
    if not hasattr(menu, "rag_instance"):
        rag_instance = Core.RAG()      
        print("--------------------------------------------------------------")
        print("Bem-vindo ao Chatbot! Escolha o que deseja fazer:")
        print("1. Conversar com o chatbot")
        print("2. Sair do programa")
        input_choice = input("Escolha o que deseja: ")
        match input_choice:
            case "1":
                print("Chatbot conectado! Você pode começar a conversar.")
                pergunta = input("Digite sua pergunta: ")

                resultado = rag_instance.rag_bot(question=pergunta)

                print("\n" + "="*10)
                print("RESPOSTA DO CHATBOT:")
                
                if isinstance(resultado["answer"], list):
                    texto_final = resultado["answer"][0].get("text", "Sem resposta.")
                else:
                    texto_final = resultado["answer"]
                    
                print(texto_final)
                print("="*10 + "\n")


while True:
    menu()

