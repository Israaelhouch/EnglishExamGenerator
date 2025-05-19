
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
