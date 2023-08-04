# Куда пойти — Москва глазами Артёма

На сайте можно найти самые интересные места для различных видов активного отдыха 
с подробными описаниями и комментариями. Авторский проект Артёма.

![Демо](https://github.com/devmanorg/where-to-go-frontend/blob/master/.gitbook/assets/site.png)

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

Пример [работающего сайта](https://prikur.pythonanywhere.com/).

Чтобы отредактировать локации и/или удалить их, перейдите на [сайт администраторов моделей]().
Для доступа к административному интерфейсу введите логин и пароль.
Тестовые данные в формате **`json`** можно получить [здесь](https://github.com/devmanorg/where-to-go-frontend/tree/master/places).

### Как скачать 

Если вам нужны сами файлы - просто скачайте репозиторий целиком. \
Если нужны для скачивания, то воспользуйтесь интерфейсом Github: выберите файл, откройте его на отдельной странице и нажмите кнопку **`Raw`**. 
Так вы получите ссылку на исходный код файла.

### Как загрузить локации на сайт в ручном режиме

В командной строке введите 
```bash
$ python3 manage.py load_place <ссылка на файл> --settings=where_to_go.settings.prod
```

Если не хотите постоянно выбирать параметр `--settings`, то в командную строку введите:
```bash
export DJANGO_SETTINGS_MODULE=where_to_go.settings.prod
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).