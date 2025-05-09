# 📓 NotePad — Онлайн Блокнот

Простий онлайн-блокнот на Django: створення, перегляд та редагування нотаток.

---

## Основні можливості:
- Створення нової нотатки.
- Перегляд списку всіх нотаток.
- Детальний перегляд окремої нотатки.
- Редагування існуючих нотаток.
- Авторизація: доступ до перегляду та редагування тільки для залогінених користувачів.
- Захист через CSRF.

![image](https://github.com/user-attachments/assets/91cd5bdc-a34d-492e-b836-72542a149ad3)
![image](https://github.com/user-attachments/assets/b10e0068-5862-4cea-a443-da1a199c5456)

---

##  Стек технологій:
- **Python 3.11+**
- **Django 5.x**
- **Bootstrap 5** (стилізація інтерфейсу)

---

## ⚙️ Встановлення:

1. **Клонувати репозиторій:**
   ```bash
   git clone https://github.com/your-username/note-plus-plus.git
   cd note-plus-plus
   ```

2. **Створити віртуальне середовище та активувати:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / Mac
   venv\Scripts\activate     # Windows
   ```

3. **Встановити залежності:**
   ```bash
   pip install django
   ```

4. **Застосувати міграції:**
   ```bash
   python manage.py migrate
   ```

5. **Створити суперкористувача (за бажанням):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Запустити локальний сервер:**
   ```bash
   python manage.py runserver
   ```

7. **Перейти в браузері:**
   ```
   http://127.0.0.1:8000/
   ```
