import os
from time import sleep

def menu():
    print("--------------------------------------------------------------")
    print("Bem-vindo ao SisIA! Escolha o que deseja fazer:")
    print("1. Conversar com o chatbot")
    print("2. Sair do programa")
    input_choice = input("Escolha o que deseja: ")
    match input_choice:
        case "1":
            print("Conectando ao SisIA...")
            sleep(2)
            print("SisIA conectado! Você pode começar a conversar.")
        case "2":
            print("Saindo do programa...")
            sleep(2)
            print("Programa encerrado. Até a próxima!")
            exit()
    print("--------------------------------------------------------------")



