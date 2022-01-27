### Проект api_yamdb

```
API социальной сети с отзывами на фильмы, книги и музыку.
Здесь вы можете зарегистрироваться, чтобы поделиться своим мнением о понравившемся или раздражающем произведении, а ваши друзья смогут прочитать ваш отзыв и оставить к нему комментарии. Также вы можете почитать отзывы об интересующем вас произведении и обсудить их в комментариях с другими пользователями.
Для вежливых граммар-наци есть возможность стать модераторами, чтобы поддерживать чистоту и взаимоуважение на платформе.
```

Разработчики:

```
https://github.com/Drvmnekta
Пользователи и аутентификация
```

```
https://github.com/JacksonHi
Отзывы и комментарии
```

```
https://github.com/avb15214yp
Произведения и категории
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Документация с примерами запросов и ответов на них по адресу 
```
http://127.0.0.1:8000/redoc/
```