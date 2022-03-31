from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, func, create_engine


from random import choice


Base = declarative_base()


class Hero(Base):
    """
    Модель героя (id, side (сторона, принадлежность), name, birthday, nickname)
    """
    __tablename__ = "heroes"

    id = Column(Integer, autoincrement=True, primary_key=True)
    side = Column(String(40), nullable=False)
    name = Column(String(40), nullable=False)
    birthday = Column(Date())
    nickname = Column(String(40))

    story = relationship("Story", back_populates="hero", cascade="all, delete-orphan", uselist=False)
    mottos = relationship("Motto", back_populates="hero", cascade="all, delete-orphan")

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.id}:{self.name}|{self.side}|" \
               f"birthday:{self.birthday}|" \
               f"nickname:{self.nickname}"

    def get_random_motto(self):
        """
        Возвращает случайный лозунг героя
        """
        return choice(self.mottos)


class Motto(Base):
    """
    Модель лозунга (id, hero_id, moto_id, moto)
    """
    __tablename__ = "mottos"

    id = Column(Integer, autoincrement=True, primary_key=True)
    hero_id = Column(Integer, ForeignKey("heroes.id"))
    motto_id = Column(Integer, nullable=False)
    motto = Column(String(200), nullable=False)

    hero = relationship("Hero", back_populates="mottos")

    def __repr__(self):
        return f"{self.hero_id}:{self.motto_id}:{self.motto}"


class Story(Base):
    """
    Модель краткой истории (id, hero_id, story)
    """
    __tablename__ = "stories"

    id = Column(Integer, autoincrement=True, primary_key=True)
    hero_id = Column(Integer, ForeignKey("heroes.id"))
    story = Column(Text)

    hero = relationship("Hero", back_populates="story")

    def __repr__(self):
        return f"{self.hero_id}:{self.story}"


class Battle(Base):
    """
    Модель столкновения id, hero_id_1, motto_id_1, hero_id_2, motto_id_2, winner (many-to-many)
    """
    __tablename__ = "battles"

    id = Column(Integer, autoincrement=True, primary_key=True)
    hero_id_1 = Column(Integer, nullable=False)
    motto_id_1 = Column(Integer, nullable=False)
    hero_id_2 = Column(Integer, nullable=False)
    motto_id_2 = Column(Integer, nullable=False)
    winner = Column(Integer, nullable=False)

    hero1 = relationship("Hero", foreign_keys=hero_id_1, primaryjoin="Battle.hero_id_1==Hero.id")
    hero2 = relationship("Hero", foreign_keys=hero_id_2, primaryjoin="Battle.hero_id_2==Hero.id")

    motto1 = relationship("Motto", foreign_keys=motto_id_1, primaryjoin="Battle.motto_id_1==Motto.id")
    motto2 = relationship("Motto", foreign_keys=motto_id_2, primaryjoin="Battle.motto_id_2==Motto.id")

    def __repr__(self):
        return f"{self.__class__.__name__} | " \
               f"Hero {self.hero_id_1} motto {self.motto_id_1} VS Hero {self.hero_id_2} motto {self.motto_id_2} | " \
               f"Winner: {self.winner}"

