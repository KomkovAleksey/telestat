# 🤖 [Telestat](https://github.com/KomkovAleksey/QRkot_spreadsheets)


## Оглавление:

- [Технологии](#технологии)
- [Описание проекта](#Описание-проекта)
- [Установка и запуск проекта](#установка-и-запуск-проекта)
- [Авторы проекта](#Авторы-проекта)

## Технологии:

- Python 3.9.10
- SQLalchemy 1.4.36
- Alembic 2.0.29
- Pyrogram 2.0.106
- Google API

## Описание проекта:

Telestat это телеграм бот для сбора статистики телеграм каналов 

В проекте реализованы два бота:

Первый бот(bot_parse) парсит данные о каждом подписчике телегам канала и передает данные в гугл таблицу
 
Второй бот(bot_report) осуществляет запрос данных из гугл таблиц и выводит отчет в чате

## Установка и запуск проекта:

### Установка проекта:

* Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/KomkovAleksey/telestat
```
```
cd telestat
```
Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

* Установите зависимости из файла requirements.txt и обновите pip:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
* Зарегестрируйте свое приложение на сайте https://my.telegram.org/. После  система выдаст вам идентификаторы: api_id и api_hash.

* Создайте .env файл в корневой папке проекта. 
```
touch .env
```

В корневой папке есть файл .env.example,
с примером того как надо заполнять .env файл.

* Применить миграции:
```
alembic upgrade head
```
### Запуск проекта:
```
python main.py 
```

## Авторы проекта:

[Олег Карапоткин](https://github.com/VanDerMusculus) тимлид

[Павел Кошкаров](https://github.com/pavel-koshkarov3)

[Дарья Василевская](https://github.com/dasha2000vas)

[Максим](https://github.com/Maxis1981)

[Алексей Комков](https://github.com/KomkovAleksey)
