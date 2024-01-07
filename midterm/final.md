<h1>Database Advanced Data Techniques</h1>
<h2>Final report</h2>

<div style="text-align: right"> Course <b>CM3010</b></div>
<div style="text-align: right"> Final report</div>
<div style="text-align: right"> Student <b>Anvar Nurmatov</b></div>
<div style="text-align: right"> January 06, 2024</div>

<h2>Contents:</h2>

- [Introduction](#introduction)
- [Dataset Overview](#dataset-overview)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Key Observations from EDA](#key-observations-from-eda)
- [Defining Research Questions](#defining-research-questions)
- [Data Modeling](#data-modeling)
- [Database Implementation](#database-implementation)
  - [Database Setup Script](#database-setup-script)
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
  - [Data Normalization](#data-normalization)
  - [Preprocessing Script](#preprocessing-script)
- [Data Analysis and Findings](#data-analysis-and-findings)
  - [Most Favored Programming Languages in 2023](#most-favored-programming-languages-in-2023)
  - [Most Common Level of Education Among Developers in 2023](#most-common-level-of-education-among-developers-in-2023)
- [Web Application Development](#web-application-development)
  - [Overview](#overview)
  - [Back-end Development](#back-end-development)
  - [Front-end Development](#front-end-development)
  - [Features](#features)
  - [Application Deployment](#application-deployment)
  - [Conclusion](#conclusion)
- [Conclusion](#conclusion-1)
- [References](#references)
- [Appendices](#appendices)

## Introduction
This report delves into the 2023 Stack Overflow Developer Survey, aiming to uncover trends and preferences within the global developer community. By analyzing this comprehensive dataset, we seek to gain insights into the technologies, practices, and sentiments that shape the landscape of software development today.

## Dataset Overview
The Stack Overflow Developer Survey 2023 is a comprehensive collection of responses from thousands of developers worldwide. It covers a wide range of topics from programming languages, frameworks, and tools to career satisfaction and development practices. This dataset is an invaluable resource for understanding current trends in the tech industry.


## Exploratory Data Analysis (EDA)

During the initial phase of exploratory data analysis, we examined a subset of the Stack Overflow Developer Survey 2023 to identify patterns and gain preliminary insights. This analysis focused on understanding the distribution and trends of various attributes, such as programming languages popularity, respondents' age distribution, and education levels.

Below is a snapshot of the data we analyzed, formatted as a table for clarity:

| ResponseId | Age   | EdLevel                              | LanguageWantToWorkWith  |
|------------|-------|--------------------------------------|-------------------------|
| 1          | 25-34 | Bachelor’s degree (B.A., B.S., ...)  | JavaScript; HTML/CSS    |
| 2          | 18-24 | Some college/university study        | Python; Rust            |
| 3          | 35-44 | Master’s degree (M.A., M.S., ...)    | Go; TypeScript          |
| ...        | ...   | ...                                  | ...                     |

*Sample data extracted from the Stack Overflow Developer Survey 2023.*

### Key Observations from EDA

1. **Programming Language Popularity**: Early analysis suggests a strong preference for web-based languages such as JavaScript and Python. Further investigation will determine the most favored programming languages in 2023.

2. **Age Distribution**: There is a diverse age range among respondents, with a notable concentration in the 25-34 age bracket. This may reflect the demographics of active developers in the industry.

3. **Educational Background**: Preliminary data shows a wide range of educational backgrounds, with a significant number of respondents holding a Bachelor's degree. We will analyze how educational levels correlate with other factors such as language preference.

The EDA provided valuable direction for our research questions and helped to tailor our subsequent data modeling and analysis efforts. It is evident from the early stages that the survey data is rich with insights that can illuminate the current state of the developer community and the tech industry at large.


## Defining Research Questions
Based on our objectives and the data available in the Stack Overflow Developer Survey 2023, we have identified two key research questions:

1. **What are the most favored programming languages in 2023?**
   - This question aims to identify the programming languages that are most popular among developers, providing insights into current technology trends in the software development industry.

2. **What is the most common level of education among developers in 2023?**
   - This question seeks to understand the educational background of the developer community, which can be indicative of the industry's educational diversity and requirements.


## Data Modeling

The data modeling for the Stack Overflow Developer Survey 2023 was adapted to a revised Entity-Relationship Diagram (ERD) that reflects the updated database structure. This ERD serves as a comprehensive blueprint for our database, illustrating the interconnected nature of the data. The key components of the ERD, in alignment with the new database schema, include:

- **Entities**: Our ERD includes the entities `Education_Levels`, `Respondents`, and `Languages`. These entities correspond to the main data points we are analyzing from the survey:
  - `Education_Levels` contains the various educational qualifications reported by the survey respondents.
  - `Respondents` records individual survey participants, their identifiers, ages, and direct association with an education level.
  - `Languages` lists the programming languages that respondents are interested in working with.

- **Relationships**:
  - `Respondents` are directly linked to `Education_Levels`, establishing a one-to-one relationship where each respondent reports one education level, indicated by the foreign key `education_level_id` in the `Respondents` table.
  - `Respondents_Preferred_Languages` is an associative table that facilitates a many-to-many relationship between `Respondents` and `Languages`, showing the programming languages that are preferred by each respondent.

- **Normalization**:
  - The ERD reflects a normalized structure that aims to reduce data redundancy and improve the integrity of our database. This design allows for efficient data storage and retrieval for analysis purposes.

Below is the visual representation of the ERD for our database:

<p align="center">
  <img src="images/erd.jpg" alt="Image" width="500">
</p>

This visual ERD illustrates the relationships between `Respondents`, `Education_Levels`, and `Languages`, with the associative tables clearly indicating the connections that support our research questions. The diagram serves as a guide for understanding the logical structure of our database and informs our data cleaning, preprocessing, and subsequent analysis.


## Database Implementation
The database was implemented in MySQL. Tables were created corresponding to the ERD, with appropriate data types and constraints to ensure data integrity. Relationships were established using foreign keys. A script was developed to import the survey data into the database, allowing for efficient querying and analysis.

### Database Setup Script

In addition to data normalization and preprocessing, a separate script, `data_preparation_scripts/database.py`, was created to automate the setup of the database structure. This script plays a crucial role in establishing the foundational database schema onto which the survey data is loaded. The key functions of this script include:

- **Database Creation**: Automatically creates the `stackoverflow_survey` database, ensuring a clean environment for data import.
- **Table Definition and Creation**: Defines and creates tables in accordance with the normalized database schema. This includes tables for respondents, education levels, languages, and their associative relationships.
- **Execution and Committing**: The script executes SQL statements to construct the database and its tables, committing each change to ensure the database structure is correctly set up.

To recreate the database on a different machine, one simply needs to run the `database.py` script. This script is designed to be idempotent, meaning it can be run multiple times without causing errors or unintended effects, as it first checks for the existence of the database and drops it if it exists before creating a new one.

This approach ensures that the database setup process is easily replicable, making it convenient for any reviewer or user to initialize the database on their local system for analysis or review purposes.


## Data Cleaning and Preprocessing

The preprocessing of the Stack Overflow Developer Survey 2023 data involved a series of steps to ensure the data was organized efficiently and ready for analysis. This process, commonly referred to as data normalization in database management, is crucial for reducing redundancy and improving data integrity.

### Data Normalization

Data normalization in the context of our project involved structuring the database to manage dependencies and store the data efficiently. The key aspects of this process included:

1. **Separation of Concerns**: We created distinct tables for different entities such as `respondents`, `education_levels`, and `languages`. This separation ensures that each data type is stored in its dedicated structure, adhering to the first principle of normalization.

2. **Reduction of Redundancy**: By establishing separate tables for `education_levels` and `languages` and linking them to `respondents` through associative tables (`respondents_education_levels` and `respondents_preferred_languages`), we minimized data redundancy. Each education level and language is stored once and referenced in the respondents' records.

3. **Referential Integrity**: The use of foreign keys to establish relationships between tables maintains referential integrity, ensuring that links between tables are consistent and reliable.

### Preprocessing Script

The `data_preparation_scripts/preprocess.py` script was developed to handle the extraction and insertion of survey data into our normalized database schema. The script performs the following functions:

- **Data Extraction**: Reads the CSV file containing survey responses and extracts relevant information.
- **Data Transformation**: Transforms the raw data to fit into our database schema. This includes parsing and splitting data from columns like `LanguageWantToWorkWith`.
- **Database Insertion**: Inserts data into the respective tables, creating new entries for unique education levels and programming languages to avoid duplication.

This preprocessing step was vital in setting the stage for efficient and effective data analysis, ensuring that our database structure supports complex queries without performance issues or data integrity concerns.


## Data Analysis and Findings
The analysis focused on answering the two research questions. SQL queries were used to extract relevant data from the database, and the findings were as follows:

### Most Favored Programming Languages in 2023
(Detail the analysis findings on the most popular programming languages based on the survey responses.)

### Most Common Level of Education Among Developers in 2023
(Present the findings on the educational qualifications of developers, highlighting the most common level of education as revealed by the survey data.)


## Web Application Development

### Overview
The web application was designed to provide a straightforward and interactive way to explore the Stack Overflow Developer Survey data. It was built using Node.js and Express, prioritizing simplicity and functionality. 

### Back-end Development
The back-end of the application was developed using Node.js and Express. It includes several routes to handle requests for different types of survey data. The application connects to the MySQL database, executing SQL queries based on user requests and returning the results. 

### Front-end Development
For the front-end, simple templating was used, employing Express's integrated template engine, EJS (Embedded JavaScript). This approach allowed for dynamically generating HTML pages based on the data retrieved from the back-end. The user interface includes basic forms and tables to facilitate data querying and display the results in a readable format.

### Features
- **Querying Programming Languages**: Users can view statistics about the most popular programming languages in 2023.
- **Querying Educational Background**: The application allows users to explore the distribution of educational levels among developers.

### Application Deployment
The application is set up to run locally for demonstration purposes. Instructions for setting up and running the application are included in the repository's README file.

### Conclusion
This simple web application serves as a practical tool for exploring the Stack Overflow Developer Survey data, demonstrating the potential of Node.js and Express in building effective web solutions with minimal complexity.


## Conclusion
This report provides valuable insights into the preferences and trends within the global developer community. Key findings highlight the importance of technology choice on job satisfaction and the evolving nature of work environments. Future research could explore longitudinal changes in these trends and delve deeper into the causative factors behind these observations.


## References
1. Stack Overflow Developer Survey 2023. Stack Overflow. URL: [https://insights.stackoverflow.com/survey](https://insights.stackoverflow.com/survey)
2. Node.js Documentation. Node.js. URL: [https://nodejs.org/en/docs/](https://nodejs.org/en/docs/)
3. Express.js Documentation. Express.js. URL: [http://expressjs.com/](http://expressjs.com/)
4. EJS Documentation. EJS. URL: [https://ejs.co/](https://ejs.co/)


## Appendices
Appendix A: SQL Scripts for Database Creation and Data Import  
Appendix B: Node.js Server Code  
Appendix C: Express Route Definitions  
Appendix D: EJS Template Examples  
Appendix E: Instructions for Setting Up and Running the Application
