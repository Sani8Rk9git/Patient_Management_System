# Patient Management System

A web-based Patient Management System built using **Python, Streamlit, FastAPI, and PostgreSQL**. It allows doctors to manage patient records through a simple interface with authentication.

## Features
- **Doctor Registration**: Create a doctor account with a securely hashed password.
- **Doctor Login**: Authenticate doctors using JWT tokens.
- **Patient Management**: Create, view, update, and delete patient records.
- **Patient Information**: Store details such as name, age, gender, city, height, and weight.
- **Verdict calculation**: Calculate the verdict by calculating the BMI from height and weight and display the corresponding category.
- **Authentication**: Protect patient API endpoints using JWT authentication.
- **Logout**: Clear the login token from the current session.

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python     | Complete project |
| Streamlit  | Frontend Interface |
| FastAPI    | REST API    |
| PostgreSQL | Database    |
| SQLAlchemy | Database connectivity|
| Pydantic   | Data validation |
| JWT        | Authentication  |
| Argon2     | Password hashing |


## Project Structure

```
Patient_Management_System/
    - frontend/
        - app.py
        - login.py
        - register.py
        - create.py
        - view.py
        - update.py
        - delete.py
    - backend/
        - main.py
        - database.py
        - models.py
        - auth.py
    - database/
        - schema.sql
    - .env
    - .gitignore
    - requirements.txt
    - README.md

```

## Installation and Setup

1. ### Clone the repository
```
git clone https://github.com/Sani8Rk9git/Patient_Management_System.git
cd Patient_Management_System
```

2. ### Create a virtual environment
```
python -m venv venv

Activate it on Windows:
venv\Scripts\activate
```

3. ### Install dependencies
```
pip install -r requirements.txt
```

4. ### Configure environment variables
```
Create a .env file using .env and add your PostgreSQL database credentials and JWT secret key.
```

5. ### Set up the database
```
Create a PostgreSQL database and execute the SQL commands in database/schema.sql.

```

6. ### Start the FastAPI backend
```
uvicorn backend.main:app --reload
```

7. ### Start the Streamlit frontend
```
Open another terminal:
streamlit run frontend/app.py
```


## Usage
1. Register a new doctor account
2. Log in using the credentials
3. Create, view, update or delete patient records
4. Log out when finished

## Security Note
This project is intended for learning and demonstration purposes. Use dummy patient data only. It has not been designed or validated for handling real medical records.

## Author

**Sanidhya Sharma**

- Github: [Sani8Rk9git](https://github.com/Sani8Rk9git)
- LinkedIn: [Sanidhya Sharma](https://www.linkedin.com/in/sanidhya-sharma-2354303a8)

