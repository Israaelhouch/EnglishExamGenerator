from backend.src.utils.writing import writing_templates 
from backend.src.utils.generation_fuctions import generate_response, oraganize_text
#from backend.src.utils.constants import CHROMA_PATH_WRITING_EX1, CHROMA_PATH_WRITING_EX1


CHROMA_PATH_WRITING_EX1 = "backend/src/utils/writing/db_writing_ex1"
CHROMA_PATH_WRITING_EX2 = "backend/src/utils/writing/db_writing_ex2"

def format_writing (chapter:str, possible_topics_of_chapter:str) :
    writing_ex1 = oraganize_text(generate_response("Writing", chapter, writing_templates.WRITING_EX1_PROMPT_TEMPLATE, CHROMA_PATH_WRITING_EX1, possible_topics_of_chapter))
    writing_ex2 = generate_response("Writing", chapter, writing_templates.WRITING_EX2_PROMPT_TEMPLATE, CHROMA_PATH_WRITING_EX2, possible_topics_of_chapter)
    
    dotted_line = "." * 90 + "\n" 
    result = "Writing:\n\n" + writing_ex1 + "\n" + dotted_line * 4 + "\n\n" + writing_ex2 + "\n" + dotted_line * 12
    
    return result