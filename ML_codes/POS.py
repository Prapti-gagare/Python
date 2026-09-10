import spacy

# -------------------------------------------------
# 1. Load English NLP model
# -------------------------------------------------

nlp = spacy.load("en_core_web_sm")

# -------------------------------------------------
# 2. Input sentence
# -------------------------------------------------

sentence = (
    "The intelligent student solved "
    "the difficult problem quickly."
)

# -------------------------------------------------
# 3. Process sentence
# -------------------------------------------------

doc = nlp(sentence)

# -------------------------------------------------
# 4. Display POS tags
# -------------------------------------------------

print("POS Tagging")
print("-----------")

print(
    f"{'Token':<15}"
    f"{'POS':<10}"
    f"{'Description'}"
)

print("-" * 50)

for token in doc:

    description = spacy.explain(
        token.pos_
    )

    print(
        f"{token.text:<15}"
        f"{token.pos_:<10}"
        f"{description}"
    )