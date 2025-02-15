▎drf-popular-men

▎Описание

drf-popular-men — это API для работы с популярными мужчинами, разработанное на основе Django и Django REST Framework. Проект предоставляет удобные эндпоинты для управления данными о мужчинах, включая их создание, обновление и удаление. Также реализована аутентификация пользователей с использованием токенов.

▎Стек технологий

• Django — основной фреймворк для разработки веб-приложений.

• Django REST Framework — мощный инструмент для создания RESTful API.

• Djoser — библиотека для упрощения аутентификации пользователей.

• Simple JWT — библиотека для работы с JSON Web Tokens (JWT).

• PostgreSQL (или любая другая база данных) — для хранения данных.

▎Инструкция по запуску

1. Клонируйте репозиторий:
      git clone https://github.com/yourusername/drf-popular-men.git
   cd drf-popular-men
   

2. Создайте и активируйте виртуальное окружение:
      python -m venv venv
   source venv/bin/activate  # Для Windows используйте: venvScriptsactivate
   

3. Установите зависимости:
      pip install -r requirements.txt
   

4. Настройте базу данных:

   • Убедитесь, что у вас установлен PostgreSQL (или другая СУБД).

   • Создайте базу данных и настройте параметры подключения в settings.py.

5. Примените миграции:
      python manage.py migrate
   

6. Запустите сервер:
      python manage.py runserver
   

7. API будет доступен по адресу: http://127.0.0.1:8000/api/v1/

▎Спецификация API

▎Аутентификация

• Получение токена:

  • POST /api/v1/token/

  • Тело запроса:
        {
      "username": "your_username",
      "password": "your_password"
    }
    

• Обновление токена:

  • POST /api/v1/token/refresh/

  • Тело запроса:
        {
      "refresh": "your_refresh_token"
    }
    

• Проверка токена:

  • POST /api/v1/token/verify/

  • Тело запроса:
        {
      "token": "your_access_token"
    }
    

▎Работа с мужчинами

• Получение списка мужчин:

  • GET /api/v1/men/

  
• Создание нового мужчины:

  • POST /api/v1/men/

  • Тело запроса:
        {
      "name": "Имя",
      "age": "Возраст",
      "popularity": "Популярность"
    }
    

• Обновление информации о мужчине:

  • PUT /api/v1/men/<int:pk>/

  • Тело запроса:
        {
      "name": "Новое имя",
      "age": "Новый возраст",
      "popularity": "Новая популярность"
    }
    

• Удаление мужчины:

  • DELETE /api/v1/mendelete/<int:pk>/