import json
import pandas as pd
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI


def extract_filtered_entities(text: str) -> dict:
    
    """
    Extract only Persons, Organizations, Locations, Dates, and Events from text.
    """
    
    template = (
        "Extract the following entities from the text below. "
        "Only include these categories: Persons, Organizations, Locations, Dates, and Events. "
        "Return the result as a JSON object with keys: persons, organizations, locations, dates, events.\n\n"
        "Text: {text}"
    )
    prompt = PromptTemplate(template=template, input_variables=["text"])
    llm = OpenAI(temperature=0)
    
    # Compose the chain using the pipe operator and invoke it with the text.
    chain = prompt | llm
    response = chain.invoke({"text": text})
    
    try:
        entities = json.loads(response)
    except json.JSONDecodeError:
        entities = {"persons": [], "organizations": [], "locations": [], "dates": [], "events": []}
    
    return entities


def process_dataframe(df: pd.DataFrame, content_column: str = "content") -> pd.DataFrame:
    
    """
    Process a DataFrame of articles by extracting filtered entities for each article.
    """

    df["structured_entities"] = df[content_column].apply(extract_filtered_entities)
    
    return df