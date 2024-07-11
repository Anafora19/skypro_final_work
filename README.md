# skypro_final_work
Graduate work. Framework architecture.
Данный проект является продолжением работы по ручному тестированию сервиса, который доступен по ссылке: https://anafora19.atlassian.net/wiki/spaces/~7120200d494c2a1db440a199a1e56f8c646271/pages/29917185
Работа состоит из двух частей: UI и API-тесты.
Основные элементы проверки - возможность поиска книг 
Основные элементы проверки - возможность поиска книг.

1) Стек:
pytest

@@ -12,8 +12,11 @@ requests
allure

2) Струткура:
./methods - Хелперы для работы
./Мethods - папка с методами
./Мethods - папка с тестами
test_ - Тесты
requirements.txt - файл с зависимостями


3) Шаги:
1 - Склонировать проект

@@ -24,3 +27,5 @@ test_ - Тесты
pyp install pytest
pip install selenium
pip install webdriver-manager# skypro_final_project
