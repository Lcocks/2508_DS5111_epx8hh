


import sys
import os
sys.path.append("../.")

import pandas as pd


def process_volume(x):

    x = str(x).replace(',', '')  # Remove commas

    if 'M' in x:
        # Strip the M and get the number
        num = float(x.strip('M'))
        # If the number is greater than 1000, it's likely raw count that needs conversion
        if num > 1000:
            return str(round(num / 1_000_000, 6)) + 'M'
        else:
            # Already in millions, keep it
            return str(round(num, 6)) + 'M'
    else:
        # No M suffix, convert to millions
        return str(round(float(x) / 1_000_000, 6)) + 'M'

if __name__ == "__main__":
    import glob

    # Find all files matching ygainers*.csv
    try:
        files = glob.glob("./ygainers.csv")

        if not files:
            print("Warning: No ygainers*.csv files found")
        else:
            for filepath in files:
                try:
                    df = pd.read_csv(filepath, index_col=0)
                    print(f"\nProcessing: {filepath}")
                    print("Original data:")
                    print(df[['volume']].head(20))

                    df['volume'] = df['volume'].apply(process_volume)

                    print("\nProcessed data:")
                    print(df[['volume']].head(20))

                    # Create new filename with _c before .csv
                    base_name = filepath.rsplit('.csv', 1)[0]
                    new_filepath = f"{base_name}_c.csv"

                    df.to_csv(new_filepath, index=False)
                    print(f"\nSaved to {new_filepath}")

                except (pd.errors.EmptyDataError, pd.errors.ParserError, ValueError) as e:
                    print(f"Error processing {filepath}: {e}")

    except Exception as e:
        print(f"Error: {e}")
