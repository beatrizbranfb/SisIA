from langchain_huggingface import HuggingFaceEmbeddings


class Core:

    def load_api_key(): 
        import dotenv 
        import os
        dotenv.load_dotenv()
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY não encontrada no arquivo .env")
        return api_key

    def load_api_key_pc(): 
        import dotenv
        import os
        dotenv.load_dotenv()
        api_key_pc = os.getenv("API_KEY_PC")
        if not api_key_pc: 
            raise ValueError("API_KEY_PC não encontrada no arquivo .env")
        return api_key_pc
    
    def Documentation():
        from langchain_community.document_loaders import PyPDFLoader
        from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter

        loader = PyPDFLoader("documentacao_v1.pdf")
        documents = loader.load()
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,
            chunk_overlap=50,
            separators=["\n\n", "\n", " ", ""]
        )

        chunks = splitter.split_documents(documents)
        
    def RAG():
        from langchain_openai import OpenAIEmbeddings, ChatOpenAI
        from langchain_text_splitters import CharacterTextSplitter
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_community.vectorstores import InMemoryVectorStore
        from langchain_core.output_parsers import StrOutputParser
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_pinecone import PineconeVectorStore
        from pinecone import Pinecone

        chunks = Core.Documentation()
        embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=Core.load_api_key())

        embeddings_model.embed_query()

        vectorstore = InMemoryVectorStore.from_documents(chunks, embeddings_model)

        query = input("Digite sua pergunta: ")

        retriever = vectorstore.as_retriever(search_kwargs={"k":2})

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Você é um assistente do SisAmbientes, sistema do Tribunal de Contas da União, que tem como objetivo auxiliar os usuários a entenderem para que serve a parte de recepção, e como realizar fluxos para determinadas tarefas. Você deve lembrar que não pode realizar os fluxos pelo usuário, podendo assim, apenas orientá-lo sobre como realizar as tarefas desejadas que forem solicitadas."),
            ("human", "{query}")
        ])

        llm = ChatOpenAI(model="gpt-4.1-nano", 
                        openai_api_key=Core.load_api_key(),
                        temperature=0.2,
                        )
        
        llm.invoke = (query)

        chain = prompt | llm | StrOutputParser()
        response = retriever.invoke(query) 
        context = "\n\n".join([doc.page_content for doc in response])

        token_splitter = CharacterTextSplitter.from_tiktoken_encoder(encoding_name="cl100k_base", chunk_size=1000, chunk_overlap=100)
        token_pieces = token_splitter.split_text(context)

        hf_embeddings_model = HuggingFaceEmbeddings(model="intfloat/multilingual-e5-small")
        hf_embeddings = hf_embeddings_model.embed_documents(token_pieces)

    
    def PineCone():
        from langchain_pinecone import PineconeVectorStore
        from pinecone import Pinecone

        pc = Pinecone(api_key=Core.load_api_key_pc())
        pc_vector_store = PineconeVectorStore(
            host = "https://rag-sisia-60c393t.svc.aped-4627-b74a.pinecone.io",
            api_key = Core.load_api_key_pc(),
            embedding=HuggingFaceEmbeddings(model="intfloat/multilingual-e5-small")
        )
        



#emb_tokenizer = AutoTokenizer.from_pretrained("intfloat/multilingual-e5-small")
#emb_model = AutoModel.from_pretrained("intfloat/multilingual-e5-small")
#hf_splitter = CharacterTextSplitter.from_hf_tokenizer(emb_tokenizer, chunk_size=1000, chunk_overlap=100)
#hf_pieces = hf_splitter.split_text(context)
#from langchain_experimental.text_splitter import SemanticChunker
#from langchain_openai.embeddings import OpenAIEmbeddings
#semantic_openai_splitter = SemanticChunker(OpenAIEmbeddings())


        

        

        

            


