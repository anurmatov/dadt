<h1>Database Advanced Data Techniques</h1>
<h2>Final report</h2>

<div style="text-align: right"> Course <b>CM3010</b></div>
<div style="text-align: right"> Final report</div>
<div style="text-align: right"> Student <b>Anvar Nurmatov</b></div>
<div style="text-align: right"> January 06, 2024</div>

<h2>Contents:</h2>

- [Introduction](#introduction)
- [Dataset Overview](#dataset-overview)
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Defining Research Questions](#defining-research-questions)
- [Data Modeling](#data-modeling)
- [Database Implementation](#database-implementation)
- [Data Analysis and Findings](#data-analysis-and-findings)
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

## Data Cleaning and Preprocessing
The dataset underwent several preprocessing steps to ensure the integrity and relevance of the analysis. Key actions included handling missing data by filtering out incomplete responses, transforming categorical variables for ease of analysis, and selecting relevant columns that align with our research focus.

## Exploratory Data Analysis (EDA)
Initial EDA revealed intriguing patterns in developer preferences and behaviors. Statistical analysis was conducted on various aspects such as preferred programming languages, job satisfaction levels, and remote work trends. This exploratory phase helped in identifying key areas for detailed analysis.

## Defining Research Questions
From the EDA, several critical questions emerged: What are the most favored programming languages in 2023? How does remote work affect job satisfaction among developers? These questions are pivotal in understanding the evolving dynamics of the software development industry.

## Data Modeling
The data modeling process involved constructing an Entity-Relationship Diagram (ERD) to effectively represent the structure of the Stack Overflow survey data. Key entities identified include Respondent, Technology, and Employment details, with relationships designed to mirror the complexity of the dataset. Attention was given to normalization to ensure efficient and logical data organization.

## Database Implementation
The database was implemented in MySQL. Tables were created corresponding to the ERD, with appropriate data types and constraints to ensure data integrity. Relationships were established using foreign keys. A script was developed to import the survey data into the database, allowing for efficient querying and analysis.

## Data Analysis and Findings
The analysis yielded several key insights. For instance, a significant correlation was found between programming language preference and job satisfaction. Another interesting finding was the emerging trend of remote work and its varied impact on developers' work-life balance and productivity.

## Web Application Development

### Overview
The web application was designed to provide a straightforward and interactive way to explore the Stack Overflow Developer Survey data. It was built using Node.js and Express, prioritizing simplicity and functionality. 

### Back-end Development
The back-end of the application was developed using Node.js and Express. It includes several routes to handle requests for different types of survey data. The application connects to the MySQL database, executing SQL queries based on user requests and returning the results. 

### Front-end Development
For the front-end, simple templating was used, employing Express's integrated template engine, EJS (Embedded JavaScript). This approach allowed for dynamically generating HTML pages based on the data retrieved from the back-end. The user interface includes basic forms and tables to facilitate data querying and display the results in a readable format.

### Features
- **Data Querying**: Users can query the database through simple forms, selecting specific criteria like technology preferences, employment status, or demographic information.
- **Result Display**: The queried data is displayed in a tabular format, allowing users to easily interpret the survey results.
- **Navigation**: Simple navigation is provided to switch between different data queries and view results.

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
