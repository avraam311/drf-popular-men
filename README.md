▎Popular Men API

Сервис, предоставляющий API для получения информации о популярных мужчинах.

▎Используемые технологии:

• PostgreSQL (хранилище данных)
• Docker (для запуска сервиса)
• Django (веб-фреймворк)
• Django REST Framework (для создания RESTful API)
• Djoser (для аутентификации пользователей)
• Simple JWT (для работы с JSON Web Tokens)

Сервис написан с использованием принципов REST.

▎Запуск
1. Склонировать репозиторий:
      git clone https://github.com/yourusername/drf-popular-men.git
   cd drf-popular-men
2. Создать файл .env в директории проекта и заполнить его. Убедитесь, что у вас установлен PostgreSQL и вы создали базу данных. Укажите параметры подключения в файле settings.py.
3. Выполнить в терминале:
      python -m venv venv
   source venv/bin/activate  # Для Windows используйте: venvScriptsactivate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

▎Спецификация API

▎GET /api/v1/men

Возвращает список популярных мужчин. Формат ответа:

{
    "men": [
        {
            "id": 1,
            "name": "Имя",
            "age": 30,
            "popularity": 95
        },
        ...
    ]
}

▎GET /api/v1/men/:id

Возвращает информацию о конкретном мужчине по ID. Формат ответа:

{
    "status": "success",
    "id": 1,
    "name": "Имя",
    "age": 30,
    "popularity": 95
}

▎POST /api/v1/men

Создание нового мужчины. Формат запроса:

{
    "name": "Имя",
    "age": 30,
    "popularity": 95
}

Формат ответа:
{
    "id": 1,
    "name": "Имя",
    "age": 30,
    "popularity": 95
}

▎PUT /api/v1/men/:id

Обновление информации о мужчине. Формат запроса:

{
    "name": "Новое имя",
    "age": 31,
    "popularity": 97
}

Формат ответа:

{
    "id": 1,
    "name": "Новое имя",
    "age": 31,
    "popularity": 97
}

▎DELETE /api/v1/men/:id

Удаление мужчины по ID. Формат ответа:

{
    "message": "Мужчина успешно удален"
}

▎GET /api/v1/men/popular

Возвращает список самых популярных мужчин. Формат ответа:

{
    "popular_men": [
        {
            "id": 2,
            "name": "Популярное Имя",
            "age": 28,
            "popularity": 99
        },
        ...
    ]
}