# 📓 NotePad

A simple online notepad on Django: create, view, and edit notes.

## Main features:
- Create a new note.
- View a list of all notes.
- Detailed view of an individual note.
- Editing existing notes.
- Authorization: access to view and edit only for logged in users.
- Protection via CSRF.

![image](https://github.com/user-attachments/assets/91cd5bdc-a34d-492e-b836-72542a149ad3)
![image](https://github.com/user-attachments/assets/b10e0068-5862-4cea-a443-da1a199c5456)


---

## ⚙️ Setup:

1. **Clone & open the repository:**
   ```bash
   git clone https://github.com/your-username/note-plus-plus.git
   cd note-plus-plus
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run server:**
   ```bash
   python manage.py runserver
   ```

7. **Перейти в браузері:**
   ```
   http://127.0.0.1:8000/
   ```
##  Demo

https://notepad-zzv5.onrender.com


##  Technology stack:
- **Python 3.11+**
- **Django 5.x**
- **Bootstrap 5**
