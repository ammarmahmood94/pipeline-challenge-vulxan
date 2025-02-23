import os

import pandas as pd

from preprocess import load_data, preprocess_articles 


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
    print(df.head(10))


if __name__=="__main__":
    main()