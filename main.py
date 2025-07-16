from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
from application.rainbow import rainbow_text
from rich.console import Console

employees = ['Олег', 'Тимур', 'Елена', 'Кирилл']
today = datetime.now().date()

if __name__ == '__main__':
    console = Console(force_terminal=True, color_system="auto")
    print(f"Данные функции были выполнены: {today}")
    salary_text = calculate_salary(200, 350)
    employees_text = get_employees(employees)
    rainbow1 = rainbow_text(salary_text)
    rainbow2 = rainbow_text(employees_text)
    console.print(rainbow1)
    console.print(rainbow2)
