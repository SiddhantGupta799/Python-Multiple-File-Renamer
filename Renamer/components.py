import re
"""
# good for scrapping out the strings between double quotes 
re.findall(r'"(.*?)"', content)
"""

def remove_date(name: str) -> str:
    # removes dates in the name -> formats: DD/MM/YY or DD-MM-YY or DD.MM.YY or DD/MM/YYYY
    # boundary cases -> 30 and 31 of feb
    name = re.sub(r"([0]?[1-9]|[1|2][0-9]|[3][0|1])[./-]([0]?[1-9]|[1][0-2])[./-]([0-9]{4}|[0-9]{2})", "", name)
    return name


def remove_underscores(name: str) -> str:
    name = re.sub(r"_", " ", name)
    return name


def remove_periods(name: str) -> str:
    name = re.sub(r"\.", " ", name)
    return name


def remove_brackets(name: str) -> str:
    name = re.sub(r"[\(\)\{\}\[\]]", "", name)
    return name


def remove_redundant_spaces(name: str) -> str:
    name = re.sub(r"\s+", " ", name)
    return name


def remove_hyphens(name: str) -> str:
    name = re.sub(r"-", " ", name)
    return name


def beautify_pascal_case(name: str) -> str:
    # ls = re.findall(r"([A-Z][a-z0-9]+)((\d)|([A-Z0-9][a-z0-9]+))*([A-Z])?", name)
    # will implement later
    return name

def remove_youtube_tags(name: str) -> str:
    name = re.sub(r"( - YouTube(_[0-9]?)?)", "", name)
    return name


def remove_links(name: str) -> str:
    name = re.sub(r"(((www(\.))+|(http://)+|(https://)+)(([a-zA-Z0-9]{0,100})(\.)([a-z]{0,3})))", "", name)
    return name


class SongNameFilter:
    __song_link_list = ["mr-jatt.com", "mymp3songs.com", "dailymaza.com"]

    def __remove_bitRate(self, song_name: str) -> str:
        song_name = re.sub(r"([0-9]{0,3})kbps", "", song_name.lower())
        return song_name

    def __remove_stagnant_prefixed_links(self, song_name: str) -> str:
        song_name = song_name.lower()
        for link in self.__song_link_list:
            song_name = song_name.replace(link, "")
        return song_name

    def __remove_links(self, song_name: str) -> str:
        song_name = re.sub(r"((www\.)?|(http://)?|(https://)?)([a-z0-9]{0,100})\.([a-z]{0,4})", "", song_name.lower())
        return song_name

    def __remove_hyphen_and_underscore(self, song_name: str) -> str:
        song_name = re.sub(r"[-_]", " ", song_name)
        return song_name

    def __init__(self, song_name: str):
        song_name = self.__remove_bitRate(song_name)
        song_name = self.__remove_stagnant_prefixed_links(song_name)
        song_name = self.__remove_hyphen_and_underscore(song_name)
        song_name = self.__remove_links(song_name)
        self.__new_name = song_name

    def get_name(self) -> str:
        return self.__new_name
