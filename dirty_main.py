from application.salary import *
from application.db.people import *
from datetime import datetime as dt, date

if __name__ == '__main__':
    print(dt.utcnow(), end='\t')
    calculate_salary()
    print(date.today(), end='\t')
    get_employees()