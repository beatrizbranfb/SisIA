import os
from time import sleep
from core import Core

def menu():
    if not hasattr(menu, "rag_instance"):
        menu.rag_instance = Core.RAG()      
        print("--------------------------------------------------------------")
        print("Bem-vindo ao Chatbot! Escolha o que deseja fazer:")
        print("1. Conversar com o chatbot")
        print("2. Sair do programa")
        input_choice = input("Escolha o que deseja: ")
        match input_choice:
            case "1":
                print("Conectando ao chatbot...")
                sleep(2)
                print("Chatbot conectado! Você pode começar a conversar.")
                pergunta = input("Digite sua pergunta: ")
                resultado = menu.rag_instance.rag_bot(question=pergunta)            
                print("\nRESPOSTA DO CHATBOT:")
                print(resultado["answer"])
                print("-" * 30)
            case "2":
                print("Saindo do programa...")
                sleep(2)
                print("Programa encerrado. Até a próxima!")
                exit()
        print("--------------------------------------------------------------")


while True:
    menu()

