import os, dotenv
from langchain_openai import OpenAiEmbeddings
from langchain_openai import ChatOpenAI

def load_api_key():
    dotenv.load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY não encontrada no arquivo .env")
    return api_key

def agent():
    ChatOpenAI(model="gpt-3.5-turbo",
                   temperature = 0.2,
                   api_key=load_api_key,
                   System_prompt='''Você é um assistente virtual que tem como função ajudar os usuários a realizar fluxos dentro de um sistema chamado SisAmbientes, utilizado pelas recepcionistas do Tribunal de Contas da União.
                Você deve lembrar que não pode realizar o fluxo pelo usuário, não podendo realizar uma reserva, por exemplo.''',
                    name = "SisAgente")

