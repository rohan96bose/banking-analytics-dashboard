
import pandas as pd
import numpy as np
from pathlib import Path

def clean_banking_data(input_path, output_path):
    # Load data
    df = pd.read_excel(input_path)

    # Fill missing values
    df.fillna(0, inplace=True)

    # Convert date columns
    if 'Joined Bank' in df.columns:
        df['Joined Bank'] = pd.to_datetime(df['Joined Bank'], errors='coerce', dayfirst=True)

    # Create Income Band
    if 'Estimated Income' in df.columns:
        bins = [0, 100000, 300000, float('inf')]
        labels = ['Low', 'Mid', 'High']
        df['Income Band'] = pd.cut(df['Estimated Income'], bins=bins, labels=labels, include_lowest=True)

    # Create Age Band
    def age_band(age):
        if age >= 18 and age <= 30:
            return "18-30"
        elif age <= 45:
            return "31-45"
        elif age <= 60:
            return "46-60"
        else:
            return "60+"

    if 'Age' in df.columns:
        df['Age Band'] = df['Age'].apply(age_band)

    # Export cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    input_file = Path("Banking.xlsx")  # Change to your actual file path
    output_file = Path("banking_clean.csv")
    clean_banking_data(input_file, output_file)
