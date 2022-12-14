# Тестовое задание 1 (task_1)

Сервис проведения тестирования по каким-либо темам. Тесты группируются в наборы тестов, которые затем пользователь может проходить и видеть свой результат.

Разработан на фреймворке Django.

## Описание функционала:

Cерсив:
* Регистрация пользователей;
* Аутентификация пользователей;
* Зарегистрированные пользователи могут проходить любой из тестовых наборов;
* Последовательный ответ на все вопросы, каждый вопрос должен выводится на новой странице с отправкой формы (перескакивать через тесты или оставлять неотмеченными нельзя);
* После завершения тестирования можно смотреть результат, количество правильных/неправильных ответов, процент правильных ответов.

Админка Django:
* Возможность на странице набора тестов добавлять вопросы/ответы к вопросам/отмечать правильные ответы;
* Валидация на то, что должен быть хотябы 1 правильный вариант;
* Валидация на то, что все варианты не могут быть правильными;
* Удаление вопросов/вариантов ответов/изменение правильных решений при редактировании тестового набора;

# Тестовое задание 2 (task_2)

Веб-приложение для управления базой данных бонусных карт (карт лояльности, кредитный карт и т.д.)

Разработан на python совместно с:
* Фреймворк Django для построения Web;
* Celery и Redis для автоматического поиска и уаления просроченных карт раз в сутки.

## Описание функционала:

Функционал приложения:
1. список карт с полями: серия, номер, дата выпуска, дата окончания активности, статус;
2. поиск по этим же полям;
3. просмотр профиля карты с историей покупок по ней;
4. активация/деактивация карты;
5. удаление карты;


Дополнительно: 
1. Реализован генератор карт, с указанием серии и количества генерируемых карт, а также "срок окончания активности" со значениями "1 год", "6 месяцев" "1 месяц".
2. После истечения срока активности карты, у карты проставляется статус "просрочена". Првоерка осуществляется автоматически раз в сутки в полночь. 

# Установка и запуск

Реализовано два варианта запуска приложений:
* общий запуск приложений через консоль;
* запуск докер контейнера (только для taks_2 для функций автоматического удаления просроченных писем)

Для всех вариантов склонировать репозиторий с Github.com:
````
git clone https://github.com/Povarenskiy/tasks_krab.git
````

## Общий запуск через консоль 
1. В директории проекта создать виртуальное окружение (venv/ — название виртуального окружения)
````
python -m venv venv
````
2. Активировать виртуальное окружение 
````
venv\Scripts\activate.bat - для Windows
source venv/bin/activate - для Linux и MacOS
````
3. Установка зависимостей
````
pip install -r requirements.txt
````
4. Перейти в дирректорию проекта task_1 или task_2
````
cd task_1
или 
cd task_2
````
5. Создать и применить миграции в базу данных
````
python manage.py makemigrations
python manage.py migrate
````
5. Создать аккаунт администратора  
````
python manage.py createsuperuser
````
6. Запустить сервер
````
python manage.py runserver
````
7. В браузере перейти на localhost порт 8000
````
http://127.0.0.1:8000/
````

## Запуск контейнера

1. В каталоге проекта запустить docker-compose
````
docker-compose up -d
````
2. В браузере перейти на localhost порт 8000
````
http://127.0.0.1:8000/
````

### Панель администратора

1. Создание администратора
````
docker-compose run web python manage.py createsuperuser
````
2. В браузере перейти на панель администратора
````
http://127.0.0.1:8000/admin/
````

