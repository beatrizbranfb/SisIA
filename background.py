def load_api_key(): #Puxar a Key do arquivo .env
    import dotenv 
    import os
    dotenv.load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY não encontrada no arquivo .env")
    return api_key
    
def RAG():
    from langchain_markitdown import BaseMarkitdownLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_community.vectorstores import InMemoryVectorStore
    from langchain_core.output_parsers import StrOutputParser

    loader = BaseMarkitdownLoader("documentacao_sistema.MD") 
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_documents(documents)
    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=load_api_key())

    embeddings_model.embed_query()

    vectorstore = InMemoryVectorStore.from_documents(chunks, embeddings_model)

    query = input("Digite sua pergunta: ")

    retriever = vectorstore.as_retriever(search_kwargs={"k":2})

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente do SisAmbientes, sistema do Tribunal de Contas da União, que tem como objetivo auxiliar os usuários a entenderem para que serve a parte de recepção, e como realizar fluxos para determinadas tarefas. Você deve lembrar que não pode realizar os fluxos pelo usuário, podendo assim, apenas orientá-lo sobre como realizar as tarefas desejadas que forem solicitadas."),
        ("human", "{query}")
    ])

    llm = ChatOpenAI(model="gpt-4.1-nano", 
                     openai_api_key=load_api_key(),
                     temperature=0.2,
                     )
    
    llm.invoke = (query)

    chain = prompt | llm | StrOutputParser()
    response = retriever.invoke(query) 
    context = "\n\n".join([doc.page_content for doc in response])
    

    

     

        


