# SmartDesign_test

## Установка проекта
Создать виртуальное окружение ```python -m venv venv``` или ```python3 -m venv venv```  
Войти в него ```source venv/biv/activate```  
Установка всех библиотек ```pip instsall -r app/requirements.txt```

#### Установка базы данных
Запустить docker ```sudo systemctl start docker```  
Установит mongo и запустить ```docker run -d -p 27017:27017 mongo```

#### Миграция таблиц в бд
Сбор изменений ```python manage.py makemigrations```  
Применение миграций ```python manage.py migrate```

## Запуск проекта
Запуск напрямую ```python app/manage.py runserver <host>:<port>```


## Проверка работы с помощью curl запросов
##### Запрос на создание (URL - ```/api/create_new_product/```)
```
curl  -H 'Content-Type: application/json' --data '{"name":"test_name", "description":"test_description", "options":[{"key":"test_key", "value":"test_value"}]}' http://0.0.0.0:8000/api/create_new_product/
```
Ответ с данными о товаре
```
{"id":1,"name":"test_name","description":"test_description","options":"[{\"key\": \"test_key\", \"value\": \"test_value\"}]"}
```

##### Запрос на нахождение товара по параметру (Фильтрация по наименованию) (URL - ```/api/get_name_produc/```)
```
curl http://0.0.0.0:8000/api/get_name_product/?name=test_name
```
Ответ на запрос
```
[{"id":1,"name":"test_name"}]
```

##### Запрос на нахождение товара по параметру (Фильтрация по опциям) (URL - ```/api/get_name_produc/```)
```
curl http://0.0.0.0:8000/api/get_name_product/?test_key=test_value
```
Ответ на запрос
```
[{"id":1,"name":"test_name"}]
```

##### Запрос на получение деталий о товаре (URL - ```/api/get_product/```)
```
curl http://0.0.0.0:8000/api/get_product/?id=1
```
Ответ на запрос
```
[{"id":1,"name":"test_name","description":"test_description","options":"[{\"key\": \"test_key\", \"value\": \"test_value\"}]"}]
```
