import os

import pandas as pd
from dotenv import load_dotenv
import openai

from src.preprocess import load_data, preprocess_articles
from src.ner import process_dataframe


def main():

    # Organize File Path
    work_dir = "/Users/ammarmahmood/syenah-assignment/pipeline-challange-vulxun"
    file_path = os.path.join(work_dir, "data/articles.csv")
    
    # Read the File Contents
    df = load_data(file_path)

    # Display Information columns
    print(df.columns)

    # Preprocess Articles
    print("preprocessing initiated")
    df = preprocess_articles(df)

    # Retreive the named entities
    df = process_dataframe(df)
    print(df.head())

if __name__=="__main__":

    # Load environment variables from .env file
    load_dotenv()

    # Set your OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file.")

    openai.api_key = api_key    
    main()