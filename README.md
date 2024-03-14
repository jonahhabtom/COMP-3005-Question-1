# COMP 3005 Assignment 3 Question 1

This application is written in Python and connects to a database to perform CRUD (Create, Read, Update, Delete) operations. It allows the user to retrieve all students in a database, add a student to a database, update student's email in a database, and a delete a student in the database.

## Video

Here is the link to the video demonstration for this application: https://youtu.be/pGpeO_94gxQ

## Running the Application

### Prerequisites
- Python (Can be downloaded from https://www.python.org/downloads/)
- PostgreSQL and pgAdmin (Can be installed from https://www.postgresql.org/download/)
- psycopg (Can be installed using pip install psycopg)

### Setting Up the Database
- Launch pgAdmin 4
- Under the Object Explorer panel on the left, expand Servers
- Right click on Databases and choose Create -> Database
- In the pop-up window, enter School as the Database name and click the Save button in the buttom right
- You should now see the School database under Databases in the Object Explorer. Right click on the School database and select Query Tool
- Click on the Open File icon in the toolbar and open the ddl.sql file that is under the SQL folder of this repository
- Click on the Run button to add the students table
- Click on the Open File icon again and open the dml.sql file that is under the SQL folder of this repository
- Click on the Run button to insert the records to the student table

### Connecting the Application to the Database
- The database connection occurs on line 54 of the main.py file in the src folder
- The current implementation has the fields filled out as: dbname="School", user="postgres", password="postgres", host="localhost", port=5432
- Adjust the user, password, host, and port parameters to fit the PostgreSQL setup on your system
- If you named the database School, there is no need to update the dbname parameter

### Running the Application
- In the command line, navigate to the src folder of this repository
- Run the command "py main.py"
- Interact with command line application using the menu options