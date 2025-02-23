import json
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
import pandas as pd



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


def process_summary(df: pd.DataFrame, content_column: str = "content") -> pd.DataFrame:
    
    """
    Process a DataFrame of articles by extracting filtered entities for each article.
    """

    df["summary"] = df[content_column].apply(summarize_text)
    
    return df
