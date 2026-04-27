# 5COSC021W-Epic
Software Development Group Project


## Setup and Run Instructions (PowerShell)

### 1. Create virtual environment
```
python -m venv venv
```

### 2. Activate virtual environment
```
venv\Scripts\Activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Apply database migrations
```
python manage.py migrate
```

### 5. Create admin account
```
python manage.py createsuperuser
```
Follow the prompts to set an admin username and password.

### 6. Run server
```
python manage.py runserver
```

### 7. Access application
Open in browser:
```
http://127.0.0.1:8000/
```
Admin panel:
```
http://127.0.0.1:8000/admin/
```
