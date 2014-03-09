# Using python version 2.7, django version 1.4 and PostgreSQL

# In settings.py file fill out DATABASES and TEMPLATE_DIRS settings

# In mysite directory run 
>python manage.py sqlall news
>python manage.py syncdb
>python manage.py runserver

# URL
enter "http://127.0.0.1:8000" into browser URL for database entry
then enter "http://127.0.0.1:8000/search" into browser URL to search database