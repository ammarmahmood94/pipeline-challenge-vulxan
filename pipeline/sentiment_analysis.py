
import json
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI


def analyze_sentiment(text: str) -> dict:
    
    """
    Analyze the article's sentiment as Positive, Negative, or Neutral.
    Returns a dict with key 'sentiment'.
    """
    
    template = (
        "Determine the overall sentiment of the following article text. "
        "Return one of: Positive, Negative, or Neutral, as a JSON object with key 'sentiment'.\n\n"
        "Text: {text}"
    )
    
    prompt = PromptTemplate(template=template, input_variables=["text"])
    llm = OpenAI(temperature=0)
    chain = prompt | llm
    response = chain.invoke({"text": text})
    
    try:
        result = json.loads(response)
    except json.JSONDecodeError:
        result = {"sentiment": "Neutral"}
    
    return result
