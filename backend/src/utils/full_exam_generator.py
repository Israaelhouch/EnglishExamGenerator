import os
import random
from backend.src.utils.comprehension.generate_comprehension import format_comprehension
from backend.src.utils.language.generate_language import format_language
from backend.src.utils.writing.generate_writing import format_writing


topics = {
        "Education matters": "Education matters, Education matters, Education matters, Dropping out of school",
        "Life issues" : "Attitudes, Ecodriving, Urban Exxodus, smoking, poverty, lifestyle, well-being, health",
        "Creative, inventive minds" : "Robots, Prize Winners, Brain Drain, Scientists' Achievements",
        "Art shows and holidaying" : "Holidaying, Art shows, Package Tour, Travel Agency"
        }

def choose_chapters(n:int):

    chapters = ["Education matters", "Life issues", "Art shows and holidaying", "Creative, inventive minds"]
    chapter = chapters[n-1]
    chapters_list_to_choose_randomly = [item for item in chapters if item != chapter]
    random_chapter = random.choice(chapters_list_to_choose_randomly)
    
    return chapter, random_chapter, topics[chapter], topics[random_chapter]


def generate_exam(chapter_number:int):
    
    chapter, random_chapter, possible_topics_of_chapter, possible_topics_of_random_chapter = choose_chapters(chapter_number)
    result = format_comprehension(chapter, possible_topics_of_chapter) + "\n\n\n\n" + format_language(random_chapter, possible_topics_of_random_chapter) + "\n\n\n\n" + format_writing(chapter, possible_topics_of_chapter)

    return chapter, result