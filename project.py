# Libraries
import csv, os, sys
from datetime import datetime
from fpdf import FPDF
from dateutil import parser


# Class that represents a single workday, including the date, start time, pause duration, return time, and end time.
# It also calculates the value 'worked_hours', which represents the total hours worked on that day based on user input.
class Workday:
    def __init__(self, work_date=None, work_start=None, work_pause=None, work_return=None, work_end=None, worked_hours=None):
        self.work_date = datetime.strptime(work_date, "%d.%m.%Y") if work_date else None
        self.work_start = datetime.strptime(work_start, "%H:%M") if work_start else None
        self.work_pause = datetime.strptime(work_pause, "%H:%M") if work_pause else None
        self.work_return = datetime.strptime(work_return, "%H:%M") if work_return else None
        self.work_end = datetime.strptime(work_end, "%H:%M") if work_end else None
        self.worked_hours = worked_hours if worked_hours else None

# Prompts the user for the working date, start time, pause duration, return time, and end time, 
# and checks if the date is not in the future.
    def prompt_user(self):
        self.work_date = self.validate_input('Date: ')
        if self.work_date > datetime.today():
            sys.exit('Date cannot lay in the future')
        self.work_start = self.validate_input('Start: ')
        self.work_pause = self.validate_input('Pause: ')
        self.work_return = self.validate_input('Return: ')
        self.work_end = self.validate_input('End: ')
        return self.work_date, self.work_start, self.work_pause, self.work_return, self.work_end

# Validates the user's input to ensure it is in the correct date and time format.
    def validate_input(self, prompt, previous_time=None):
        user_try = 0
        while user_try < 3:
            try:
                input_time = parser.parse(input(prompt))
                if previous_time and input_time < previous_time:
                    raise ValueError('Time must be after the previous time')
                return input_time
            except(ValueError, TypeError):
                user_try += 1
                print('Invalid input. Please try again.')
        else:
            raise ValueError('Input must be a valid date and time format')

# Calculates the hours worked in a day based on user input.
    def calculate_work_hours(self):
        total_hours = (self.work_pause - self.work_start) + (self.work_end - self.work_return)
        worked_hours = total_hours.total_seconds()/3600
        return(worked_hours)

# Formats the output of the date and time inputs provided by the user.
    def __str__(self):
        return(f'Date: {datetime.strftime(self.work_date, "%d.%m.%Y")}  Start: {datetime.strftime(self.work_start, "%H:%M")}h  Pause: {datetime.strftime(self.work_pause, "%H:%M")}h  Return: {datetime.strftime(self.work_return, "%H:%M")}h  End: {datetime.strftime(self.work_end, "%H:%M")}h  Hours worked: {self.calculate_work_hours(): .2f}hours')

# Formats the output for saving to a CSV file.
    def __repr__(self):
        return str({'Date': datetime.strftime(self.work_date, "%d.%m.%Y"), 'Start': datetime.strftime(self.work_start, "%H:%M"), 'Pause': datetime.strftime(self.work_pause, "%H:%M"), 'Return': datetime.strftime(self.work_return, "%H:%M"), 'End': datetime.strftime(self.work_end, "%H:%M"), 'Hours worked': str(self.calculate_work_hours())})

# Creates a menu that displays the user's options within the application.
def menu(workday):
    new_action=None
    while True:
        new_action = input("\n--------------------------------------------- MENU ---------------------------------------------\nNew input: 'n'  |  Save data in CSV file: 's'  |  Create PDF journal: 'p'  |  Open PDF journal: 'o'  |  Quit: 'q' \n\nChoose action: ")
        if new_action == 's':
            try:
                save_csv(workday)
                print(f'Data saved to "worktime.csv"')
            except TypeError:
                print('Not data to save entered')
        elif new_action == 'p':
            try:
                create_pdf()
                print(f'PDF created as "salary.pdf"')
            except TypeError:
                print('Enter some data first, please')
                return
        elif new_action == 'n':
            print('Enter the date and time worked, please')
            workday.prompt_user()
            print(workday)
            print(f'Your salary: $ {calculate_salary(workday)}')
        elif new_action == 'o':
            open_pdf()
        elif new_action == 'q':
            sys.exit('Thanks for using WORKTIME a Python CS50 Final Student Project by Jonas Huggler Bern Switzerland')
        else:
            print('Invalid input')

# Saves the entered data from the class to a CSV file.
def save_csv(workday):
    file_path = 'project/worktime.csv'
    write_header = not os.path.exists(file_path) or os.path.getsize(file_path) == 0
    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Start', 'Pause', 'Return', 'End', 'Hours worked', 'Salary']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
        if write_header:
            csv_writer.writeheader()
        csv_writer.writerow(({
    'Date': datetime.strftime(workday.work_date, "%d.%m.%Y"),
    'Start': datetime.strftime(workday.work_start, "%H:%M"),
    'Pause': datetime.strftime(workday.work_pause, "%H:%M"),
    'Return': datetime.strftime(workday.work_return, "%H:%M"),
    'End': datetime.strftime(workday.work_end, "%H:%M"),
    'Hours worked': f'{workday.calculate_work_hours(): .2f}',
    'Salary': calculate_salary(workday)
}))

# Reads the data from the CSV file.
def read_csv(file_path='project/worktime.csv'):
    workdays_lst = []
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, dialect='excel')
        for row in csv_reader:
            workday = Workday(
                work_date=row['Date'],
                work_start=row['Start'],
                work_pause=row['Pause'],
                work_return=row['Return'],
                work_end=row['End'],
            )
            workdays_lst.append(workday)
    return workdays_lst

# Calculates the salary based on the saved data and the calculated hours worked per day.
def calculate_salary(workday):
    salary_per_hour = 12.00
    salary = salary_per_hour * workday.calculate_work_hours()
    return f'{salary:.2f}'

# Calculates the total salary based on all workdays entered by the user and saved in the CSV file.
def total_salary():
    workdays = read_csv()
    total_hours = sum(workday.calculate_work_hours() for workday in workdays)
    salary_per_hour = 12.00
    total_salary = salary_per_hour * total_hours
    return f'Total salary: $ {total_salary:.2f}'

# Generates a PDF report summarizing the workdays and total salary based on the data entered by the user.
def create_pdf():
    # Reads data from the csv file
    try:
        with open('project/worktime.csv', 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, dialect='excel')
            pdf = FPDF(orientation='P', format='A4')
            pdf.add_page()
            pdf.set_font('helvetica', 'B', 20)
            pdf.cell(180, 10, 'Work and salary report', align='C')
            pdf.ln(20)
            pdf.set_font('helvetica', '', 12)
            for row in csv_reader:
                pdf.cell(180, 5, '   |   '.join(row), 1, 1,)
            pdf.set_font('helvetica', 'B', 12)
            pdf.cell(160, 20, total_salary(), align='C')
            pdf.output('salary.pdf', 'F')
    except FileNotFoundError:
        print('No data saved yet')

# Opens the PDF file if it exists.
def open_pdf():
    pdf_file = 'project/salary.pdf'
    if os.path.exists(pdf_file):
        print(f'File exists: {pdf_file}')
        os.system(f'open {pdf_file}')
    else:
        print('File not found')


# Main function that displays a menu to guide the user in a more user-friendly manner.
def main():
    print('\nWORKTIME')
    workday = Workday()
    menu(workday)


if __name__ == "__main__":
    main()
