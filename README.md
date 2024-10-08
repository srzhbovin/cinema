# Cinema Ticket Booking Service

## Описание

Этот проект представляет собой **сервис для бронирования билетов в кинотеатре**, разработанный с использованием FastAPI. Сервис предоставляет следующие возможности:

- Получение информации о фильмах и актерах.
- Формирование списка желаемого к просмотру и списка просмотра.
- Оценка фильмов.

## Структура проекта

- `crud.py`: Функции для выполнения операций CRUD (создание, чтение, обновление, удаление) для управления фильмами, пользователями и билетами.
- `models.py`: Определения Pydantic моделей для валидации данных и SQLAlchemy моделей для работы с базой данных.

## Установка

### Установите зависимости

Убедитесь, что у вас установлен Python 3.7 или выше. Затем установите необходимые зависимости:

```bash
pip install fastapi[all] sqlalchemy pydantic
