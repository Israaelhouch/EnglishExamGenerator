from backend.src.utils.language import language_templates 
from backend.src.utils.generation_fuctions import generate_response
#from backend.src.utils.constants import CHROMA_PATH_LANGUAGE_EX1, CHROMA_PATH_LANGUAGE_EX2


CHROMA_PATH_LANGUAGE_EX1 = "backend/src/utils/language/db_language_ex1"
CHROMA_PATH_LANGUAGE_EX2 = "backend/src/utils/language/db_language_ex2"

def format_language(random_chapter:str, possible_topics_of_random_chapter: str):
    
    language_ex1 = generate_response("Language", random_chapter, language_templates.LANGUAGE_EX1_PROMPT_TEMPLATE, CHROMA_PATH_LANGUAGE_EX1, possible_topics_of_random_chapter)
    language_ex2 = generate_response("Language", random_chapter, language_templates.LANGUAGE_EX2_PROMPT_TEMPLATE, CHROMA_PATH_LANGUAGE_EX2, possible_topics_of_random_chapter)
    
    result = "Language:\n\n" + language_ex1 + "\n\n" + language_ex2 
    return result