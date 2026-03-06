# Natural Language to SQL Assistant

A web application that allows users to query a database using natural language.
The system converts user questions into SQL queries using an LLM and executes them on a MySQL database.

Built with:

* LangChain
* FastAPI
* MySQL
* SQLAlchemy
* Bootstrap

---

# Project Structure

```
nl_sql_assistant
│
├── app
│   ├── main.py
│   ├── agent.py
│   ├── database.py
│
├── templates
│   └── index.html
│
├── create_db.sql
├── requirements.txt
└── README.md
```

---

# Setup Guide

Follow the steps below to run the project locally.

---

# 1. Clone the Repository

```
git clone https://github.com/kajaldhatrak/Natural-Language-to-SQL-Assistant.git

```

---

# 2. Create Virtual Environment

```
python -m venv venv
```

Activate the environment.

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

# 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# 4. Create the Database

The project includes a SQL file that creates the database, tables, and sample data.

Run:

```
mysql -u root -p < create_db.sql
```

This will create:

Database

```
company_db
```

Tables

```
customers
orders
```

---

# 5. Configure Environment Variables

Create a `.env` file in the root directory.

```
OPENAI_API_KEY=your_openai_api_key
DB_URI=mysql+pymysql://root:password@localhost/company_db
```

Replace `password` with your MySQL password.

---

# 6. Run the Application

Start the backend server.

```
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

# Example Queries

Try asking questions like:

```
Show all customers
```

```
Which customer spent the most money?
```

```
Show total revenue
```

```
List orders after February 2025
```

The AI agent will generate SQL queries and return the results.

---

# Tech Stack

Backend

* Python
* FastAPI

AI Layer

* LangChain
* OpenAI LLM

Database

* MySQL
* SQLAlchemy

Frontend

* Bootstrap

  ---

  # Demo


<img width="1839" height="948" alt="image" src="https://github.com/user-attachments/assets/08857a10-b689-4a6f-92f2-4877f096bcb4" />


<img width="1837" height="901" alt="image" src="https://github.com/user-attachments/assets/e552fb03-1a5a-4dd0-8613-66686fc0eee8" />

