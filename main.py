from application.salary import calculate_salary
from application.people import get_employees
from datetime import date


def current_date():
    today = date.today()
    print(today)


if __name__ == '__main__':
    current_date()
    calculate_salary()
    get_employees()
