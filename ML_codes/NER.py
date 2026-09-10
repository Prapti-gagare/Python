import spacy

# -------------------------------------------------
# 1. Load pretrained English NLP model
# -------------------------------------------------

nlp = spacy.load("en_core_web_sm")

# -------------------------------------------------
# 2. Input text
# -------------------------------------------------

text = """
Sundar Pichai is the CEO of Google.
He lives in California and visited London
on January 15, 2026.
"""

# -------------------------------------------------
# 3. Process text
# -------------------------------------------------

doc = nlp(text)

# -------------------------------------------------
# 4. Display entities
# -------------------------------------------------

print("Named Entity Recognition")
print("------------------------")

for entity in doc.ents:

    print(
        f"Entity: {entity.text}"
    )

    print(
        f"Label: {entity.label_}"
    )

    print(
        f"Description: {spacy.explain(entity.label_)}"
    )

    print("------------------------")