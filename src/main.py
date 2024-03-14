# COMP 3005 Assignment 3 Question 1
# Jonah Habtom

import psycopg

#Retrieves and displays all records from the students table
def getAllStudents():
    with conn.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM students;")
            students = cursor.fetchall()
            
            #Prints each of the student records in the database, separating their fields with a commma
            for row in students:
                print("Student Id:", str(row[0]) + ", First Name:", row[1] + ", Last Name:", row[2] + ", Email:", row[3] + ", Enrollment Date:", row[4])
        except psycopg.Error as e:
            print(f"Error when getting students: {e}")
        
    
#Inserts a new student record into the students table
def addStudent(firstName, lastName, email, enrollmentDate):
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (firstName, lastName, email, enrollmentDate))
            print("Student added")
        except psycopg.Error as e:
            print(f"Error when adding student: {e}")
    

# Updates the email address for a student with the given id
def updateStudentEmail(id, updatedEmail):
    with conn.cursor() as cursor:
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;", (updatedEmail, id))
        #If 0 rows were affected, that means the id did not exist and no email was updated. Else, the email was updated for that id
        if cursor.rowcount == 0:
            print("Student id does not exist")
        else:
            print("Student email was updated")

# Deletes the record of the student with the specified id
def deleteStudent(id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM students WHERE student_id = %s;", (id,))
        #If 0 rows were affected, that means the id did not exist and no student was deleted. Else, the student was deleted
        if cursor.rowcount == 0:
            print("Student id does not exist")
        else:
            print("Student was deleted")
    
if __name__ == "__main__":
    #Connect to the database
    try:
        #Set the user and password parameters corresponding to your setup
        conn = psycopg.connect(dbname="School", user="postgres", password="postgres", host="localhost", port=5432)
        conn.autocommit = True
    except psycopg.OperationalError as e:
        print(f"Error: {e}")
        exit(1)
    
    #Loop to continue to display the menu until a user exits
    while True:
        #Prints the menu and asks for user input
        print("What would you like to do?")
        print("1. Get all the students")
        print("2. Add a student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Enter your selection: ")

        if choice == "1":
            #Call the function to print out the students in the database
            getAllStudents()
        elif choice == "2":
            #Get the input from the user for the student's first and last name, email and enrollment date
            firstName = input("Enter student's first name: ")
            lastName = input("Enter student's last name: ")
            email = input("Enter student's email: ")
            enrollmentDate = input("Enter enrollment date (Use the form YYYY-MM-DD): ")
            #Call the function to add the student to the database
            addStudent(firstName, lastName, email, enrollmentDate)
        elif choice == "3":
            #Get the input from the user for the student's id and email to update
            id = int(input("Enter student's Id: "))
            updatedEmail = input("Enter the updated email: ")
            #Call the function to update the email in the database for the given student id
            updateStudentEmail(id, updatedEmail)
        elif choice == "4":
            #Get the input from the user for the student's id
            id = int(input("Enter student's Id: "))
            #Call the function to delete the student with the specific student id
            deleteStudent(id)
        elif choice == "5":
            #If user selects 5, we exit the program
            break
        else:
            print("Please select one of the existing options")

    #Close connection to database
    conn.close()