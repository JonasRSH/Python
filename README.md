# README for project.py

#### Video Demo:  <URL HERE>

## Description

### What does 'project.py' do?

The Python script 'project.py' is designed to help users track their work hours on a daily basis. It prompts the user to input specific details about their workday, including the date, start time, break duration, return time, and end time. Once the user has entered this information, the program calculates the total hours worked and allows the user to save this data in a structured format.

The data is saved in a CSV file, with a separate file created for each month. This organization makes it easy for users to keep track of their work hours over time. After entering the data, the user is given the opportunity to review their input for accuracy. If everything looks correct, they can save the information as 'worktime.csv'. The saved file includes the date, start time, return time, end time and total hours worked for that day.

Additionally, the program offers the functionality to generate a PDF report from the CSV file. This report includes all the data for the month, along with a summary of the total hours worked and the salary earned, which is saved as 'salary.pdf'.

### Python Libraries Used

The following Python libraries are utilized in this project:

- `datetime`: For handling date and time operations.
- `fpdf`: For generating PDF files from the CSV data.
- `dateutil.parser`: For parsing user input into valid date and time formats.
- `csv`: For reading from and writing to CSV files.
- `os`: For interacting with the operating system, such as file management.
- 'sys': For error handling

### Class 'Workday'

The 'Workday' class encapsulates the concept of a single workday. It stores the date of the workday, start time, break duration, return time, and end time. The class also includes methods to calculate the total hours worked. This structure allows for easy manipulation and retrieval of workday data.

### User Input

User input is expected to be in a valid date and time format. To enhance user experience, the program employs `dateutil.parser` to parse the input, making it more user-friendly. If the parser fails to recognize the input as a valid date or time, an error message is displayed, and the user is prompted to re-enter the information.

### Error Handling

The program includes robust error handling to ensure data integrity. If the user inputs a date that is in the future, the program will exit, prompting the user to start over. Additionally, if the date or time format is incorrect, a `ValueError` is raised. The user is allowed three attempts to enter valid data before the program terminates.

### How to Use

To use 'project.py', follow these steps:

1. Choose an action from the menu:
   - Enter new data: 'n'
   - Save the entered data in a CSV file: 's'
   - Print/save the CSV as a PDF file: 'p'
   - Open the PDF file with the default PDF viewer: 'o'
   - Quit the program: 'q'

2. Enter the date, work start time, break duration, return time, and end time in a valid format for date and time.

3. After completing the input, you will be presented with the following options again:
   - Save data as a CSV file: 's'
   - Print journal as a PDF file: 'p'
   - Enter new input: 'n'
   - Quit: 'q'

4. You can verify your input on the screen. If everything is correct, you can save it ('s') or choose to enter new data ('n'). You can also print a journal as a PDF ('p') and finally quit the program after all tasks are completed ('q').

This structured approach ensures that users can efficiently track their work hours and generate reports, making 'project.py' a valuable tool for time management.
