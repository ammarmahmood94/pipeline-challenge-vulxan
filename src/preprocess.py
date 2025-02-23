import pandas as pd


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


def clean_text(text: pd.DataFrame) -> pd.DataFrame:
    pass
