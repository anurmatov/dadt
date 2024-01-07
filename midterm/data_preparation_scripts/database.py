import mysql.connector

# Database connection details
HOST = 'localhost'
USER = 'root'
PASSWORD = 'password'
DB_NAME = 'stackoverflow_survey'

# Establish database connection
conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
cursor = conn.cursor()

# Create database and tables
cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
cursor.execute(f"CREATE DATABASE {DB_NAME};")
conn.commit()
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

for statement in create_tables_sql.split(';'):
    if statement.strip():
        cursor.execute(statement)
        conn.commit()

cursor.close()
conn.close()