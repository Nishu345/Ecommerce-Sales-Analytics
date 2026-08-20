import pandas as pd

# =========================
# LOAD DATA
# =========================
file_path = "data/raw/Ecommerce_Unclean_Project.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print("Rows and Columns:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# =========================
# INITIAL INSPECTION
# =========================
print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

print("\n--- Data Types ---")
print(df.dtypes)

# =========================
# DATA CLEANING
# =========================

# 1. Remove completely duplicate rows
df = df.drop_duplicates().copy()

# 2. Clean Discount
df["Discount"] = df["Discount"].replace(r"^\s*$", pd.NA, regex=True)
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")

# 3. Convert Qty and Unit_Price to numeric
df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")

# 4. Convert dates.
# format="mixed" handles the dataset's mixed date formats such as
# 30-06-2025 and 2025/03/21.
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"].astype("string").str.strip(),
    dayfirst=True,
    errors="coerce",
    format="mixed"
)

df["Delivery_Date"] = pd.to_datetime(
    df["Delivery_Date"].astype("string").str.strip(),
    dayfirst=True,
    errors="coerce",
    format="mixed"
)

# 5. Fill missing numeric values
df["Qty"] = df["Qty"].fillna(df["Qty"].median())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())
df["Discount"] = df["Discount"].fillna(0)

# 6. Feature Engineering
df["Gross_Amount"] = df["Qty"] * df["Unit_Price"]

df["Discount_Amount"] = (
    df["Gross_Amount"] * df["Discount"] / 100
)

df["Net_Amount"] = (
    df["Gross_Amount"] - df["Discount_Amount"]
)

df["Delivery_Days"] = (
    df["Delivery_Date"] - df["Order_Date"]
).dt.days

# =========================
# VALIDATION
# =========================
print("\n--- Cleaning Completed ---")
print(df.head())

print("\n--- Remaining Missing Values ---")
print(df.isnull().sum())

print("\n--- Final Shape ---")
print(df.shape)
print("\n--- MySQL Connection ---")

from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = input("Enter MySQL root password: ")

safe_password = quote_plus(password)

engine = create_engine(
    f"mysql+pymysql://root:{safe_password}@localhost:3306/ecommerce_analytics"
)

with engine.connect() as connection:
    print("MySQL connection successful!")

df.to_sql(
    "ecommerce_orders",
    con=engine,
    if_exists="replace",
    index=False
)

print("\n--- Data Uploaded to MySQL Successfully ---")
print("Rows uploaded:", len(df))