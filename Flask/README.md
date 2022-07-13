#Flask
---
1. Установка виртуальной среды:
```python
sudo apt install python3-venv
sudo apt-get install python-virtualenv
sudo pip install virtualenv
```
(разные варианты)

2.Создать папку для проекта:
```python
$ mkdir myproject
$ cd myproject
$ virtualenv venv
```
3.Запуск виртуальной среды:
```python
. venv/bin/activate
```
4.Установка Flask:
```python
pip install Flask
```
5.Проверка установки:
```python
python -m flask --version
```
Пример вывода:
```
Python 3.8.5
Flask 1.1.2
Werkzeug 1.0.1
```
