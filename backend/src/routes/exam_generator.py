import os
import random
import re
from pathlib import Path

from backend.src.routes import templates
from backend.src.routes.modify_outputs import adjust_comprehension
from backend.src.routes.utils import generate_response, generate_questions, oraganize_text 

BASE_DIR = Path(__file__).resolve().parent

CHROMA_PATH_COMPREHENSION_1 = str(BASE_DIR / "exam_generator/backend/db_store/db_comprehension_1_store")
CHROMA_PATH_COMPREHENSION_2 = str(BASE_DIR / "exam_generator/backend/db_store/db_comprehension_2_store")
CHROMA_PATH_LANGUAGE_EX1 = str(BASE_DIR / "exam_generator/backend/db_language_ex1")
CHROMA_PATH_LANGUAGE_EX2 = str(BASE_DIR / "exam_generator/backend/db_store/db_language_ex2")
CHROMA_PATH_WRITING_EX1 = str(BASE_DIR / "exam_generator/backend/db_store/db_ex1")
CHROMA_PATH_WRITING_EX2 = str(BASE_DIR / "exam_generator/backend/db_store/db_ex2")


topics = {
        "Education matters": "Education matters, Education matters, Education matters, Dropping out of school",
        "Life issues" : "Attitudes, Ecodriving, Urban Exxodus, smoking, poverty, lifestyle, well-being, health",
        "Creative, inventive minds" : "Robots, Prize Winners, Brain Drain, Scientists' Achievements",
        "Art shows and holidaying" : "Holidaying, Art shows, Package Tour, Travel Agency"
        }

def choose_chapters(n:int):
    
    """print("Chapters:\n1- Education matters\n2- Life issues\n3- Art shows and holidaying\n4- Creative, inventive minds")
    
    n = int(input("Choose one: "))
    while not( 1<= n & n<=4) :
        n = int(input("Choose one again: "))"""   

    chapters = ["Education matters", "Life issues", "Art shows and holidaying", "Creative, inventive minds"]
    
    chapter = chapters[n-1]
    chapters_list_to_choose_randomly = [item for item in chapters if item != chapter]
    random_chapter = random.choice(chapters_list_to_choose_randomly)
    
    return chapter, random_chapter, topics[chapter], topics[random_chapter]



def comprehension(chapter:str, possible_topics_of_chapter:str):
    comprehension_text = generate_response("Comprehension", chapter, templates.COMPREHENSION_1_PROMPT_TEMPLATE, CHROMA_PATH_COMPREHENSION_1, possible_topics_of_chapter)
    comprehension_questions = generate_questions(comprehension_text, templates.COMPREHENSION_2_PROMPT_TEMPLATE, CHROMA_PATH_COMPREHENSION_2)
    adjusted_comprehension_questions = adjust_comprehension(comprehension_questions)
    result ="The text:\n\n" + "    "+ comprehension_text + "\n\n" + "Reading comprehension:\n" + adjusted_comprehension_questions
    
    return  result



def language(random_chapter:str, possible_topics_of_random_chapter: str):
    
    language_ex1 = generate_response("Language", random_chapter, templates.LANGUAGE_EX1_PROMPT_TEMPLATE, CHROMA_PATH_LANGUAGE_EX1, possible_topics_of_random_chapter)
    language_ex2 = generate_response("Language", random_chapter, templates.LANGUAGE_EX2_PROMPT_TEMPLATE, CHROMA_PATH_LANGUAGE_EX2, possible_topics_of_random_chapter)
    
    result = "Language:\n\n" + language_ex1 + "\n\n" + language_ex2 
    return result
   
   
def writing (chapter:str, possible_topics_of_chapter:str) :
    writing_ex1 = oraganize_text(generate_response("Writing", chapter, templates.WRITING_EX1_PROMPT_TEMPLATE, CHROMA_PATH_WRITING_EX1, possible_topics_of_chapter))
    writing_ex2 = generate_response("Writing", chapter, templates.WRITING_EX2_PROMPT_TEMPLATE, CHROMA_PATH_WRITING_EX2, possible_topics_of_chapter)
    
    dotted_line = "." * 90 + "\n" 
    result = "Writing:\n\n" + writing_ex1 + "\n" + dotted_line * 4 + "\n\n" + writing_ex2 + "\n" + dotted_line * 12
    
    return result
    
    
    
def generate_exam(chapter_number:int):
    
    chapter, random_chapter, possible_topics_of_chapter, possible_topics_of_random_chapter = choose_chapters(chapter_number)
    result = comprehension(chapter, possible_topics_of_chapter) + "\n\n\n\n" + language(random_chapter, possible_topics_of_random_chapter) + "\n\n\n\n" + writing(chapter, possible_topics_of_chapter)
    #result = language(random_chapter, possible_topics_of_random_chapter)
    return chapter, result