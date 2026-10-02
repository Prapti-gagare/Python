
import ollama

# Structured context with an explicit definition
context = """
Genetic Algorithms.
1. Candidate solutions are represented as chromosomes.
2. Selected candidate solutions are called parents.
3. Crossover combines genetic material from parent
   chromosomes to create offspring.
4. In single-point crossover, a position is selected
   on the chromosome representation.
5. The genetic material after that position is exchanged
   between the two parents.
6. This selected position is called the crossover point.

Important:
A crossover point is the position where the chromosomes
are split for the exchange. Crossover is the overall
operation of exchanging genetic material.
"""

prompt = f"""
Role: You are a teacher of Genetic Algorithms teach it to a beginner.
Use the following structured context to answer the question.

Context:
{context}

Instructions:
1. Explain the meaning in simple language.
2. Explain how the crossover point is used.
3. Keep the answer focused on Genetic Algorithms.
4. Do not change the question.

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

print("EXPERIMENT 3: IMPROVED STRUCTURED CONTEXT")
print("Question: What is a crossover point?")
print("\nModel Response:")
print(response["message"]["content"])
