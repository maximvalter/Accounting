def calculate_salary(hours, pph):
    """
    Функция позволяет посчитать зарплату человека
    Параметры:
    hours: Количество отработнных часов
    pph: Оплата за 1 час работы
    """
    salary = hours * pph
    return f"Ваша зарплата: {salary}"