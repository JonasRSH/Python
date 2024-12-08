import pytest
import project as p


def test_calculate_salary():
    workday = p.Workday('01.03.2024', '08:00', '12:00', '14:00', '21:00')
    assert p.calculate_salary(workday) == '110.00'

def test_total_salary():
    p.read_csv('test_worktime.csv')
    assert p.total_salary() == 'Total salary: $ 1009.33'

def test_calculate_work_hours():
    workday = p.Workday('01.03.2024', '08:00', '12:00', '14:00', '21:00')
    assert p.Workday.calculate_work_hours(workday) == 11.0
