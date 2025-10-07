import pandas as pd
from sqlalchemy import create_engine
 
# Load CSV
df = pd.read_csv(r"health-sqlite-lite\data\patients.csv")
 
# Connect to SQLite
engine = create_engine("sqlite:///clinic_simple.db")
 
# Append data to patients table
df.to_sql("patients", engine, if_exists="append", index=False)
 
print(" patients.csv imported into patients table")