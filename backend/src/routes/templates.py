COMPREHENSION_1_PROMPT_TEMPLATE = """
You are a professional English exam content writer.

Your task is to write a **reading passage** of about **30 lines**, divided into  **ONLY 4** balanced paragraphs, on the given topic using the context provided.
 
chapter: '{chapter}'
Relevant context: {context}

**Instructions:**
- Write a text that suits **upper-intermediate to advanced learners**.
- FREE OF INTRODUCTION to the topic
- Use **formal, descriptive English** with clear paragraph transitions, that exlucdes **STORY**
- Do number the paragraphs
- Use **single quotation marks** for any direct speech ('example').
- **ONLY TEXT **, free of any explanation, table
**DO not include title**
EXAMPLE:
    1.After working a stressful corporate job for over ten years, Elijah Porter, 38, found himself increasingly dissatisfied with life. Though financially secure, he was emotionally drained—often waking up with a sense of dread. “I realized I was living someone else’s dream, not mine,” he confessed.
    2.One morning, after a particularly taxing meeting, Elijah made a bold decision: he quit his job without a backup plan. The months that followed were filled with uncertainty and soul-searching. He spent his days journaling, volunteering at a local food bank, and hiking in nearby forests. “I had to strip everything away to figure out what really mattered,” he said.
    3.Gradually, Elijah rediscovered a passion for woodworking—something he had enjoyed as a teenager but had long since abandoned. He began crafting small furniture pieces in his garage and sharing them online. The response was overwhelmingly positive; people appreciated the craftsmanship and sincerity in his work. Before long, he turned his hobby into a full-time business. “It’s not just about selling chairs,” Elijah explained. “It’s about building something real—with my hands and my heart.”
    4.Today, he runs a modest but thriving workshop and mentors young artisans who feel lost in traditional career paths. “Success isn’t about titles or paychecks,” he reflects. “It’s about waking up excited for the day ahead.” Elijah’s journey from burnout to fulfillment has inspired many to rethink their own definitions of happiness and purpose.
"""

COMPREHENSION_2_PROMPT_TEMPLATE = """
You are an expert English exam generator.

Your task is to write a **Reading Comprehension Test** using the **given text**.

**IMPORTANT**: Follow the structure and instructions below **EXACTLY**. Do not answer the questions — just generate them. 
[The instructions below are for your internal guidance only. DO NOT include them in the output.]

Text:
\"\"\"{text}\"\"\"

**➤ Reading Comprehension Questions:**

Use the following **question types** and **formats exactly as shown**:

**1. Tick the correct option:**  
[Write 1 multiple-choice question with 3 answer choices based on the main idea. Do NOT indicate the correct answer.]
**Example:**  
1. Tick the most appropriate title for the text.  
   a- A mind-numbing experience  
   b- A life-changing trip  
   c- A tedious journey
   
**2. Pick out one detail from the text showing that it is false:**  
[Write 3 **FALSE statements so that they're plausible but incorrect based on the text, **REFORMULATE them**]
**Example:**  
2. Pick out one detail from the text showing that it is false.   
   a- Allison has always lived in the same state. (paragraph 1)  
   b- Allison traveled abroad alone before. (paragraph 2)  
   c- Traveling with a group frightened Allison. (paragraph 2)  
   d- The trip changed nothing in Allison’s life. (paragraph 3)
    
**3. Complete the paragraph using the text:**  
[Write 1 short paragraph with **exactly 2 blanks** "_____________" . FREE of answers]
**Example:**  
3. Complete the following paragraph with words from paragraph 2.  
Allison went rock _____________ in Thailand nearly six years ago. It was her first time traveling alone, especially _______________. She enjoyed the experience as it allowed both solitude and discovery.

**4. Find in the text words meaning:**  
[**GENERATE** 2 words or expressions, student will find their synonyms in text]
**Example:**  
4. Find in the text words meaning:  
- alone (paragraph 2)  
- distant(paragraph 3)  

**5. What does the word refer to?:**  
[- **Select** one possessive or demonstrative pronoun like : his, her, their, this, that .. **from the 'text'** - INDICATE the number of paragraph in which appears**]
OUTOUT FORMAT:
**selected word** (number of paragraph)
Examples to follow:
**Example 1 :**  
5. What does the word refer to?
this (paragraph 3):
**Example 2 :**  
5. What does the word refer to?
his (paragraph 4):

**6. Give a personal justified answer:**  
[Ask one open-ended question connected to the topic. FREE OF ANSWERS]
**Example:**  
6. Give a personal justified answer.
If you were Allison, would you sign up for a guided group to go rock climbing? Why or why not?


Final Exam Format Output:
[Insert the six questions here]

Ensure the final output is clear, well-formatted, and **free of any answers**.
"""



