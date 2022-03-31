import logging
import random
from datetime import date

import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import functions

from models import Hero, Motto, Story, Battle


# Движок, сессия
engine = create_engine("postgresql+psycopg2://user:rootroot@db:5432/marvel")
Session = sessionmaker(bind=engine)
session = Session()

# тайпер
app = typer.Typer(help="Small simulation for horizons universe")

# log.txt <= DEBUG
logging.basicConfig(
    filename="logs.txt",
    format="%(asctime)s => %(filename)s => %(levelname)s => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG   # (DEBUG->INFO->WARNING->ERROR->CRITICAL)
)

# Для консоли
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console_formatter = logging.Formatter("%(asctime)s => %(filename)s => %(levelname)s => %(message)s")
console.setFormatter(console_formatter)

# Хэндлер в handler_logs.txt
file = logging.FileHandler(filename="handler_logs.txt")
file.setLevel(logging.ERROR)
file_formatter = logging.Formatter("%(asctime)s => %(filename)s => %(levelname)s => %(message)s")
console.setFormatter(file_formatter)

root_logger = logging.getLogger("")

root_logger.addHandler(console)
root_logger.addHandler(file)


class DrawFilter(logging.Filter):  # фильтр на событие, на ничью
    def filter(self, record):
        return not (record.msg.startswith("Battle") and record.msg.endswith("0"))

root_logger.addFilter(DrawFilter())


@app.command()
def add_hero(name, nickname, birthday, side):
    """
    Добавляет героя
    """
    if birthday:  # преведение
        birthday = date.fromisoformat(birthday)

    new_hero = Hero(name=name, nickname=nickname, birthday=birthday, side=side)
    session.add(new_hero)
    session.commit()

    logging.info(f"Герой создан: {new_hero}")


@app.command()
def add_motto(hero_id, motto):
    """
    Добавляет лозунг для героя
    """
    hero = session.query(Hero).get(hero_id)

    if hero:
        motto_id = len(hero.mottos) + 1
        hero.mottos.append(Motto(motto_id=motto_id, motto=motto))

        session.commit()
        logging.info(f"Добавлен лозунг {motto} для героя {hero_id}")
    else:
        logging.error(f"Герой {hero_id} не найден")
        raise Exception('Герой не найден')


@app.command()
def add_story(hero_id, story):
    """
    Добавляет/обновляет краткую историю героя
    """
    hero = session.query(Hero).get(hero_id)

    if hero:
        if hero.story:
            hero.story.story = story
            logging.info(f"Обновлена история для героя {hero_id}")
        else:
            hero.story = Story(story=story)
            logging.info(f"Добавлена история  для героя {hero_id}")

        session.commit()
    else:
        logging.error(f"Герой {hero_id} не найден")
        raise Exception('Герой не найден')


@app.command()
def delete_hero(hero_id):
    """
    Удаляет героя, все его лозунги и его историю
    """
    hero = session.query(Hero).get(hero_id)

    if hero:
        session.delete(hero)
        session.commit()
        logging.info(f"Герой {hero_id} удален")
    else:
        logging.warning(f"Герой {hero_id} не существует")


@app.command()
def add_battle(battles_quantity=1):
    """
    Случайно добавляет двух героев с противоположных сторон, случайно выбирает победителя
    """
    first_fighter = session.query(Hero).order_by(functions.random()).first()
    second_fighter = session.query(Hero).filter(Hero.side != first_fighter.side).order_by(functions.random()).first()

    first_fighter_motto = first_fighter.get_random_motto()
    second_fighter_motto = second_fighter.get_random_motto()

    winner = random.choice([0, 1, 2])

    for battle in range(battles_quantity):
        new_battle = Battle(hero_id_1=first_fighter.id,
                            hero_id_2=second_fighter.id,
                            motto_id_1=first_fighter_motto.id,
                            motto_id_2=second_fighter_motto.id,
                            winner=winner)

        session.add(new_battle)
        session.commit()

    logging.info(f"Бой: {first_fighter.name} VS {second_fighter.name}. Побелитель: {winner}")


@app.command()
def show_all_heroes():
    """
    Выводит всех героев
    """
    print("Heroes:")
    for hero in session.query(Hero).all():
        print(hero)

@app.command()
def show_all_mottos():
    """
    Выводит все лозунги
    """
    print("Mottos:")
    for motto in session.query(Motto).all():
        print(motto)

@app.command()
def show_all_stories():
    """
    Выводит все истории героев
    """
    print("Stories:")
    for story in session.query(Story).all():
        print(story)

@app.command()
def show_all_battles():
    """
    Выводит все сражения
    """
    print("Battles:")
    for battle in session.query(Battle).all():
        print(battle)


if __name__ == "__main__":
    app()