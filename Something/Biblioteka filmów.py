from faker import Faker
fake = Faker("pl_PL")

class movie:
    def __init__(self, title, date, type, number_of_plays):
        self.title = title
        self.date = date
        self.type = type
        self.number_of_plays = number_of_plays

movie_1 = movie(title="Django Unchained", date="2012", type="Western", number_of_plays="5")
movie_2 = movie(title="The Wolf of Wall Street", date="2013", type="Biographical / Crime comedy", number_of_plays="5")
movie_3 = movie(title="Forest Gump", date="1994", type="Comedy / Drama", number_of_plays="6")
movie_4 = movie(title="Mad Max: Fury Road", date="2015", type="Sensational / Sci-Fi", number_of_plays="2")
movie_5 = movie(title="Inception", date="2010", type="Thriller / Sci-Fi", number_of_plays="4")

class series:
    def __init__(self, title, date, type, episode_number, season_number, number_of_plays):
        self.title = title
        self.date = date
        self.type = type
        self.episode_number = episode_number
        self.season_number = season_number
        self.number_of_plays = number_of_plays

series_1 = series(title="Arcane", date="2021", type="Animation / Fantasy / Adventure", episode_number="8", season_number="1", number_of_plays="1")
series_2 = series(title="The Witcher", date="2019", type="Fantasy / Adventure", episode_number="1", season_number="1", number_of_plays="2")
series_3 = series(title="Peaky Blinders", date="2013-2021", type="Crime Drama / Historical", episode_number="4", season_number="4", number_of_plays="1")
series_4 = series(title="The Office", date="2005-2013", type="Comedy", episode_number="5", season_number="2", number_of_plays="1")
series_5 = series(title="True Detective", date="2014", type="Drama / Crime", episode_number="4", season_number="1", number_of_plays="2")