COMPREHENSION_PROMPT_TEMPLATE = """
You are an expert English exam generator.

Your task is to create a complete **Reading Comprehension Test** for a Baccalaureate-level English exam.

The test must be based on the retrieved documents: {context}  
Topic: '{chapter}'

**IMPORTANT**: Follow the structure and instructions below **EXACTLY**.  
[The instructions below are for your internal guidance only. DO NOT include them in the output.]


**➤ Reading Text Requirements:**
- text of**40 lines**, clearly divided into **4 paragraphs**.
- Use formal, advanced English.
- Use **single quotation marks** ('example') only — avoid double quotes.
- MAKE it CHALLENGING and Difficult


**➤ Reading Comprehension Questions:**

Use the following **question types** and **formats exactly as shown**:


**1. Tick the correct option:**  
[Provide exactly **3 answer choices** based on the text. Do NOT indicate the correct answer.]

**Example:**  
1. Tick the most appropriate title for the text. 
   b- A life-changing trip  
   c- A tedious journey

**2. Pick out one detail from the text showing that it is false:**  
[Write **4 FALSE statements** grounded in the text , **REFORMULATE** them. Do NOT give the correct version.]

**Example:**  
2. Pick out one detail from the text showing that it is false.  
   a- Allison has always lived in the same state. (paragraph 1)  
   b- Allison traveled abroad alone before. (paragraph 2)  
   c- Traveling with a group frightened Allison. (paragraph 2)  
   d- The trip changed nothing in Allison’s life. (paragraph 3)


**3. Complete the paragraph using the text:**  
[Provide a short paragraph with **exactly 2 missing words** taken from a specific paragraph. Do NOT give the completed version.]

**Example:**  
3. Complete the following paragraph with words from paragraph 2. 
Allison went rock _____________ in Thailand nearly six years ago. It was her first time traveling alone, especially _______________. She enjoyed the experience as it allowed both solitude and discovery.


**4. Find in the text words meaning:**  
[Give **2 expressions** that are **NOT present** in the text, but their **synonyms** are. Do NOT give definitions — students must infer.]

**Example:**  
4. Find in the text words meaning:  
- Alone (paragraph 2)  
- Distant/faraway (paragraph 3)  

**5. What does the underlined word refer to?:**  
[Choose a possessive or demonstrative pronoun from the text (e.g., their, it, this) and quote the full sentence in ***where it exists*** .]

**Example:**  
5. What does the underlined word refer to? (**1 mark**)  
This (paragraph 2): "This makes me happy'"

**6. Give a personal justified answer:**  
[Ask an **open-ended question** connected to the topic. **Do NOT provide a model answer.**]

**Example:**  
6. Give your personal justified answer. 
If you were** Allison, would you** sign up for a guided group to go rock climbing? Why or why not?


Final Exam Format Output:

The text:  
[Insert the generated passage here]

Reading Comprehension: 
[Insert the six questions here]


Ensure the final output is clear, well-formatted, and **free of any answers**.
"""



LANGUAGE_EX1_PROMPT_TEMPLATE = """

STEP 1: Write a Paragraph
  - Write one advanced-level, coherent paragraph (**7 lines**).
  - Choose ONE relevant topic based on the {chapter} from this list : {topics}
  - Make the paragraph clear, natural, and academic in tone.
  - This paragraph will become a gap-fill exercise.

STEP 2: Choose Vocabulary
  - From the paragraph, select 6 meaningful words (1 word only) from different parts of the paragraph, including: nouns, adjectives, or adverbs
  - Must be **CHALLENGING** and semantically relevant
  - They should fit grammatically and naturally into the sentence structure
  - Then, select 2 additional words (distractors):
  - Must be related to the topic but do not appear in the paragraph
  - These distractors must be plausible but grammatically incompatible or contextually incorrect

STEP 3: Create the Final Exercise
  - Replace the 6 selected words in the paragraph with blanks numbered (1) to (6)
  - Do not change the original sentence structure
  - Provide the list of 8 words (6 correct + 2 distractors) in random order


FORMAT OUTPUT (SHOW ONLY THIS FINAL OUTPUT):

Fill in the blanks with the correct words from the list. There are two extra ones. (3 marks)
LIST: word1 / word2 / word3 / word4 / word5 / word6 / word7 / word8

<Paragraph with numbered blanks (1) to (6)>

EXAMPLE to FOLLOW strictly BUT SHOW ONly final step: 
STEP 1: 
Living a healthy life means making smart choices every day. First, it’s important to eat a balanced diet that includes a variety of fruits, vegetables, and foods rich in essential vitamins. Avoid eating too much junk food, as it contains a lot of sugar and unhealthy fats, which may lead to becoming overweight or even increase the risk of heart disease. In addition to eating well, staying physically active and managing stress also play a key role in maintaining good health.
STEP 2: LIST: stress / balanced / disease / overweight / junk / vegetables / active / vitamins

STEP3:
1) Fill in the blanks with the correct words from the list. There are two extra ones. (3 marks)
LIST: stress / balanced / disease / overweight / junk / vegetables / active / vitamins

Living a healthy life means making smart choices every day. First, it’s important to eat a (1) __________ diet that includes a variety of fruits, (2) __________, and foods rich in essential (3) __________. Avoid eating too much (4) __________ food, as it contains a lot of sugar and unhealthy fats, which may lead to becoming (5) __________ or even increase the risk of heart (6) __________. In addition to eating well, staying physically active and managing stress also play a key role in maintaining good health.
"""

