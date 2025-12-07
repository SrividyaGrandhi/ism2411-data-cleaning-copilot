#this file takes in an input file called sala_data_raw_csv and modifies each colum to syncrnize to a similer format. 
# some examples of things to re format are like replacing upercase with lowercase, getting rid of white space, handle 
# missing prices and quantities, removes rows with invaild vales
import pandas as pd

#function: laod sales_data_raw.csv from data/raw/ to use for future processing
def load_data(file_path : str) -> pd.DataFrame:
    input_data = pd.read_csv(file_path)
    return input_data

#clean data to make the colums in lowercase, no extra spaces, underscores. it will make colums easier to use consistently later
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        df[col] = df[col].str.strip()
        df[col] = df[col].str.replace(' ', '_', regex=False)
        return df


#handle missing values. drop rows missing important numeric values as it will affect calculations later and make it invaild
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in ["price", "quantity"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    required_cols = [c for c in ["price", "qty"] if c in df.columns]
    df = df.dropna(subset=required_cols)
    return df


#remove rows with invaild rows like negative prices or quantities
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
   df = df.copy()
   if "price" in df.columns: 
       df = df[df["price"] >= 0]
   if "quantity" in df.columns:
       df = df[df["quantity"] >= 0]
   return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())
