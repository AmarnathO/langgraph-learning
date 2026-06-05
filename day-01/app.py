from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import streamlit as st

# import loading env 
load_dotenv(override=True)

# loading variables
ollama_key = os.getenv("OLLAMA_API_KEY")

# llm instance 
llm = init_chat_model(
    model = "llama3.2",
    model_provider="ollama",
    temperature= 0.7
)

prompt = PromptTemplate(
    input_variables=["user_input"],
    template="You are a carrer Advisor that advice people on carrer with details plan in below format only" \
    "Skills Required: List of Soft and tech skill" \
    ", Learning Roadmap : Detail learning roadmap week by week" \
    ", Salary Range: Yearly Salary range for the carrer"
)
    

# streamli app
st.title("AI Carrer Advisor")
carrer_input = st.text_input("What career are you interested in?")
submit_button = st.button("Submit")

# invoking llm 
if submit_button and carrer_input:
    format_prompt = prompt.format(user_input=carrer_input)
    response = llm.invoke(
        format_prompt 
    )

    st.markdown(response.content)


