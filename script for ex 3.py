import json
import pyodbc
from datetime import datetime

def connect_to_database():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-BNVHVDN;'
        'DATABASE=Exercise3;'
        'UID=sa;'
        'PWD=tuanle3456;'
        'Trusted_Connection=no;'
    )

def ensure_table_exists(cursor):
    cursor.execute("""
    IF OBJECT_ID('dbo.employees', 'U') IS NULL
      CREATE TABLE dbo.employees (
        id INT PRIMARY KEY,
        name NVARCHAR(100),
        department NVARCHAR(100),
        salary INT,
        join_date DATE
      );
    """)
    cursor.connection.commit()

def load_employee_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def insert_employee(cursor, employee):
    jd = datetime.strptime(employee['join_date'], '%Y-%m-%d').date()
    try:
        cursor.execute(
            "INSERT INTO dbo.employees (id,name,department,salary,join_date) VALUES (?,?,?,?,?)",
            employee['id'], employee['name'], employee['department'], employee['salary'], jd
        )
    except pyodbc.IntegrityError:
        pass

def main():
    conn = connect_to_database()
    cursor = conn.cursor()
    
    ensure_table_exists(cursor)
    
    employees = load_employee_data('employees.json')
    for emp in employees:
        insert_employee(cursor, emp)
    
    conn.commit()
    conn.close()
    print("Data import completed successfully")

if __name__ == "__main__":
    main()
