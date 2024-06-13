В данном проекте представлена разработка CRM-системы.
Система предназначена для того, чтобы автоматизировать работу с клиентами, в том числе учёт услуг, 
запуск рекламных кампаний, управление потенциальными и активными клиентами, а также подсчёт статистики 
успешности рекламных кампаний.
Этапы создания проекта:
1. Создается репозиторий на локальном компьютере с git-репозиторием, связываем проект с удаленном репозиторием на github.
2. Создаетя файл .gitignore и файл READMY.md
3. Устанавливается django: pip install django
4. Создается файл с зависимостями pip freeze >requirements.txt
5. Создается проект srmsystem: python -m django startproject srmsystem
6. Устанавливаются библиотеки Pillow djangorestframework django-filter drf-spectacular, заморозить зависимости
7. Устанавливается плагин django-request-logging, заморозить зависимости
8. В настройках проекта прописываются LOCALE_PATHS, REST_FRAMEWORK, DEFAULTS, SPECTACULAR_SETTINGS, LOGFILE_NAME, LOGFILE_SIZEL, OGFILE_COUNT, LOGGING, LOGIN_REDIRECT_URL, LOGIN_URL
9. В INSTALLED_APPS добавляются: rest_framework, drf-spectacular, debug_toolbar
10. Создается приложение services - управление услугами: создание, редактирование и просмотр предоставляемых услуг, прописывается в settings.py и urls.py проекта.
11. Создается база данных: python manage.py migrate
12. Создается администратор: python manage.py createsuperuser (задается имя и пароль)
13. 