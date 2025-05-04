# cleaning_functions.py

import pandas as pd
import numpy as np



def fill_categorical_with_mode(df: pd.DataFrame, column: str):
    mode_val = df[column].mode()[0]
    df[column] = df[column].fillna(mode_val)
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df


# Convert 'date_time' column to datetime
def conv_datetime (df_web):
    df_web['date_time'] = pd.to_datetime(df_web['date_time'], errors='coerce')
    return df_web

def quick_data_report(df: pd.DataFrame):
    print("\nDataFrame shape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDescriptive statistics:\n", df.describe())


def standardize_gender(g):
    g = str(g).strip().lower()
    if g in ['f', 'female']:
        return 'f'
    elif g in ['m', 'male']:
        return 'm'
    else:
        return 'u'

def apply_to_column(df: pd.DataFrame, column: str, func):
    if column in df.columns:
        df[column] = df[column].apply(func)
    else:
        print(f"Warning: Column '{column}' not found in DataFrame.")
    return df

def merge_datasets(df_demo, df_client, df_web):
    df = pd.merge(df_demo, df_client, on='client_id', how='inner')
    df = pd.merge(df, df_web, on='client_id', how='inner')
    return df


def main_cleaning(df):
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Rename gender
    df.rename(columns={ 'gendr' : 'gender' }, inplace=True)

    # Now apply normal cleaning
    df = fill_categorical_with_mode(df, 'gender')
    df = remove_duplicates(df)
    return df
