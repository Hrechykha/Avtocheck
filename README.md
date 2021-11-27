# Avtocheck

Avtocheck это приложение, которое позволяет людям, осмотревшим автомобили перед продажей, поделиться этими данными с другими. Просмотреть информацию может любой пользователь. Добавить информацию по автомобилю возможно только после входа в систему. 

## Предусловие

На вашем компьютере установлен Python 3xx.

## Установка

1) Чтобы установить себе приложение Avtocheck, необходимо клонировать себе [репозиторий](https://github.com/Hrechykha/Avtocheck).

2) В зависимости от того, какую базу данных вы используете, необходимо сделать следующее:

#### SQLite: ####

В PyCharm зайти в Edit Configurations -> Environment variables и добавить переменную **DATABASE_URL** со значением sqlite:///PATH, где PATH это абсолютный путь к файлу БД (sqlite:////full/path/to/your/database/file.sqlite).

Если не установлен PyCharm, то переменную необходимо добавить в переменные окружения вашей ОС. 


#### PostgreSQL: ####

В PyCharm зайти в Edit Configurations -> Environment variables и добавить переменную **DATABASE_URL** со значением postgres://USER:PASSWORD@HOST:PORT/NAME.

Если не установлен PyCharm, то сделать аналогично, как с SQLite.

3) Также понадобится утилита (которая поможет вам загрузить вашу базу данных в словарь из переменной среды DATABASE_URL):

```bash
$ pip install dj-database-url
```

4) Чтобы запустить сервер локально, необходимо выполнить команду  

```bash
DATABASE_URL=sqlite:////path/file.sqlite python /full/path/to/manage.py_file/manage.py runserver
```
