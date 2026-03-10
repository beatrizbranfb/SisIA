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
    from langchain_community.document_loaders import UnstructuredMarkdownLoader #Leitor de markdown
    from langchain.text_splitter import RecursiveCharacterTextSplitter #Divisor de texto
    from langchain.embeddings import OpenAIEmbeddings #Embeddings é a transformação de texto em vetores numéricos
    from langchain.vectorstores import chroma #DB vetorial
    from langchain.chat_models import ChatOpenAI 
    from langchain.chains import RetrievalQA #Recuperação de informação e geração de texto

    agent = agent() 
    document = UnstructuredMarkdownLoader("documentacao_sistema.MD", mode = "single",strategy = "fast").load() #Carrega o documento markdown
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 600, chunk_overlap = 0) #Divide o texto em pedaços de 600 caracteres sem sobreposição
    chunks = text_splitter.split_documents(document) 

    for chunk in chunks:
        texto = chunk.page_content.lower()

        if "reserva" in texto or "reservar" in texto:
            chunk.metadata["categoria"] = "reserva"

        elif "cadastro" in texto or "cadastrar" in texto:
            chunk.metadata["categoria"] = "cadastro"

        elif "consulta" in texto:
            chunk.metadata["categoria"] = "consulta"

        elif "cancelamento" in texto or "cancelar" in texto:
            chunk.metadata["categoria"] = "cancelamento"   

        elif "alteração" in texto:
            chunk.metadata["categoria"] = "alteracao"

        elif "localização" in texto or "Onde fica" in texto or "como chegar" in texto:
            chunk.metadata["categoria"] = "localizacao"

        

        




