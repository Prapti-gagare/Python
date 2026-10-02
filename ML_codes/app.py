import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(
    page_title="Chatbot with ollama",
    layout="centered",
)

st.title("Chatbot")
st.caption("Built with Streamlit, Langchain and Ollama Llama 3.2")

llm = ChatOllama(
    model="llama3.2",
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a friendly and helpful conversational assistant.
        You will answer the user's questions to the best of your ability.
        If you do not know the answer, say so honestly.
        Instructions:
        1. Answer the user's questions accurately.
        2. Use simple language.
        3. Maintain the context of the conversation.
        4. If the question is not clear, ask for clarification.
        5. Use examples if needed to explain concepts.
        6. Only give sure answers.
        """,
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

chain = prompt | llm

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.header("Chatbot with ollama")
    st.write("Model: Llama 3.2")
    st.write("Backend: Ollama")
    st.write("Chain: template -> LLM")

    if st.button("New conversation"):
        st.session_state.messages = []
        st.session_state.history = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me anything")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
    })
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = chain.invoke({
                    "question": user_input,
                    "history": st.session_state.history,
                })
                answer = response.content
                st.markdown(answer)
                st.session_state.history.extend([
                    HumanMessage(content=user_input),
                    AIMessage(content=answer),
                ])
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                })
            except Exception as e:
                st.error(
                    "Could not connect to Ollama. "
                    "Make sure Ollama is running and llama3.2 is installed."
                )
                st.caption(f"Technical details: {e}")
