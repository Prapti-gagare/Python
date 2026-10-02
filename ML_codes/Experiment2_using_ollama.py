
import ollama

# Read the provided context file
with open("context.txt", "r", encoding="utf-8") as file:
    context = file.read()

prompt = f"""
Use the following context to understand the intended meaning
of the question.

Context:
{context}

- Explain the answer in simple language.
- Relate your answer to the context.
- Do not use a meaning from an unrelated field.

Question: What is a crossover point?
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    options={"temperature": 0}
)

print("EXPERIMENT 2: RELEVANT CONTEXT")
print("Question: What is a crossover point?")
print("\nModel Response:")
print(response["message"]["content"])
