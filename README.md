# Куда пойти — Москва глазами Артёма (интерактивная карта Москвы)

На сайте можно найти самые интересные места для различных видов активного отдыха 
с подробными описаниями и комментариями. Авторский проект Артёма.

![Демо](https://dvmn.org/media/lessons/ezgif.com-gif-maker_4nWhtfQ.gif)

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

## Управление локациями

[Пример работающего сайта]().

Чтобы отредактировать локации и/или удалить их, перейдите на сайт администраторов моделей по ссылке: []().
Для доступа к административному интерфейсу введите логин и пароль.
Тестовые данные в формате **`json`** можно получить [здесь](https://github.com/devmanorg/where-to-go-frontend/tree/master/places).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).