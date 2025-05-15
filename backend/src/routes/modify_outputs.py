import re
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from backend.src.routes.templates import PROMPT_TEMPLATE_LANG


dotted_line = "." * 90 

def adjust_ex2(text):
   a = text[text.find("a-") : text.find("b-")].strip()
   b = text[text.find("b-") : text.find("c-")].strip()
   c = text[text.find("c-") : text.find("d-")].strip()
   d = text[text.find("d-") :].strip()
    
   result = (
      "2. Pick out one detail from the text showing that it is false:\n"
      f"   {a}\n   {dotted_line}\n   {dotted_line}\n"
      f"   {b}\n   {dotted_line}\n   {dotted_line}\n"
      f"   {c}\n   {dotted_line}\n   {dotted_line}\n"
      f"   {d}\n   {dotted_line}\n   {dotted_line}\n"
   )

   return result


def generate_expressions(word: str):
   Prompt_Template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE_LANG)
   prompt = Prompt_Template.format(word = word)
   model = Ollama(model="mistral")
   response_text = model.invoke(prompt, tempreture= 0.8)
   
   return response_text
   
   
def adjust_ex4(text):

   keyword_lines = re.findall(r'-\s*.*\(paragraph \d+\)', text)
   print("***ORIGINAL words***:", keyword_lines)
   dotted_line = "." * 20

   result = "4. Find in the text words meaning:\n"
   
   for i in range (len(keyword_lines)):
      key_word_line = keyword_lines[i]
      word = key_word_line[key_word_line.find("-")+1 : key_word_line.find("(")-1]
      generated_expression = generate_expressions(word)
      key_word_line = key_word_line.replace(word, generated_expression)
      result += f"   {key_word_line} :  {dotted_line}\n"

   return result


def adjust_comprehension(questions):
   
   question_1 = questions[questions.find("1.") : questions.find("2.")].strip()
   question_2 = adjust_ex2(questions[questions.find("2.") : questions.find("3.")].strip())
   question_3 = questions[questions.find("3.") : questions.find("4.")].strip()
   question_4 = questions[questions.find("4.") : questions.find("5.")].strip()
   question_4 = adjust_ex4(question_4)
   question_5 = questions[questions.find("5.") : questions.find("6.")].strip() + "\n" + dotted_line
   question_6 = questions[questions.find("6.") :] + "\n" + dotted_line + "\n" + dotted_line
   
   result =question_1 + "\n\n" + question_2 + "\n\n" + question_3 + "\n\n" + question_4 + "\n\n" + question_5 + "\n\n" + question_6 
   return result