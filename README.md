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
- Description: Count the total number of patients in the database
- Query: 
 ```bash
 SELECT COUNT(*) AS n_patients FROM patients;
    ```

- Results
- Explanation: The database contains 500 patient records total.
![Query_A_Results](images/pic1.png)

### Query B: Top Primary Diagnoses
- Description: Group patients by ICD-10 diagnosis code and count how many patients have each diagnosis
- Query:
```bash
SELECT primary_icd10, COUNT(*) AS n
FROM patients
GROUP BY primary_icd10
ORDER BY n DESC;
   ```
- Results
- Explanation: The most common diagnosis is I10 (Essential Hypertension) with 81 patients
![Query_B_Results](images/pic2.png)

### Query C: Recent Office Visits
- Description: Find office visit procedures (CPT codes)
- Query:
```bash
SELECT patient_id, last_cpt, last_visit_dt
FROM patients
WHERE last_cpt LIKE '992%' AND last_visit_dt >= '2025-01-01'
ORDER BY last_visit_dt DESC;
   ```
- Results
- Explanation: 94 patients had office visits in 2025
![Query_C_Results](images/pic3.png)

### Query D: Five Oldest Patients
- Description: Calculate patient ages and show the 5 oldest patients
- Query
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
- Results
- Explanation: The five oldest patients are all 85 years old, born in 1940
![Query_D_Results](images/pic4.png)


### Query E: Data Quality Check
- Description: Check for any records with blank giagnosis or procedure codes
- Query:
```bash
SELECT *
FROM patients
WHERE primary_icd10 = '' OR last_cpt = '';
   ```
- Results
- Explanation: No data quality issues were found, all patient records have complete diagnosis and procedure codes