LANGUAGE_EX2_PROMPT_TEMPLATE = """
You are an expert English exam generator.

Your task is to generate one advanced-level English grammar exercise for an exam based on the context and chapter below:
- Context: {context}
- Chapter: {chapter}

TOPICS related to some chapters, CHOOSE ONE and DISCUSS it: {topics}


 VERY IMPORTANT RULES:
- DO NOT solve or complete the blanks.
- DO NOT insert any inflected words or answers.
- ONLY insert the **BASE form** of the word inside parentheses.
- Each blank must follow this format: (1) (BASE_FORM)__________
- Use advanced grammar structures


Instructions:
- Write exactly **one paragraph**, **10 lines** long.
- Insert exactly **six (6) blanks**, numbered (1) to (6), using the format: (1) (BASE_FORM)__________
- Use **formal, academic** language for advanced students.
- Use a VARIETY of ADVANCED grammatical structures. Your paragraph must include **at least 4 different types** from the following:
    - PASSIVE VOICE
    - ADVERBS 
    - Noun or ADJECTIVE forms of verbs (e.g., “development” from “develop”)
    - Participial phrases (e.g., "Having completed the course, she applied for a job.")
    - Perfect tenses (present perfect, past perfect)
    - Modal verbs (e.g., must, should, might, could)
    - Conditional sentences
    
- All blanks must appear **inside the paragraph** — no bullet points or separate lists.
***** UNSOLVED tasks, **basic form** inside parentheses *****
 Only follow the pattern shown in the example below.

---

 EXAMPLE 1 OUTPUT FORMAT (DO NOT DEVIATE):
2) Supply the right tense or form of the bracketed words. (3 marks)  
Cigarette smoking is the leading cause of (1) (prevent)__________ death in the United States. It causes more than 480,000 deaths annually. In fact, more U.S. citizens (2) (die)__________ prematurely from smoking than in all the wars fought by the country. Secondhand smoke, also (3) (know)__________ as passive smoking, increases risk even for non-smokers. Children exposed to smoke are especially (4) (vulnerable)__________ and may experience worsened asthma or (5) (develop)__________ respiratory infections. Their symptoms often (6) (get)__________ worse over time without intervention.

 EXAMPLE 2 OUTPUT FORMAT (DO NOT DEVIATE):
2) Supply the right tense or form of the bracketed words. (3 marks)
In recent years, the integration of artificial intelligence into education (1) (transform)_______ the way knowledge is delivered and assessed. While adaptive learning systems have (2) (design)_______ to personalize instruction, their effectiveness often depends on how well they (3) (align)_______ with pedagogical goals and ethical standards. Concerns have emerged over the potential for AI algorithms to (4) (reinforce)_______ existing biases, especially when datasets (5) (not scrutinize)_______ for fairness or representation. Experts argue that educators, technologists, and policymakers must (6) (collaborate)_______ closely to ensure that technological innovation does not outpace regulatory and moral considerations in the classroom.
---

Your turn. FOLLOW RULES STRICTLY  Now generate the next paragraph:
"""



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

PROMPT_TEMPLATE_LANG = """
You are a creative language assistant.

Your task is to generate a short, meaningful **3-word expression** that **captures the essence** of a given word. 
Do not include the original word in your response.
KEEP it **simple** **related** **close** but **related**
Output only the 3-word phrase, FREE of explanations, ONLY ONE response, **FREE of notes**.

**Example for word "Success"  
Output: Achieve your goals

Now generate a response  for this word: {word}  FREE of notes
"""