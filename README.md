# HHA 504 Assignment 2: Single-Table Patient Roster in SQLite
- Name: Blanca Chimborazo-Reyes
- In this project I used Python to create a patient database in SQLite. I loaded patient data from the patients.csv file and ran SQL queries to analyze diagnoses, procedure codes etc. 

## How To Recreate the Database
- Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
- Create the database: This creates the clinic-simple.db file and applies the schema from sql/schema.sql
```bash
   python src/create_db.py
   ```
- Load the CSV data: This imports the data from data/patients.csv into the databse
 ```bash
   python src/import_csv.py
   ```
- Run Queries
    - Open clinic_simple.db in DB Broswer for SQLite
    - Go to the "Execute DQL" tab
    - Run queries from sql/analysis.sql

## Query Results
### Query A: Total Patient Count
- Query:

```bash
SELECT COUNT(*) AS n_patients FROM patients;
   ```
- Explanation: This query counts the total number of patients in the database. The database contains 500 patient total

![QueryA](images/pic1.png)

### Query B: Top Primary Diagnoses
- Query:

```bash
SELECT primary_icd10, COUNT(*) AS n
FROM patients
GROUP BY primary_icd10
ORDER BY n DESC;
   ```
- Explanation: This query groups patients by ICD-10 diagnosis code and counts how many patients have each diagnosis. The most common diagnosis is I10 (Essential Hypertension) with 81 patients, followed by E11.9 (Type 2 Diabetes) with 73 patients.

![QueryB](images/pic2.png)

### Query C: Recent 
- Query:

```bash
SELECT patient_id, last_cpt, last_visit_dt
FROM patients
WHERE last_cpt LIKE '992%' AND last_visit_dt >= '2025-01-01'
ORDER BY last_visit_dt DESC;
   ```
- Explanation: This query finds office visit procedures (CPT codes starting with 992) since January 1, 2025. 94 patients had office visits in 2025, with the most recent visits occurring in September 2025.

![QueryC](images/pic3.png)

### Query D
- Query:

```bash
SELECT
  patient_id,
  birth_date,
  last_visit_dt,
  CAST((julianday(date('now')) - julianday(birth_date)) / 365.25 AS INT) AS age_years
FROM patients
ORDER BY age_years DESC
LIMIT 5;
   ```
- Explanation: This query calculates patient ages and show the 5 oldest patients. The five oldest patients are all 85 years old, born in 1940.

![QueryD](images/pic4.png)

### Query E
- Query:

```bash
SELECT *
FROM patients
WHERE primary_icd10 = '' OR last_cpt = '';
   ```
- Explanation: This query check for any records with blank diagnosis or procedure codes. Based on the results, no data quality issues were found, all patient records have complete diagnosis and procedure codes.

![QueryE](images/pic5.png)