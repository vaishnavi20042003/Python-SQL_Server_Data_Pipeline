# Python-SQL Server Data Pipeline 🚀

This project demonstrates how to connect a Python application to a SQL Server database using the `pyodbc` library. It covers database connection, data insertion, querying, and basic error handling — simulating a real-world data engineering task.

---

## 📁 Project Structure

.
├── doc-script.py         → Python script to connect & fetch data  
├── 1.sql                 → SQL script to populate `users` table  
├── 1.pdf                 → Initial project report  
├── Final_Report.docx     → Editable report file  
└── README.md             → This documentation

---

## 🔧 Requirements

- Python 3.x  
- SQL Server  
- Python package: `pyodbc`  
  → Install via `pip install pyodbc`

---

## ⚙️ What This Project Does

- Connects to a remote SQL Server database  
- Runs a query: `SELECT TOP 5 * FROM users`  
- Prints fetched records  
- Handles exceptions gracefully  
- Uses realistic user data (100+ records)

---

## 📜 Key Python Snippet

python
server = '192.168.0.20'
database = 'tws'
username = 'Vaish22'
password = 'V@aish22'

conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

## 🧰 Tools Used

| Tool       | Role                   |
|------------|------------------------|
| Python     | Scripting              |
| pyodbc     | SQL Server connectivity|
| SQL Server | Database backend       |
| GitHub     | Version control        |

---

## 📝 Notes

- `users` table has nullable IDs to simulate data issues  
- The `year` field is stored as a date string  
- ODBC Driver used: **17 for SQL Server**

---

## ✅ Conclusion

This project provides a solid foundation for:

- Data connectivity in ETL workflows  
- Handling real-world structured data  
- Practicing SQL-Python integration

---

## 👤 Author

**Vaishnavi Bandil**  
_Data Engineering Intern_  
GitHub: vaishnavi20042003

