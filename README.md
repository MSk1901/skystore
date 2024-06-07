## Skystore

Веб-приложение для управления каталогом продуктов.
- регистрация с подтверждением по почте
- CRUD для модели продукта
- кэширование

### Стек технологий:

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0.1-green)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey)](https://www.postgresql.org/)

- `python`
- `django`
- `postgreSQL`

<details>
  <summary>Развертывание и использование</summary>

### 1. Клонируйте проект:

```bash
git clone https://github.com/MSk1901/skystore.git
```

### 2. Перейдите в корневую директорию проекта:

```bash
cd skystore
```

### 3. Настройте переменные окружения: 

   1. Создайте файл `.env` в корневой директории 
   2. Скопируйте в него содержимое файла `.env.sample` и подставьте свои значения
   3. Для корректной работы проекта в локальной среде разработки установите значение `DEBUG=True`, чтобы обеспечить автоматическую обработку статических файлов и подробные сообщения об ошибках.


### 4. Установите зависимости:

```bash
pip install -r requirements.txt
```

### 5. Выполните миграции базы данных:

```bash
python3 manage.py migrate
```

### 6. Запустите сервер разработки:

```bash
python3 manage.py runserver
```

### Использование

Перейдите по адресу http://127.0.0.1:8000/ и пользуйтесь кнопками :)

#### Административная панель:
Для доступа к админке создайте суперпользователя:

```bash
python3 manage.py csu
```

Откройте административную панель по адресу http://127.0.0.1:8000/admin/ и войдите с учетными данными суперпользователя.

</details>

### Автор проекта

Мария Кузнецова - kuznetsova19.m@gmail.com