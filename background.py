def load_api_key(): #Puxar a Key do arquivo .env
    import dotenv 
    import os
    dotenv.load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY não encontrada no arquivo .env")
    return api_key

def agent():
    from langchain.chat_models import ChatOpenAI
    ChatOpenAI(model="gpt-3.5-turbo", #Modelo sendo utilizado
            temperature = 0.2, #Temperatura é a "criatividade" do modelo. 
            api_key=load_api_key, 
            System_prompt='''Você é um assistente virtual que tem como função ajudar os usuários a realizar fluxos dentro de um sistema chamado SisAmbientes, utilizado pelas recepcionistas do Tribunal de Contas da União.
                Você deve lembrar que não pode realizar o fluxo pelo usuário, não podendo realizar uma reserva, por exemplo.''',
            name = "SisAgente")
    
def RAG():
    from langchain.document_loaders import PyPDFLoader #Leitor de PDF
    from langchain.text_splitter import RecursiveCharacterTextSplitter #Divisor de texto
    from langchain.embeddings import OpenAIEmbeddings #Embeddings é a transformação de texto em vetores numéricos
    from langchain.vectorstores import chroma #DB vetorial
    from langchain.chat_models import ChatOpenAI 
    from langchain.chains import RetrievalQA #Recuperação de informação e geração de texto

      



