import random
import time

AUTHORS = (
    ('Ewa', 'Białołęcka'),
    ('Tomasz', 'Bochiński'),
    ('Małgorzata', 'Borkowska'),
    ('Anna', 'Brzezińska'),
    ('Elżbieta', 'Cherezińska'),
    ('Krystyna', 'Chodorowska'),
    ('Paweł', 'Ciećwierz'),
    ('Jakub', 'Ćwiek'),
    ('Eugeniusz', 'Dębski'),
    ('Rafał', 'Dębski'),
    ('Witold', 'Dzielski'),
    ('Bartosz', 'Grykowski'),
    ('Maciej', 'Guzek'),
    ('Agnieszka', 'Hałas'),
    ('Łukasz', 'Henel'),
    ('Aneta', 'Jadowska'),
    ('Marcin', 'Jamiołkowski'),
    ('Aleksandra', 'Janusz'),
    ('Dorota', 'Kaczyńska-Ciosk'),
    ('Anna', 'Kańtoch'),
    ('Marta', 'Kisiel'),
    ('Krzysztof', 'Kochański'),
    ('Tomasz', 'Kołodziejczak'),
    ('Jacek', 'Komuda'),
    ('Maja Lidia', 'Kossakowska'),
    ('Magdalena', 'Kozak'),
    ('Feliks W.', 'Kres'),
    ('Michał', 'Krzywicki'),
    ('Krystyna', 'Kwiatkowska'),
    ('Piotr Witold', 'Lech'),
    ('Konrad T.', 'Lewandowski'),
    ('Katarzyna Berenika', 'Miszczuk'),
    ('Marcin', 'Mortka'),
    ('Jakub', 'Nowak'),
    ('Jewgienij T.', 'Olejniczak'),
    ('Tadeusz', 'Oszubski'),
    ('Marcin', 'Pągowski'),
    ('Jacek', 'Piekara'),
    ('Andrzej', 'Pilipiuk'),
    ('Krzysztof', 'Piskorski'),
    ('Adam', 'Przechrzta'),
    ('Martyna', 'Raduchowska'),
    ('Magdalena', 'Salik'),
    ('Andrzej', 'Sapkowski'),
    ('Michał', 'Studniarek'),
    ('Iwona', 'Surmik'),
    ('Robert J.', 'Szmidt'),
    ('Wit', 'Szostak'),
    ('Artur', 'Szrejter'),
    ('Robert M.', 'Wegner'),
    ('Andrzej', 'Ziemiański'),
    ('Marek', 'Żelkowski'))

TITLES = (
    "Nieśmiertelni",
    "Ever",
    "Błękitna godzina",
    "W cieniu klątwy",
    "Mroczny płomień",
    "Nocna gwiazda",
    "Kroniki rodu Drake'ów",
    "Księżniczka wampirów",
    "Pojedynki wampirów",
    "Żądza krwi",
    "Najmroczniejsze siły",
    "Wezwanie",
    "Przebudzenie",
    "Odwet",
    "Dziedzictwo mroku",
    "Rasa Środka Nocy",
    "Pocałunek o północy",
    "Szkarłat północy",
    "Przebudzenie o północy",
    "Potęga północy",
    "Welony północy",
    "Cienie północy",
    "Strażnicy wieczności",
    "Kiedy nadciąga ciemność",
    "W objęciach ciemności",
    "Smak ciemność",
    "Nieujarzmiona ciemność",
    "Odwieczna ciemność",
    "Pamięć krwi",
    "Pamiętniki Wampirów",
    "Dom Nocy",
    "Naznaczona",
    "Zdradzona",
    "Wybrana",
    "Nieposkromiona",
    "Osaczona",
    "Kuszona",
    "Spalona",
    "Przebudzona",
    "Piąta pora roku",
    "Królowie Dary",
    "Pod sztandarem Dzikiego Kwiatu",
    "Śmierć Artura",
    "Time",
    "Diuna",
    "Genialna przyjaciółka",
    "Księgi Jakubowe",
    "Saga o Wiedźminie",
    "Jadłonomia po polsku",
    "Wyrwa",
    "Jest krew",
    "Księga Nowego Słońca",
    "Opowieści z meekhańskiego pogranicza",
    "Saga o Fafrdzie i Szarym Kocurze")

PUBLISHERS = (
        {'name': 'Helion',
         'url': 'www.helion.pl',
         'description': None},
        {'name': 'Świat Książki',
         'url': 'wydawnictwoswiatksiazki.pl',
         'description': 'Wydawnictwo'},
        {'name': 'Martel',
         'url': 'wydawnictwomartel.pl', 
         'description': ''},
        {'name': 'Wydawnictwo Centrum',
         'url': 'www.wydawnictwocentrum.pl',
         'description': 'Wydawnictwo'}
)

random.seed(time.time())


def rand_authors(x=1):
    ret = set()

    while len(ret) < x:
        ret.add(random.choice(AUTHORS))

    return ret


def authors():
    for x in AUTHORS:
        yield x


def titles():
    for x in TITLES:
        yield x


def publishers():
    for x in PUBLISHERS:
        yield x


def rand_number_authors():
    return random.randint(1, 3)


def rand_publisher_id(list_pk):
    return random.choice(list_pk)


def rand_isbn():
    return ''.join(map(str, random.choices(range(10), k=15)))


def rand_rating():
    return round(random.uniform(0.0, 5.0), 2)


def rand_pages():
    return random.randint(100, 500)

