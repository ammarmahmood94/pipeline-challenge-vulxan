import json
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
import pandas as pd



def classify_topic(text: str) -> dict:

    """
    Classify the article into one of: Politics, Sports, Business, Technology, Health, Entertainment, Science.
    Returns a dict with key 'topic'.
    """
    
    template = (
        "Classify the following article text into one of these categories: Politics, Sports, Business, "
        "Technology, Health, Entertainment, Science. Return the result as a JSON object with key 'topic'.\n\n"
        "Text: {text}"
    )
    
    prompt = PromptTemplate(template=template, input_variables=["text"])
    llm = OpenAI(temperature=0)
    chain = prompt | llm
    response = chain.invoke({"text": text})
    
    try:
        result = json.loads(response)
    except json.JSONDecodeError:
        result = {"topic": "Unknown"}
    
    return result


def process_classify(df: pd.DataFrame, content_column: str = "content") -> pd.DataFrame:
    
    """
    Process a DataFrame of articles by extracting filtered entities for each article.
    """

    df["topic"] = df[content_column].apply(classify_topic)
    
    return df