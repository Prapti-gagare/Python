import json
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

CACHE_FILE = "qa_cache.json"
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE,"r") as f:
        cache = json.load(f)
else:
    cache = {}
    
def generate_story(idea):
    llm = ChatOllama(model="llama3.2",temperature =0.8)
    prompt=ChatPromptTemplate.from_messages([("system","You are a fiction or fantasy writer. Write a short story""(500-900 words)based on the user's idea.keep names,""places and facts consistent throughout."),("human",idea)])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({})

def answer_question(story,question):
    key = question.strip().lower()
    if key in cache:
        return cache[key]
    llm = ChatOllama(model="llama3.2",temperature=0)
    prompt = ChatPromptTemplate.from_messages([("system","Answer the question using only this story\n"+story),("human",question),])
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({}).strip()
    cache[key] = answer
    with open(CACHE_FILE,"w") as f:
        json.dump(cache,f,indent=2)
    return answer

if __name__=="__main__":
    idea = input("Story idea:")
    story = generate_story(idea)
    print("\n"+story+"\n")
    
    while True:
        question = input("Ask a question:")
        if(question.lower() in ("quite","exit","")):
            break
        print("Answer:",answer_question(story,question),"\n")
        