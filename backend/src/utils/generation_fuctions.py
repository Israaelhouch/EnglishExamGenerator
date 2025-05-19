from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings

def oraganize_text(text):
    task = text[: text.find(":")+1]
    text = text[text.find(":")+1:] 
    lines = [line.strip("- ").strip() for line in text.strip().split("\n")]
    result  = task + "\n   "
    for line in lines:
        result += "- " + line + "\n   "
    
    return result 

def generate_questions(query_text: str, prompt_template: str, chroma_path: str):
    Prompt_Template = ChatPromptTemplate.from_template(prompt_template)
    prompt = Prompt_Template.format(text = query_text)
    model = Ollama(model="mistral")
    response_text = model.invoke(prompt, tempreture= 0.8)
    
    return response_text

def generate_response(exam_part:str, query_text: str, prompt_template: str, chroma_path: str, topics:str):

    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=chroma_path, embedding_function=embedding_function)

    results = db.similarity_search_with_score(query_text, k=2)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])


    Prompt_Template = ChatPromptTemplate.from_template(prompt_template)
    prompt = Prompt_Template.format(context=context_text, chapter=query_text, topics= topics)
    model = Ollama(model="mistral")
    if exam_part == "Language":
        response_text = model.invoke(prompt, tempreture= 0.8)
        while response_text.count("__________") != 6:
            response_text = model.invoke(prompt, tempreture= 0.8)   
    else :
        response_text = model.invoke(prompt, tempreture= 0.8)
        
    return response_text


