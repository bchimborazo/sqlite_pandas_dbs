import sqlite3
from pathlib import Path
# Path to the database file
db_path = Path("clinic_simple.db")
schema_path = Path("sql/schema.sql")
# Connect to DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
# Run schema
with open(schema_path, "r") as f:
    schema_sql = f.read()
cursor.executescript(schema_sql)
conn.commit()
conn.close()
print(" Database created with schema applied")