from langchain_groq import ChatGroq 
import streamlit as st
from langchain_core.prompts import PromptTemplate
model = ChatGroq(model = "llama-3.3-70b-versatile",
                 api_key = st.secrets["GROQ_API_KEY"])

st.header(" Asking for tv features ")
Input1 = st.selectbox(" select Which company TV you need know about ",["Samsung","LG","Sony","1+"])
Input2 = st.selectbox("Select what feature to want to know about ",["Screen Size", "Resolution", "Smart TV", "HDR Support", "Refresh Rate", "OLED/QLED/LED", "Dolby Audio", "Bluetooth", "WiFi Built-in", "Voice Control"])
Input3 = st.selectbox("In how much size you want output",["Short (1-2 paragraph)","Normal 3-4 paragraph)","Long (5-6 paragraph)"])

template = PromptTemplate(
    template="You are a TV expert. Company: {company}, Feature: {feature}, Explain in {length}.",
    input_variables=["company", "feature", "length"]
)
st.text("Tap ask for output")
button = st.button("Ask")
if button:
    st.success(" Wait for just a sec")
    prompt = template.invoke(
        {
            "company" : Input1,
            "feature" : Input2,
            "length" : Input3
        }
    )
    responce = model.invoke(prompt)
    st.write(responce.content)