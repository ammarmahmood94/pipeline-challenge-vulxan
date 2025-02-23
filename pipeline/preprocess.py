import pandas as pd
from langdetect import detect, LangDetectException


def load_data(file_path: str) -> pd.DataFrame:
    
    """
    Load articles from a CSV File

    """

    df = pd.read_csv(
        file_path,
        dtype = {'content': str, 
            'url': str, 
            'id': str},  
        parse_dates=['publication_datetime']         
        )

    return df


def is_english(content: str) -> bool:
    
    """
    To check whether the article is in english or not
    
    """
    try:
        # detect() returns a language code, e.g., 'en' for English
        return detect(content) == 'en'

    except LangDetectException:
        # If detection fails, assume not English
        return False


def preprocess_articles(df: pd.DataFrame) -> pd.DataFrame:
    
    """
    Checks to see if the articles meet the requirements specified:

    1) Length >= 1000
    2) Articles are in English

    """

    # Filter by language and minimum length (1000 characters)
    df = df[df['content'].apply(lambda x: isinstance(x, str) and len(x) >= 1000 and is_english(x))]
    
    # Reset index after filtering
    df.reset_index(drop=True, inplace=True)
    
    return df


