# Avtocheck

Avtocheck это приложение, которое позволяет людям, осмотревшим автомобили перед продажей, поделиться этими данными с другими. Просмотреть информацию может любой пользователь. Добавить информацию по автомобилю возможно только после входа в систему. 

## Установка

1) Чтобы установить себе приложение Avtocheck, необходимо клонировать себе [репозиторий](https://github.com/Hrechykha/Avtocheck). 

2) В зависимости от того, какую базу данных вы используете, необходимо сделать следующее:

#### SQLite: ####

В PyCharm зайти в Edit Configurations -> Environment variables и добавить переменную **DATABASE_URL** со значением sqlite:///PATH, где PATH это абсолютный путь к файлу БД (sqlite:////full/path/to/your/database/file.sqlite).

#### PostgreSQL: ####

В PyCharm зайти в Edit Configurations -> Environment variables и добавить переменную **DATABASE_URL** со значением postgres://USER:PASSWORD@HOST:PORT/NAME.

3) Также понадобится утилита (которая поможет вам загрузить вашу базу данных в словарь из переменной среды DATABASE_URL:

```bash
$ pip install dj-database-url
```
