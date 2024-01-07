const express = require('express');
const mysql = require('mysql');

// Create an Express application
const app = express();

app.set('view engine', 'ejs');

// Database connection configuration
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'stackoverflow_survey'
});

// Connect to the database
db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log('Connected to database');
});

// Index Route
app.get('/', (req, res) => {
    res.render('index');
});

// Define a route to get favored programming languages
app.get('/favored-languages', (req, res) => {
  let sqlQuery = 'SELECT l.name `language`, count(*) `count` FROM respondents_preferred_languages rpl INNER JOIN languages l ON l.id = rpl.language_id GROUP BY l.name ORDER BY `count` DESC';
  db.query(sqlQuery, (err, results) => {
      if (err) throw err;
      res.render('favoredLanguages', { languages: results });
  });
});

// Define a route to get common education levels
app.get('/common-education', (req, res) => {
  let sqlQuery = 'SELECT l.name `Education Level`, COUNT(*) `count` FROM respondents r INNER JOIN education_levels l ON l.id = r.education_level_id GROUP BY l.name ORDER BY `count` DESC';
  db.query(sqlQuery, (err, results) => {
      if (err) throw err;
      res.render('commonEducation', { educationLevels: results });
  });
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
