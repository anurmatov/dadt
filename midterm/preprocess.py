import mysql.connector
import requests
import zipfile
import os
import csv
import pandas as pd

# Database connection details
HOST = 'localhost'
USER = 'root'
PASSWORD = 'password'
DB_NAME = 'stackoverflow_survey'

# Download URL
ZIP_URL = 'https://cdn.stackoverflow.co/files/jo7n4k8s/production/49915bfd46d0902c3564fd9a06b509d08a20488c.zip/stack-overflow-developer-survey-2023.zip'

# Establish database connection
conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
cursor = conn.cursor()

# Create database and tables
cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
cursor.execute(f"CREATE DATABASE {DB_NAME};")
conn.database = DB_NAME

create_tables_sql = """
CREATE TABLE education_levels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

CREATE TABLE respondents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    response_id VARCHAR(255),
    age VARCHAR(255),
    education_level_id INT NOT NULL,
    FOREIGN KEY (education_level_id) REFERENCES education_levels(id)
);

CREATE TABLE languages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

CREATE TABLE respondents_preferred_languages (
    respondent_id INT,
    language_id INT,
    FOREIGN KEY (respondent_id) REFERENCES respondents(id),
    FOREIGN KEY (language_id) REFERENCES languages(id)
);
"""
cursor.execute(create_tables_sql, multi=True)
cursor.close()
conn.close()

# Download and extract ZIP file
r = requests.get(ZIP_URL)
zip_file_path = './download/stack-overflow-developer-survey-2023.zip'

with open(zip_file_path, 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('./download/')

# Process CSV file
csv_file_path = './download/survey_results_public.csv'

def get_or_create_id(cursor, table, value):
    """ Get ID of a value in a table, or create it if it doesn't exist """
    cursor.execute(f"SELECT id FROM {table} WHERE name = %s", (value,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        cursor.execute(f"INSERT INTO {table} (name) VALUES (%s)", (value,))
        conn.commit()
        return cursor.lastrowid

conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DB_NAME)
cursor = conn.cursor()

with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['ResponseId'])>10000: break
        # Process education level
        education_level = row['EdLevel']
        if education_level is None: break
        education_level_id = get_or_create_id(cursor, 'education_levels', education_level)

        # Insert respondent data
        print(row['ResponseId'] + ' ' + row['Age'] + ' ' + str(education_level_id))
        cursor.execute("INSERT INTO respondents (response_id, age, education_level_id) VALUES (%s, %s, %s)", (row['ResponseId'], row['Age'], education_level_id))
        respondent_id = cursor.lastrowid

        # Process preferred languages
        languages = row['LanguageWantToWorkWith'].split(';')
        for language in languages:
            if language:
                language_id = get_or_create_id(cursor, 'languages', language)
                cursor.execute("INSERT INTO respondents_preferred_languages (respondent_id, language_id) VALUES (%s, %s)", (respondent_id, language_id))

        conn.commit()

# Close connection
cursor.close()
conn.close()
