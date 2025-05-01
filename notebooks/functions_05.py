import pandas as pd
def load_data(file_urls):
    """
    Loads multiple CSV files from a list of URLs into a list of DataFrames.
    
    Parameters:
        file_urls (list): List of CSV file URLs to load.
    
    Returns:
        list: List of pandas DataFrames.
    """
    return [pd.read_csv(url) for url in file_urls]



def show_heads(dfs, n=5):
    """
    Prints the first n rows of each DataFrame in a list.
    
    Parameters:
        dfs (list): List of pandas DataFrames.
        n (int): Number of rows to show from each DataFrame.
    """
    for i, df in enumerate(dfs, start=1):
        print(f"\n--- Head of DataFrame {i} ---")
        print(df.head(n))