#Установка виртуального окружения
---
Установите pyenv с помощью pyenv-installer
```
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```
добавить в 
```
nano ~/bash.profile
```
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || 
export PATH="$PYENV_ROOT/bin:$PATH" eval "$(pyenv init -)"
```
Обновить pyenv
```
pyenv update
```
Удалить pyenv
```
rm -fr ~/.pyenv
```
Затем удалите в .bash

Установка нужной версии
```
pyenv install 3.9.13
```

Установка глобальной версии
```
pyenv global 3.9.13
```

Установка виртуального окружения
```
pyenv global 3.9.13
```

Создаем виртуальное окружение
```
pyenv virtualenv 3.9.13 work 3.9
```
Создать папку проекта
```
 mkdir myproject
 cd myproject
 ```
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

```
3.Запуск виртуальной среды:
```python
virtualenv venv
```
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
