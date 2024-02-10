# Task

Тестовое задание

1. Скачать проект:
git clone https://github.com/AlenaSapfirova/task_1/

3. Установить python:
pip install python 3.10 - windows
sudo apt install python3.10-venv - linux

3. Установить виреуальное окружение и активировать его:
python3.10 -m venv venv
source venv/bin/activate - linux
source venv/Scripts/activate

2. Создать файл .env:
touch .env
3. Скопировать в этот файл содержимое файла .env.example

4. Установить зависимости:
pip install -r requirements.txt

5. Перейти с директорию backend
6. Совершить миграции:
python manage.py makemigrations
python manage.py migrate

7. Запустить проект локально:
python manage.py runserver

Внешний API доступен по адресу http://127.0.0.1:8000/api/docs/
