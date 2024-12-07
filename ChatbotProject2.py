from langchain_ollama import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
   try:
      with open(pdf_path, "rb") as file:
         reader=PdfReader (file)
         text = ""
         for page in reader.pages:
            text += page.extract_text()
         return text
   except Exception as e:
      print("Error reading PDF:", e)
      return ""


template = """
Use the provided PDF content to answer the question below.

PDF Content: {pdf_content}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")   
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation(pdf_content):
    print("Welcome to the AI Chatbot! Here you will learn about opioids! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"pdf_content": pdf_content, "question": user_input})
        print("Bot: ", result)
    
if __name__ == "__main__":
    pdf_path = r"C:\\LLM Project\\PDFs\\opioids_doc.pdf" 
    pdf_content = extract_text_from_pdf(pdf_path)
    if pdf_content:
        handle_conversation(pdf_content)
    else:
        print("Unable to load PDF content. Exiting.")

 


   