##  Normalizer for ygainers.csv and wsjgainers.csv  ##

"""
Importing 3 packages, using 2 functions to clean 2 sets fo data
 from Yahoo Finance and Wall Street Journal.
"""

import re
import pandas as pd
import numpy as np



def normalize_yahoo(df):
    """
    Normalizer for ygainers.csv
    """

    # Update the column names
    titles = ['symbol', 'company_name', 'Unnamed: 2','Price(extra)', 'change', 'perc_change',
 'volume', '3_Month_Avg_Volume', 'Market Cap', 'P/E_Ratio (TTM)', '52_Wk_Change_%', '52_Wk_Range']
    df.columns = titles
    print(df[['Price(extra)']].head())

    # Create the price column
    df['price'] = df['Price(extra)'].apply(lambda x: str(x).split()[0])
    print(df[['Price(extra)', 'price']].head())

    # Drop the unnecessary columns and reorder
    df.drop(['Unnamed: 2', 'Price(extra)', '3_Month_Avg_Volume', 'Market Cap',
 'P/E_Ratio (TTM)', '52_Wk_Change_%', '52_Wk_Range'], axis=1, inplace=True)
    df = df.iloc[:, [0, 1, 5, 2, 3, 4]]

    # Update the perc_change and volume columns
    df['perc_change'] = df['perc_change'].apply(lambda x: str(x).strip('+%'))
    df['volume'] = df['volume'].apply(lambda x: str(round(float(str(x).strip('M')), 1)) + 'M')

    # Handle missing values
    numeric_cols = ['price', 'change', 'perc_change', 'volume']  # numeric columns
    df[numeric_cols] = df[numeric_cols].replace(['nan', 'nanM'], None).fillna(np.nan)
 # convert to np.nan and infer type to handle deprecated behavior
    df = df.dropna(subset=numeric_cols)


    return df.to_csv('normalized_ygainers.csv', index=False)


def normalize_wsj(df):
    """
    Normalizer for wsjgainers.csv
    """

    # Update the column names, set the regex and apply it
    rex = r'\(([A-Z]+)\)$'
    print(df.columns)
    print(df[['Unnamed: 0']].head())
    df.rename(columns={'Unnamed: 0': 'company_name', 'Volume': 'volume',
 'Last': 'price', 'Chg': 'change', '% Chg': 'perc_change'}, inplace=True)
    df['symbol'] = df['company_name'].apply(lambda x: re.findall(rex, x)[0])
    df['company_name'] = df['company_name'].apply(lambda x: re.sub(rex, '', x))
    print(df[['company_name', 'symbol']].head())

    # Reorder
    df = df.iloc[:, [5, 0, 2, 3, 4, 1]]

    # Handle missing values
    numeric_cols = ['price', 'change', 'perc_change', 'volume']  # your numeric columns
    df[numeric_cols] = df[numeric_cols].replace(['nan', 'nanM'], None).fillna(np.nan)
 # convert to np.nan and infer type to handle deprecated behavior
    df = df.dropna(subset=numeric_cols)

    return df.to_csv('normalized_wsjgainers.csv', index=False)


if __name__ == "__main__":

    # Find and read the CSV files from anywhere in current directory tree
    try:
        normalize_yahoo(pd.read_csv('../ygainers.csv', index_col=0))
    except FileNotFoundError:
        print("Warning: ygainers.csv not found, skipping...")
    except Exception as e:
        print(f"Error processing ygainers.csv: {e}")

    try:
        normalize_wsj(pd.read_csv('../wsjgainers.csv', index_col=0))
    except FileNotFoundError:
        print("Warning: wsjgainers.csv not found, skipping...")
    except Exception as e:
        print(f"Error processing wsjgainers.csv: {e}")
