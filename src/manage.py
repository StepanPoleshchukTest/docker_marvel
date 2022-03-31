from scripts import add_hero, add_motto, add_story, add_battle, delete_hero, engine
from models import Base


def create_database():
    """
    Дропает и создает БД
    """
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def filling_heroes():
    """
    Заполняет БД (8 героев и историй, 19 лозунгов и 10 боев)
    """

    add_hero(name="Peter Parker", nickname="Spider-Man", side="avengers", birthday="1962-08-15")
    add_hero(name="Steve Rogers", nickname="Captain America", side="avengers", birthday="1918-07-04")
    add_hero(name="Anthony Stark", nickname="Iron Man", side="avengers", birthday="1970-05-29")
    add_hero(name="Wade Wilson", nickname="Deadpool", side="avengers", birthday="1991-02-20")
    add_hero(name="Otto Octavius", nickname="Doctor Octopus", side="villains", birthday="1959-02-17")
    add_hero(name="Loki Laufeyson", nickname="Loki", side="villains", birthday="1949-08-26")
    add_hero(name="Thanos", nickname="Mad Titan", side="villains", birthday="1013-01-01")
    add_hero(name="Quentin Beck", nickname="Mysterio", side="villains", birthday="1963-02-26")

    add_motto(1, "Remember, with great power comes great responsibility")
    add_motto(1, "Turn your world upside down")
    add_motto(1, "It's not so simple!")
    add_motto(2, "I can do this all day")
    add_motto(2, "Before we get started, does anyone want to get out?")
    add_motto(3, "Genius, Billionaire, Playboy, Philanthropist")
    add_motto(3, "JARVIS lets do it!")
    add_motto(3, "I never lose!")
    add_motto(4, "I want to die a natural death at the age of 102 - like the city of Detroit")
    add_motto(4, "You have something in your teeth")
    add_motto(5, "I can't wait to dissect you")
    add_motto(5, "You will slowing down soon, but my arms will never tire")
    add_motto(5, "The power of the sun in the palm of my hand")
    add_motto(5, "What do you want? Die?")
    add_motto(6, "You Can Trust One Thing. I Love To Be Right")
    add_motto(6, "Satisfaction Isn't In My Nature")
    add_motto(7, "Thanos Is Looking For Cosmic Harmony")
    add_motto(7, "Thanos Brings Out A Magic Eraser")
    add_motto(8, "Dead men hear no tales; posthumous fame is an Irish bull")

    add_story(hero_id=1, story="As a result of a radioactive spider bite, high school student Peter Parker developed "
                               "powers and special abilities similar to that of a spider. After Peter's selfishness "
                               "indirectly resulted in the death of his beloved Uncle Ben, Peter decided to live up "
                               "to the motto that 'With great power there must also come great responsibility,' and "
                               "thus became the superhero known as Spider-Man. The alternate versions listed below "
                               "are those of Peter Parker.")
    add_story(hero_id=2, story="During the dark days of the early 1940's, a covert U.S. Military experiment turned "
                               "Steve Rogers into America's first Super-Soldier, Captain America.")
    add_story(hero_id=3, story="Genius billionaire inventor, industrialist and CEO of Stark Industries Tony Stark was "
                               "fatally wounded in a war zone shortly before being kidnapped by terrorists.")
    add_story(hero_id=4, story="Wade Wilson was an international assassin who had worked for various governments when "
                               "he developed an aggressive cancer. In an effort to find a cure, he enrolled in the "
                               "Weapon X program in Canada, which gave him a healing factor from another member and "
                               "set him to work for them.")
    add_story(hero_id=5, story="Dr. Otto Octavius is a highly intelligent and prideful scientist, better known as the "
                               "criminal mastermind Doctor Octopus. During an atomic research project, Octavius' body "
                               "was fused to four mechanical, tentacle-like arms, also causing him severe brain damage "
                               "that turned him into a criminal.")
    add_story(hero_id=6, story="Loki Laufeyson is the Trickster God, God of Mischief, Evil, and Lies a member of the "
                               "monstrous Frost Giants of Jotunheim but was adopted and raised among the Asgardians a "
                               "group of humanoid beings from the pocket dimension of Asgard, the Realm Eternal.")
    add_story(hero_id=7, story="Thanos was one of the last sons of A'Lars, progenitor of the second colony of Eternals "
                               "on Titan, and Sui-San, the last survivor of the original settlement of Eternals on "
                               "Titan. Born with purple, hide-like skin and a massive body due to being born with the "
                               "Deviant Syndrome, Thanos was a morose child who became obsessed with the concept "
                               "of death.")
    add_story(hero_id=8, story="Quentin Beck is a special effects wizard and stunt man working for a major Hollywood "
                               "studio with dreams of making a name for himself in the film industry. However, he came "
                               "to see his career in special effects as a dead-end job. His attempts to become an "
                               "actor were poorly received, but he realized that his expertise in illusions could "
                               "make him an effective criminal.")

    for i in range(20):
        add_battle()


if __name__ == '__main__':
    create_database()
    filling_heroes()
