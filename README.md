# python-2
second try
Student Progress Tracker

GitHub Repository URL:
The source code for this project is available on GitHub: https://github.com/saarimahmedarif-2005/python-2

Identification:
- Name: Saarim Ahmed Arif
- P-number: P506871
- Course code: IY499

Declaration of Own Work:
I confirm that this assignment is my own work.
Where I have referred to academic sources, I have provided proper in-text citations and included the sources in the final reference list.

Introduction:
This project implements a student progress tracking web application using the Flask library.
The main functionality of the app includes:
- Adding and deleting students from the system
- Recording, viewing and updating grades for each student
- Searching for students by name using partial matching
- Generating a full class report with bar charts and a pie chart showing pass and fail rates

Installation:
To run the app locally:
1. Make sure Python 3.x is installed.
2. Install required dependencies:
   pip install flask matplotlib
   or manually install any external libraries used:
   pip install flask
   pip install matplotlib

How to Run the App:
1. Open terminal/command prompt in the project folder.
2. Run the main script:
   python tester.py
3. Open your browser and go to:
   http://127.0.0.1:5000
4. Controls:
   - Use the navigation links to move between pages
   - Fill in the forms to add students and grades
   - Click the report page to see charts and class statistics

App Elements:
- Student Management: Add, view and delete students stored in a CSV file
- Grade Management: Add, view and update grades for each student with validation
- Search: Search for any student by typing part of their name
- Report Page: Displays class average, top student, failing students and three charts
- Data Storage: All student and grade data is saved to and loaded from CSV files

Libraries Used:
- Flask - for creating the web application and handling routes
- matplotlib - for generating bar and pie charts
- csv - for reading and writing student and grade data to files
- io - for handling image data in memory when generating charts
- base64 - for converting charts to a format that can be displayed in HTML

Project Structure:
python-2/
|-- templates/          # HTML pages for the web app
|-- static/             # CSS styling for all pages
|-- tester.py           # Main application file
|-- students.csv        # Stores student data
|-- grades.csv          # Stores grade data
|-- README.md           # Project documentation

Testing:
Include test scenarios covering:
- Valid cases: Expected input and normal behavior
- Invalid cases: Handling of incorrect or unexpected input
- Edge/boundary cases: Values at the limits of valid input

Examples:
- Adding a student with a valid ID and name saves correctly to the CSV file
- Entering a mark above 100 or below 0 shows an error and does not save
- Adding a duplicate student ID shows an error message
- Entering a mark with letters instead of numbers shows an error message
- Searching for a name that does not exist returns no results without crashing
- Entering a mark of exactly 0 or exactly 100 is accepted as valid

References:
- Pallets Projects (2024) Flask Documentation. Available at: https://flask.palletsprojects.com/en/stable/ (Accessed: 10 April 2026)
- Matplotlib Development Team (2024) Matplotlib Documentation. Available at: https://matplotlib.org/stable/index.html (Accessed: 10 April 2026)
- Python Software Foundation (2024) csv - CSV File Reading and Writing. Available at: https://docs.python.org/3/library/csv.html (Accessed: 10 April 2026)
- OpenAI (2026) Advice on base64 encoding for embedding charts in HTML [ChatGPT conversation]. ChatGPT. 10 April 2026.
- OpenAI (2026) Advice on converting matplotlib figures to PNG using BytesIO and FigureCanvas [ChatGPT conversation]. ChatGPT. 10 April 2026.
- OpenAI (2026) Advice on Flask route structure and use of render_template and redirect [ChatGPT conversation]. ChatGPT. 10 April 2026.
- OpenAI (2026) Advice on HTML and CSS for web page structure and styling [ChatGPT conversation]. ChatGPT. 10 April 2026.