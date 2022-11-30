# Обрезка ссылок с помощью Битли
В данном проекте Вы сможете сократить свои ссылки, а также получить количество кликов по ним.

## Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```

## Переменная окружения

Переменная окружения - это текстовая переменная с динамическим именем, которая может влиять на поведение запущенных процессов на компьютере/в коде.
Чтобы получить и оформить переменную окружения, которая используется в этом коде Вам необходимо:
1. Получите API-ключ на сайте [Bit.ly](https://bitly.com/)
2. Создайте файл `.env`
3. Заполните `.env` файл согласно примеру:

```python
BITLY_TOKEN=*Ваш токен*
```

##Как запустить

###Если вы хотите получить битли своей ссылки:

```python 
python main.py [Ваша ссылка]
```

Например:

```python 
python main.py https://dvmn.org/
```

###Если вы хотите получить клики по Вашей битли:

```python
python main.py [Ваш битли]
```

Например:

```python
python main.py https://dvmn.org/
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
