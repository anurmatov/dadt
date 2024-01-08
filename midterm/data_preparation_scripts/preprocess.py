# I wrote this code
import mysql.connector
import zipfile
import csv

# Database connection details
HOST = 'localhost'
USER = 'root'
PASSWORD = 'password'
DB_NAME = 'stackoverflow_survey'

# Extract ZIP file
zip_file_path = './download/stack-overflow-developer-survey-2023.zip'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('./download/')

# Process CSV file
csv_file_path = './download/survey_results_public.csv'

conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DB_NAME)
cursor = conn.cursor()

# Function to get or create ID for a value in a table
def get_or_create_id(cursor, table, value):
    cursor.execute(f"SELECT id FROM {table} WHERE name = %s", (value,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        cursor.execute(f"INSERT INTO {table} (name) VALUES (%s)", (value,))
        conn.commit()
        return cursor.lastrowid

# Read and process each row in the CSV file
with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # there should be a maximum of 10000 entries (per webinar)
        if int(row['ResponseId'])>10000: break
        # Skip rows with missing education level
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

# Close the database connection
cursor.close()
conn.close()
# end of code I wrote