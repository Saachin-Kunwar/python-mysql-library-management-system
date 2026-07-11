<p align="center">
  A professional <b>Library Management System</b> built using <b>Python</b> and <b>MySQL</b>, featuring complete Book Management, Member Management, Borrow & Return functionality, Search System, Dashboard Analytics, and MySQL Constraints through a clean CLI-based modular architecture.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Programming-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql">
  <img src="https://img.shields.io/badge/CLI-Application-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/CRUD-Operations-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

# 📚 Library Management System

A Command Line Interface (CLI) based **Library Management System** developed using **Python** and **MySQL**. The project enables librarians to manage books, members, borrowing and returning records while storing all information securely in a MySQL database.

This project was developed to strengthen understanding of:

- Python Programming
- MySQL Database
- CRUD Operations
- Database Constraints
- SQL JOIN Queries
- Relational Database Design
- Real-World Backend Development

---

# 🚀 Features

## 📚 Book Management

### Add Book

Users can add a new book by providing:

- Book Title
- Author Name
- ISBN Number
- Price

Example

```text
Book Title : Python Programming
Author : Eric Matthes
ISBN : 9780135957059
Price : 850

Book Added Successfully!
```

---

### View Books

Displays all available books.

Information displayed

- Book ID
- Title
- Author
- Price
- Availability Status

Example

```text
ID : 1
Title : Python Programming
Author : Eric Matthes
Price : 850
Status : Available
```

---

### Update Book

Update existing book information.

Example

```text
Enter Book ID : 1

Book Updated Successfully!
```

---

### Delete Book

Remove a book from the library.

---

## 👤 Member Management

### Add Member

Register a new library member.

Required Information

- Full Name
- Email
- Phone Number
- City

Example

```text
Name : Sachin Kunwar
Email : sachin@gmail.com
Phone : 9801234567
City : Butwal

Member Added Successfully!
```

---

### View Members

Displays all registered members.

Information displayed

- Member ID
- Name
- Email
- Phone

---

### Update Member

Modify member details.

---

### Delete Member

Remove a member from the library.

---

## 📖 Borrow Book

Allows a member to borrow a book.

Features

✅ Book Availability Check

✅ Foreign Key Relationship

✅ Automatic Status Update

Example

```text
Member ID : 1

Book ID : 2

Borrow Date : 2026-07-11

Return Date : 2026-07-18

Book Borrowed Successfully!
```

---

## 📕 Return Book

Returns borrowed books.

Features

✅ Updates Borrow Status

✅ Changes Book Status to Available

Example

```text
Borrow ID : 1

Book Returned Successfully!
```

---

## 🔍 Search System

### Search Books

Search books using book title.

Example

```text
Enter Book Name :

Python
```

Output

```text
Python Programming
```

---

### Search Members

Search registered members.

Example

```text
Enter Member Name :

Sachin
```

Output

```text
Sachin Kunwar
```

---

## 📊 Dashboard

Displays overall library statistics.

Shows

- Total Books
- Available Books
- Borrowed Books
- Total Members
- Total Borrow Records

Example

```text
============= DASHBOARD =============

Total Books          : 10

Available Books      : 8

Borrowed Books       : 2

Total Members        : 5

Borrow Records       : 12
```

---

# 🗄️ Database Integration

Database Used

```text
MySQL
```

Tables

- books
- members
- borrow

Database Operations

✅ INSERT

✅ SELECT

✅ UPDATE

✅ DELETE

✅ JOIN

✅ COUNT()

---

# 🛠 MySQL Constraints Used

This project demonstrates practical implementation of MySQL Constraints.

✅ PRIMARY KEY

✅ AUTO_INCREMENT

✅ NOT NULL

✅ UNIQUE

✅ DEFAULT

✅ CHECK

✅ FOREIGN KEY

---

# 🧠 Python Concepts Used

- Functions
- Modular Programming
- Loops
- Conditional Statements
- Exception Handling
- User Input Validation
- Database Connectivity

---

# 🧠 SQL Concepts Used

- INSERT
- SELECT
- UPDATE
- DELETE
- WHERE
- LIKE
- JOIN
- COUNT()
- Parameterized Queries

---

# 📂 Project Structure

```bash
Library-Management-System/
│
├── main.py
├── db.py
├── book.py
├── member.py
├── borrow.py
├── dashboard.py
├── README.md
│
└── Database
```

---

# 📄 File Description

