import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.vectorstores import InMemoryVectorStore
from langsmith import traceable
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

class Core:
    
    class Documentation():
        def __init__(self):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            pdf_path = os.path.join(current_dir, "documentacao_v1.pdf")
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=100
            )
            doc_splits = splitter.split_documents(docs)
            embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

            vectorstore = InMemoryVectorStore.from_documents(
                documents=doc_splits,
                embedding=embedding_model 
            )
            self.retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        
    class RAG():

        def __init__(self):
            self.doc_system = Core.Documentation()
            self.llm = ChatOpenAI(
                model="gpt-4o-mini", 
                temperature=0.4, 
                api_key=os.getenv("API_KEY")
            )
        
        @traceable()
        def rag_bot(self, question: str) -> dict:
            docs = self.doc_system.retriever.invoke(question)
            docs_string = "\n".join(doc.page_content for doc in docs)
            
            instructions = f"""Você é um agente que serve para auxiliar com dúvidas relacionadas ao sistema de reservas SisAmbientes do Tribunal de Contas da União. Ele deve falar de forma fácil de entender, e que não gere dúvidas posteriores, sendo o mais claro possível. Ele deve ser cordial, considerando que está sendo utilizado para um Tribunal. A linguagem utilizada não precisa ser complexa, mas deve obrigatoriamente ser esclarecedora para as dúvidas que foram direcionadas a ele.
    Ele não pode fazer o fluxo para a pessoa que está solicitando a ajuda, devendo informar a ela que ele só pode auxiliar em como a pessoa pode realizar o que deseja, não podendo realizar reservas pelo solicitante, por exemplo. 
    Qualquer dúvida que não seja relacionada ao SisAmbientes na parte de recepção, deve ser informada que você não pode auxiliar com isso, se restringindo apenas em ajudar no sistema.
            Documentação: {docs_string}"""
            
            ai_msg = self.llm.invoke([
                {"role": "system", "content": instructions},
                {"role": "user", "content": question},
            ])

            return {"answer": ai_msg.content, "docs": docs}