<h1> Проект по тестированию сервиса электронных и аудиокниг "Литрес"</h1>

> <a target="_blank" href="https://www.litres.ru">Ссылка на сайт</a>

![This is an image](design/image/litres_page.png)

<h3> Список проверок, реализованных в автотестах:</h3>

### UI-тесты
- [x] Авторизация пользователя на сайте(успешная и неуспешная)
- [x] Поиск книги
- [x] Добавление книги в корзину
- [x] Удаление книги из корзины
- [x] Добавление книги в Избранное
- [x] Удаление книги из Избранного

### API-тесты
- [x] Авторизация пользователя на сайте(успешная и неуспешная)
- [x] Поиск книги
- [x] Добавление книги в корзину

----
### Проект реализован с использованием:
<img src="design/icons/python-original.svg" width="50">
<img src="design/icons/pytest.png" width="50">
<img src="design/icons/intellij_pycharm.png" width="50">
<img src="design/icons/selene.png" width="50">
<img src="design/icons/selenoid.png" width="50">
<img src="design/icons/jenkins.png" width="50">
<img src="design/icons/allure_report.png" width="50">
<img src="design/icons/allure_testops.png" width="50">
<img src="design/icons/tg.png" width="50">
<img src="design/icons/jira.png" width="50">

----
### Локальный запуск
1) Скачать проект и открыть в IDE  
2) Необходимо создать в корне проекта файл `.env` и заполнить его актуальными тестовыми параметрами. Пример такого файла даётся в корне проекта - .env.example
3) Для локального запуска всех тестов с дефолтными значениями необходимо выполнить команду:
```
pytest tests
```
или
```
pytest
```
> Запустить определённый тест отдельно (введя вместо * соответствующие значения)

```commandline
pytest .\tests\web\*.py::*
```
4) Сгенерировать allure-отчёт (локальный) - Windows в корне проекта в папке allure-results  

```commandline
allure.bat serve allure-results
```
или без указания папки (он указан в файле pytest.ini)

```commandline
allure.bat serve
```
### Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/Litres_Project_MS/">Ссылка на проект в Jenkins</a>

#### Параметры сборки


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/Litres_Project_MS/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Указать enviroment, browser_version
4. Указать комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

----
### Allure отчет


#### Общие результаты
![This is an image](design/image/allure_report_overview.png)
#### Список тест кейсов
![This is an image](design/image/allure_report_behaviors.png)
#### Пример отчета о прохождении ui-теста
![This is an image](design/image/example_test_ui_allure.png)
#### Пример отчета о прохождении api-теста
![This is an image](design/image/example_test_api_allure.png)

----
### Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3942/dashboards">Ссылка на проект в AllureTestOps</a> (запрос доступа `admin@qa.guru`)

#### Тест-планы проекта
![This is an image](design/image/allure_TestOps_test_plans.png)

#### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
![This is an image](design/image/allure_TestOps_test_cases.png)

#### Тестовые артефакты
![This is an image](design/image/allure_TestOps_attachment.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](design/image/allure_TestOps_dashboard.png)

#### История запуска тестовых наборов
![This is an image](design/image/allure_TestOps_launches.png)

----
### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1224">Ссылка на проект в Jira</a>

![This is an image](design/image/jira.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](design/image/tg_notification.png)

----
### Пример видео прохождения ui-автотеста
![autotest_gif](design/image/video_add_to_cart.gif)
