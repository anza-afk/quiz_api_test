
### Запуск проекта:

По примеру .env example нужно создать в корне .env файл с параметрами:

    POSTGRES_USER - Имя пользователя Postgres
    POSTGRES_PASSWORD - Пароль пользователя Postgres
    POSTGRES_DB - Название базы данных
    POSTGRES_PORT - Порт для подключения к БД (например 5432)
    POSTGRES_HOST - Название контейнера из docker-compose (по умолчанию db)

Поднимаем контейнеры коммандой:

    docker-compose up --build -d


### Пример запроса:

    curl -X POST http://127.0.0.1:8000/questions/ -H "Content-Type: application/json" -d '{"question_num": 3}'
