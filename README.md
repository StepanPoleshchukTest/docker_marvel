# Marvel heroes
Проект разворачивается в докере, позволяет добавлять героев, их лозунги и историю. Организовывать баталии между ними, записывать историю боев.
База данных заполняется 8 героями, 19 лозунгами и 10 боями по умолчанию.
### Основные таблицы 
- heroes - Герои - (id, side (сторона, принадлежность), name, birthday, nickname)
- mottos - Лозунги - (id, hero_id, moto_id, moto)
- stories - Краткие истории героев - (id, hero_id, story)
- battles - Столкновения (many-to-many) - id, hero_id_1, motto_id_1, hero_id_2, motto_id_2, winner
### Развертывание 
- Выполняем команду из корня проекта чтобы запустить контейнеры.
> docker-compose up -d --build
- Чтобы остановить из выполняем 
> docker-compose down -v
### Команды внутри проекта
- Вывести справку о имеющихся командах
> python -m scripts
- Вывести всех героев/лозунги/истории/баталии
> python -m scripts show_all_heroes
> 
> python -m scripts show_all_mottos
> 
> python -m scripts show_all_stories
> 
> python -m scripts show_all_battles
- Вы можете добавить героя вручную
> python -m scripts add-hero
- Вы можете добавить Лозунг
> python -m scripts add-story
- Вы можете добавить историю
> python -m scripts add-story
- Вы можете добавить рандомную битву
> python -m scripts add-battle
- Вы можете удалить героя
> python -m scripts delete-hero
