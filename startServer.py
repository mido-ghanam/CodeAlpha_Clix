from os import system

system("""
python manage.py makemigrations
python manage.py migrate
clear
python manage.py runserver
""")
