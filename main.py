# ADPY-49
# 1.«Import. Модуль. Пакет»
# Task 111. Import.Module. Package
# https://github.com/netology-code/py-homeworks-advanced/tree/master/1.Import.Module.Package

from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime as dt, date

if __name__ == '__main__':
    print(dt.utcnow(), end='\t')
    calculate_salary()
    print(date.today(), end='\t')
    get_employees()