| File | Purpose |
|--------|---------|
| main.py | Application Entry Point |
| db.py | Database Connection |
| book.py | Book Management Operations |
| member.py | Member Management Operations |
| borrow.py | Borrow & Return Operations |
| dashboard.py | Dashboard Statistics |
| README.md | Project Documentation |

---

# ⚙ Database Setup

## Step 1

```sql
CREATE DATABASE library_db;
```

---

## Step 2

```sql
USE library_db;
```

---

## Step 3

### Books Table

```sql
CREATE TABLE books(

book_id INT PRIMARY KEY AUTO_INCREMENT,

title VARCHAR(100) NOT NULL,

author VARCHAR(100) NOT NULL,

isbn VARCHAR(50) UNIQUE,

price DECIMAL(10,2) CHECK(price>0),

status VARCHAR(20) DEFAULT 'Available'

);
```

---

### Members Table

```sql
CREATE TABLE members(

member_id INT PRIMARY KEY AUTO_INCREMENT,

full_name VARCHAR(100) NOT NULL,

email VARCHAR(100) UNIQUE,

phone VARCHAR(20) UNIQUE,

city VARCHAR(50) DEFAULT 'Unknown'

);
```

---

### Borrow Table

```sql
CREATE TABLE borrow(

borrow_id INT PRIMARY KEY AUTO_INCREMENT,

member_id INT,

book_id INT,

borrow_date DATE NOT NULL,

return_date DATE,

status VARCHAR(20) DEFAULT 'Borrowed',

FOREIGN KEY(member_id)
REFERENCES members(member_id),

FOREIGN KEY(book_id)
REFERENCES books(book_id)

);
```

---

# 🔧 Configuration

Open

```python
db.py
```

Update your MySQL credentials.

```python
import mysql.connector

conn=mysql.connector.connect(

host="localhost",

user="root",

password="your_password",

database="library_db"

)

cursor=conn.cursor()
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/library-management-system.git
```

---

## Navigate

```bash
cd library-management-system
```

---

## Install Dependency

```bash
pip install mysql-connector-python
```

---

## Run

```bash
python main.py
```

---

# 📋 Menu Interface

```text
1. Add Book
2. View Books
3. Update Book
4. Delete Book

5. Add Member
6. View Members
7. Update Member
8. Delete Member

9. Borrow Book
10. View Borrowed Books

11. Return Book
12. Borrow History

13. Search Book
14. Search Member

15. Dashboard

16. Exit
```

---

# 🔄 Application Workflow

```text
Start Program
      │
      ▼
Display Menu
      │
      ▼
Select Operation
      │
      ├── Book Management
      ├── Member Management
      ├── Borrow Book
      ├── Return Book
      ├── Search
      ├── Dashboard
      └── Exit
      │
      ▼
Update MySQL Database
      │
      ▼
Display Result
```

---

# 💡 Learning Outcomes

### Python

- Modular Programming
- Functions
- Database Connectivity
- Exception Handling

### MySQL

- CRUD Operations
- Constraints
- JOIN Queries
- Aggregate Functions
- Relational Database Design

### Software Engineering

- Backend Development
- Database Design
- Code Organization
- CLI Application Development

---

# ⚠ Challenges Faced

- Connecting Python with MySQL
- Handling Database Errors
- Implementing Foreign Keys
- Validating User Input
- Preventing Duplicate Records
- Managing Borrow & Return Logic
- Debugging SQL Queries

---

# ✅ Solutions Implemented

✅ Modular Architecture

✅ Relational Database Design

✅ CRUD Operations

✅ Parameterized SQL Queries

✅ Input Validation

✅ Exception Handling

✅ Dashboard Analytics

---

# 🔮 Future Improvements

- Login Authentication
- Fine Calculation
- Transaction History
- Book Categories
- GUI using Tkinter
- Django Web Version
- REST API
- Barcode Scanner Integration

---

# ✨ Key Highlights

📚 Library Management System

🐍 Python Programming

💾 MySQL Database

🗄️ Database Constraints

📖 Borrow & Return Module

👤 Member Management

📊 Dashboard Analytics

🔍 Search System

📂 Modular Project Structure

🚀 Beginner-Friendly Backend Project

---

# 🤝 Contributing

Contributions are welcome.

Feel free to

⭐ Star the repository

🍴 Fork the project

📢 Share suggestions

🚀 Submit Pull Requests

---

# ⭐ Support

If you found this project helpful,

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---

# 👨‍💻 Author

**Saachin Kunwar**

Python Developer | Full Stack Web Developer

<p align="center">
Built with ❤️ while learning Python, MySQL, Database Constraints, CRUD Operations, SQL JOINs, and Backend Development.
</p>
