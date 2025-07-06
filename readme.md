✅ How to Start This Project
Install Python
Download and install Python from https://python.org

1. Install Required Packages via pip
    Open terminal (CMD or PowerShell) and run:
        pip install flask
        pip install mysql-connector-python

2. Set Up MySQL Database (WAMP/XAMPP)
    a. Start WAMP or XAMPP server
    b. Open phpMyAdmin or MySQL CLI
    c. Run the following SQL to create the database:
        CREATE DATABASE test_python;

3. Download or Clone the Project Folder
    Place the folder (named testProject) anywhere like your Desktop.

4. Check Your Folder Structure
    testProject/
    ├── app.py
    ├── routes.py
    ├── controller.py
    ├── db.py
    └── templates/
        └── index.html

5. Open Terminal in Project Folder and Navigate to your project directory:
    cd Desktop/testProject
    Start the project by running:python app.py (in this time "items" table will be created automatically)


6. Open in Browser
    Go to http://127.0.0.1:5000 in your browser

7. Make Sure:
    Database name is: test_python
