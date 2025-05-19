from backend.src.utils.comprehension import comprehension_templates
from backend.src.utils.comprehension.modify_outputs import adjust_comprehension
from backend.src.utils.generation_fuctions import generate_questions, generate_response

CHROMA_PATH_COMPREHENSION_1 = "backend/src/utils/comprehension/db_comprehension_1_store"
CHROMA_PATH_COMPREHENSION_2 = "backend/src/utils/comprehension/db_comprehension_2_store"

def format_comprehension(chapter:str, possible_topics_of_chapter:str):
    comprehension_text = generate_response("Comprehension", chapter, comprehension_templates.COMPREHENSION_1_PROMPT_TEMPLATE, CHROMA_PATH_COMPREHENSION_1, possible_topics_of_chapter)
    comprehension_questions = generate_questions(comprehension_text, comprehension_templates.COMPREHENSION_2_PROMPT_TEMPLATE, CHROMA_PATH_COMPREHENSION_2)
    adjusted_comprehension_questions = adjust_comprehension(comprehension_questions)
    result ="The text:\n\n" + "    "+ comprehension_text + "\n\n" + "Reading comprehension:\n" + adjusted_comprehension_questions
    return  result