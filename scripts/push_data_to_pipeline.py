import os
import sys 

import pandas as pd
from dotenv import load_dotenv
import openai

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Set project_root to the parent directory of the current directory
project_root = os.path.abspath(os.path.join(current_dir, '..'))

if project_root not in sys.path:
    sys.path.append(project_root)

from pipeline.preprocess import load_data, preprocess_articles
from pipeline.ner import process_ner
from pipeline.topic_classification import process_classify
from pipeline.sentiment_analysis import process_sentiment
from pipeline.summarization import process_summary



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
    df = process_ner(df)
    print(df.head(10))

    # Obtain Topic Classification
    df = process_classify(df)
    print(df.head(10))

    # Obtain Sentiment Analysis
    df = process_sentiment(df)
    print(df.head(10))

    # Obtain Summarization
    df = process_summary(df)
    print(df.head(10))



if __name__=="__main__":

    # Load environment variables from .env file
    load_dotenv()

    # Set your OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file.")

    openai.api_key = api_key    
    main()