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
