import json
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI


def summarize_text(text: str) -> dict:
    
    """
    Generate a concise summary of the article.
    Returns a dict with key 'summary'.
    """
    
    template = (
        "Summarize the following article text concisely while retaining its key points. "
        "Return the result as a JSON object with key 'summary'.\n\n"
        "Text: {text}"
    )
    
    prompt = PromptTemplate(template=template, input_variables=["text"])
    llm = OpenAI(temperature=0)
    chain = prompt | llm
    response = chain.invoke({"text": text})
    
    try:
        result = json.loads(response)
    except json.JSONDecodeError:
        result = {"summary": ""}
    
    return result
