WRITING_EX1_PROMPT_TEMPLATE= """
You are an expert English exam generator.

Your task is to generate ONE writing exercise for an upper-intermediate to advanced English exam, based on the context and chapter provided:
- Context: {context}
- Chapter: {chapter}

TOPICS related to some chapters, CHOOSE ONE and DISCUSS it: {topics}

VERY IMPORTANT INSTRUCTIONS:
- DO NOT write any answers, completed sentences, or full paragraph ideas.
- ONLY provide a guided exercise in the form of **short note fragments**.
- Notes MUST NOT form full ideas — they should be minimal cues or keywords.
- The topic should be a biography, organization, celebration, or historical event.
- Notes should look like **keywords or phrases**, not facts explained in detail.
- The content should be intellectually **challenging** and use **upper-intermediate to advanced-level vocabulary** or concepts.
- WELL represented 
- use formal vocabulary, such as 'achievements', 'birth', 'origin', 'impact', 'founder', and 'founded in'

OUTPUT FORMAT:
- Begin the exercise with: **1) Use the following notes to write a 4-line paragraph about [TOPIC]:**
- Provide exactly **5 bullet points** in this format (ORGANIZED):
   - [keywords]
   - [keywords]
   - [keywords]
   - [keywords]
   - [keywords]

EXAMPLE 1(STRICT FORMAT TO FOLLOW):

1) Use the following notes to write a 4-line paragraph about Leonardo da Vinci:
    - Birth: April 15, 1452 
    - Origin: Vinci, Italy
    - Education: Apprentice to Andrea del Verrocchio / Florence
    - Occupations: Artist, Scientist, Engineer, Inventor, Anatomist
    - Achievements: The Last Supper, Mona Lisa, Vitruvian Man
    - Impact: Contributions/anatomy/engineering/ painting / Renaissance polymath /notebooks of sketches/ inventions
   
EXAMPLE 2 (STRICT FORMAT TO FOLLOW): 

1) Use the following notes to write a 4-line paragraph about Charles Darwin:
    - Birth: February 12, 1809 
    - Origin: Shrewsbury, England
    - Education: University of Edinburgh, Cambridge University
    - Occupation: Naturalist, Geologist, Biologist
    - Achievements: On the Origin of Species (1859) / Theory of Evolution by Natural Selection
    - Legacy: Revolutionized biology / Influenced modern genetics/ anthropology/ evolutionary theory

Your task: now generate the next writing exercise in the exact same format.
"""

WRITING_EX2_PROMPT_TEMPLATE = """
You are an expert English exam question writer.

Your task is to generate **one concise writing task instruction** (no answers, no bullet points), suitable for an **upper-intermediate to advanced English exam**.

CONTEXT:
- Chapter: {chapter}
- Related context: {context}

You MUST choose **exactly ONE topic** from the list below, based on the chapter, and base the task instruction on that topic. 
VERY IMPORTANT: The topic you choose must be **clearly mentioned and reflected in the final instruction**.

TOPICS LIST related to the chapter: {topics} 
** choose ONLY ONE from the LIST **

INSTRUCTION REQUIREMENTS:
- Write **only the task instruction** (2–3 lines max).
- Choose one of the following formats: **article**, **email**, **letter**, or **speech**.
- Start the task with: **2)**
- Do not include answers, bullet points, or sample content.
- Use vocabulary and ideas appropriate to the topic
- ask for advantages, pros, cons, benefits, causes, solutions
- End the task with: **(8 marks)**

EXAMPLE TASKS:

2) Write an article for your school magazine discussing how online learning has affected students’ study routines. Support your views with examples. (8 marks)

2) You’ve been invited to give a speech about how teenagers can contribute to protecting the environment. Include examples and practical actions. (8 marks)

Now, generate the next task. Be sure to use and clearly reflect a topic from the list above.
"""

