### I2AMPARIS Project

## Install project locally

1. Clone the repository 
2. Go to project directory
3. Create virtual environment (python 3.7)
4. Install all requirements:
```bash
pip install -r requirements.txt
```
5. Run server: 
```bash
python3 manage.py runserver 0.0.0.0:8000
```

6. Apply migrations:
```bash
python3 manage.py migrate
```

7. Use SQL files or pg_dump file to populate the database. (if you use the pg_dump file you will have to manually delete the tables created by the migrate command and re-initialise the tables' sequences)

 **The contact and evaluation services do not work in localhost.

Access Point: `http://localhost:8000`


