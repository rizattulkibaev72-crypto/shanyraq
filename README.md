
````markdown
# 🪶 Shanyraq — Psychological Editorial Journal (Django Project)

Shanyraq — это современный психологический журнал, созданный на Django в стиле **Editorial Minimalism 2026**.  
Проект сочетает в себе эстетичный дизайн, чистую типографику и структуру, ориентированную на контент о личности, эмоциях, семье и работе.

---

## 🌈 Features

- ⚙️ **Backend:** Django 5.2  
- 🎨 **Frontend:** HTML5, CSS3, встроенные шаблоны Django  
- 📱 **Адаптивный дизайн** под любые устройства  
- 🧠 **Категории статей:**  
  - Личность  
  - Отношения  
  - Работа  
  - Семья  
  - Эмоции  
- 🧾 Страница “О нас” с современной версткой  
- 👤 Личный кабинет пользователя  
- 🔒 Авторизация и регистрация  
- 🌐 Готовность к деплою на Render / PythonAnywhere  

---

## 🧰 Tech Stack

| Компонент | Используется |
|------------|---------------|
| **Framework** | Django |
| **Language** | Python 3.14 |
| **Database** | SQLite (локально) / PostgreSQL (на хостинге) |
| **Frontend** | HTML, CSS, Django Templates |
| **Server** | Gunicorn + Render |
| **Version Control** | Git + GitHub |

---

## 🚀 Установка и запуск локально

```bash
# 1. Клонировать проект
git clone https://github.com/username/shanyraq.git
cd shanyraq

# 2. Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Выполнить миграции
python manage.py migrate

# 5. Запустить локальный сервер
python manage.py runserver
````

Теперь проект доступен по адресу:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ☁️ Деплой на Render

1. Создай репозиторий на **GitHub** и залей проект.
2. На сайте [Render.com](https://render.com) выбери **New Web Service** → подключи репозиторий.
3. Укажи команды:

```bash
# Build Command
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# Start Command
gunicorn shanyraq.wsgi:application
```

4. Добавь переменные окружения:

```
SECRET_KEY = your_secret_key
DEBUG = False
ALLOWED_HOSTS = shanyraq.onrender.com, shanyraq.kz
```

5. Render выдаст тебе домен вида
   `https://shanyraq.onrender.com`
6. При желании подключи свой домен (`shanyraq.kz`) через CNAME-запись.

---

## 🧱 Структура проекта

```
shanyraq/
│
├── shanyraq/             # Главная конфигурация Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── articles/             # Приложение со статьями
│   ├── templates/
│   ├── models.py
│   └── views.py
│
├── users/                # Приложение пользователей
│   ├── templates/
│   └── forms.py
│
├── static/               # Статические файлы (CSS, JS)
├── templates/            # Общие HTML-шаблоны
├── manage.py
├── requirements.txt
└── Procfile
```

---

## 🎨 Дизайн-система

| Элемент              | Значение                 |
| -------------------- | ------------------------ |
| **Основной фон**     | `#FFFFFF`                |
| **Текст**            | `#0A0A0A`                |
| **Акцентный цвет**   | `#8B5CF6`                |
| **Дополнительный**   | `#F5F0E8`                |
| **Микроакценты**     | `#FFE5D9`                |
| **Шрифт заголовков** | Sans-serif, 900 weight   |
| **Шрифт текста**     | Serif, легкий и читаемый |
| **Line-height**      | 1.8                      |
| **Hover эффекты**    | мягкий персиковый акцент |

---

## 🧑‍💻 Автор проекта

**Rizat Tulkibayev**
📍 Astana, Kazakhstan
🎓 Satbayev University
💡 Проект создан в рамках учебной и творческой практики

---

## 📜 License

This project is licensed under the MIT License — feel free to use and modify it.

---

> ✨ *“Shanyraq — место, где мысли и чувства обретают дом.”*

