<p align="center">
    <a href="https://djangochannel.com" target="_blank" rel="noopener noreferrer">
        <img width="100" src="static/logo.png" title="djangochannel">
    </a>
</p>

<h2 align="center">Django Channel Bot</h2>

### Описание проекта:
Telegram bot для группы.

### Инструменты разработки

**Стек:**
- Python >= 3.7
- Django >= 2

**Как работаем:**
- Все предложения и найденные ошибки добавляются в виде Issues на GitHub всеми желающими
- Обсуждаем фичи в чате Telegram
- Пулреквесты по таскам предлагаются всеми желающими, в комментариях к таскам люди пишут что начали делать и когда планируют закончить.
- Пул реквесты обсуждаются командой и сливаются в мастер.

**Ссылки:**
- [Сайт](https://djangochannel.com)
- [Канал Youtube](https://www.youtube.com/channel/UC_hPYclmFCIENpMUHpPY8FQ?view_as=subscriber)
- [Ошибки/Вопросы/Предложения](https://github.com/DJWOMS/django_channel_bot/issues)
- [Задачи GitHub](https://github.com/DJWOMS/django_channel_bot/projects/1)
- [Telegram](https://t.me/trueDjangoChannel)
- [Группа в VK](https://vk.com/djangochannel)
- [Поддержать проект](https://donatepay.ru/don/186076)

**Как стать членом команды:**
- Иметь время на проект
- Иметь необходимые навыки
- Сделать пулл реквест, который будет смержен в основной проект и пообщаться с текущей командой (голос/переписка)
- [Прочитать и создать свои Issues](https://github.com/DJWOMS/django_channel_bot/issues) (вопросы, предложения)

## Разработка

##### 1) Сделать форк репозитория и поставить звездочку)

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) Создать виртуальное окружение

    python -m venv venv
    
##### 4) Активировать виртуальное окружение

##### 5) В папке `django_channel_bot` файл `local_settings.py-example` переименовать в `local_settings.py` и прописать конект к базе

##### 6) Устанавливить зависимости:

    pip install -r req.txt
    
##### 7) Выполнить команду для выполнения миграций

    python manage.py makemigrations
    
##### 8) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 9) Создать суперпользователя

    python manage.py createsuperuser
    
##### 10) Запустить сервер

    python manage.py runserver


### Синхронизировать с основной веткой репозитория проекта, когда она изменилась:


##### 1. Добавить удалённый репозиторий

    git remote add название_ветки_на_локальной_машине https://github.com/DJWOMS/django_channel_bot

##### 2. Проверить добавилась ли ссылка

    git remote -v

##### 3. Синхронизируем с основной веткой на своей машине

    git pull название_ветки_на_локальной_машине develop

##### 4. Внесенные изменения добавляем в ветку в своем репозитории и пушим в свой удаленный репозиторий

    git add .

    git commit -m "четкое_и_понятное_описание_проделанной_работы""

    git push

##### 5. Сделать пулл реквест в основной ветке Django Channel в develop branch

##### Разработка осуществляется через ветку develop

## Команда

[DJWOMS](https://github.com/DJWOMS) 

## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2019-present, DJWOMS - Omelchenko Michael



