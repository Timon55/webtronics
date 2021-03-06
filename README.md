# Мануал #

Примечание: сборка docker контейнера проверялась на ОС Windows 11. В проекте присутствет swagger, но он отражает не все методы api.

Если запускать на windows машине и не работает Django Debug Toolbar, то вот решение:
https://stackoverflow.com/questions/64013643/failed-to-load-module-script-the-server-responded-with-a-non-javascript-mime-ty/64638286#64638286


Если нужна админка, то нужно создать суперпользователя с помощью команды "django-admin createsuperuser"
http://127.0.0.1:8000/admin/ 

Наличие в репозитории файла .env.dev и наличие в коде SECRET_KEY и параметров подключения к БД прошу не считать ошибкой,
это было сделано намеренно, чтобы проект можно было запустить одной командой.

Пожалуйста, ознакомьтесь с документаций в папке doc.

Нулевой вариант (без использования docker в отсутствии postgresql)

    Для запуска проекта необходимо:

    0. В зависимости от вашей ОС скачать и установить PostgreSQL.
       Инструкция тут - https://postgrespro.ru/docs/postgresql/14/tutorial-install
       Скачать тут - https://www.postgresql.org/download/

    1. В рабочем каталоге создать виртуальное окружение (venv). Можно сделать через PyCharm либо вручную через
        терминал или консоль в заисимости от ОС. (python -m venv <Имя> , <Имя>\Scripts\activate)

    2. Установить зависимости из файла requirments.txt (pip install -r requirements.txt)

    3. Создать пользователя и БД в PostgreSQL, задать параметры подлкючения в файле settings.py

    4. Сгенерировать и применить миграции с помощью команд "django-admin makemigrations", "django-admin migrate".

    5. Запустить проект используя команду python manage.py runserver Выполнять из корня проекта (директория mysite).

    6. Открыть любой браузер и перейти по адресу  http://127.0.0.1:8000/ (отладочный вебсервер)

    7. Наслаждаться результатом :)


Первый вариант (без использования docker при наличии postgresql)

    Для запуска проекта необходимо:

    0. В рабочем каталоге создать виртуальное окружение (venv). Можно сделать через PyCharm либо вручную через
        терминал или консоль в заисимости от ОС. (python -m venv <Имя> , <Имя>\Scripts\activate)

    1. Установить зависимости из файла requirments.txt (pip install -r requirements.txt)

    2. Создать пользователя и БД в PostgreSQL, задать параметры подлкючения в файле settings.py

    3. Сгенерировать и применить миграции с помощью команд "django-admin makemigrations", "django-admin migrate".

    3. Запустить проект используя команду python manage.py runserver Выполнять из корня проекта (директория mysite).

    4. Открыть любой браузер и перейти по адресу  http://127.0.0.1:8000/ (отладочный вебсервер)

    5. Наслаждаться результатом :)



Второй вариант (с использованием docker)

    Для запуска проекта необходимо:

    0. Убедиться в том что у вас установлен docker-compose

    1. Открыть терминал и перейти в корневой каталог проекта

    2. Выполнить команду "docker-compose up"

    3. Открыть любой браузер и перейти по адресу  http://127.0.0.1:8000/

    4. Наслаждаться результатом :)

