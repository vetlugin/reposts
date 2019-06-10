# Делаем пост с фотографией в трёх социальных сетях

Скрипт размещает текстовый пост с фотографией на стене группы Vkontakte, в группе в Facebook и в канале Telegram с помощью бота.

## Как установить

### Авторизация Вконтакте
Чтобы разместить пост на стене Вконтакте необходимо:
- быть зарегестрированным пользователем Вконтакте
- создать группу для размещения постов или быть администратором в существующей группе
- создать приложение, которое будет размещать пост
- получить ключ доступа (access_token) с правами размещать посты на стене групп
- токен должен давать вам права на постинг: photos, groups, wall и offline.


Токен, версия Вконтакте и ID группы прописывается в файле `.env` таким образом:
```
VK_TOKEN=796ecf344015854e6846e24fa67a4051cc9ab9
VK_VERSION=5.95
VK_GROUP_ID=182385389
```


### Авторизация в Teleggram
Чтобы разместить пост в канале Телеграм необходимо выполнить указания в статье по ссылке:
[Как создать канал, бота в Телеграм](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)

Токен прописывается в файле `.env` таким образом:
```
TELEGRAM_TOKEN=568516423:AAFOQThErHRI
```

### Авторизация на Facebook
Чтобы разместить пост в группе Facebook:
- быть зарегестрированным пользователем Facebook
- создать группу для размещения постов или быть администратором в существующей группе
- создать приложение в Facebook
- получить API ключ, именуемый в Facebook "маркер доступа пользователя". У ключа есть право publish_to_groups.

Токен прописывается в файле `.env` таким образом:
```
FACEBOOK_TOKEN=EAAKJJXkg3KABAA9DVbngTVzPu9uR4w7Ia
```

Файл .env лежит в той же папке что и скрипт.


Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Как запустить

Скрипт запускается из терминала, например:
```
python reposts.py 'Hello' https://icdn.lenta.ru/images/2019/05/25/17/20190525174605940/preview_57ce3fcf62a12a1972416bb791d1e54d.jpg
```
## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
