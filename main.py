import json
import re
from tqdm import tqdm
import argparse


class File:
    """
    Класс для чтения записей из файла

    Attributes:
        _data : list
        Содержит список считанных данных из текстового файла
    """

    def __init__(self, path: str) -> None:
        self._data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> list:
        return self._data


class Validator:
    """

    """
    _telephone: str
    _weight: int
    _snils: int
    _passport_series: str
    _university: str
    _work_experience: int
    _political_views: str
    _worldview: str
    _address: str
    _invalid_university: list = ['']
    _invalid_political_views: list = ['']
    _invalid_worldview: list = ['']

    def __init__(self, data: dict):
        self._telephone = data['telephone']
        self._weight = data['weight']
        self._snils = data['snils']
        self._passport_series = data['passport_series']
        self._university = data['university']
        self._work_experience = data['work_experience']
        self._political_views = data['political_views']
        self._worldview = data['worldview']
        self._address = data['address']

    def check_telephone(self) -> bool:
        pattern = r"(?:\+7|8)-\(?\d{3}\)?(-\d{2,3}){3}"
        if re.match(pattern, self._telephone):
            return True
        return False

    def check_weight(self) -> bool:
        if (self._weight < 120) and (self._weight > 40) and re.match(r"^\d{2,3}$", str(self._weight)):
            return True
        return False

    def check_snils(self) -> bool:
        if re.match(r"^\d{11}$", str(self._snils)):
            return True
        return False

    def check_passport_series(self) -> bool:
        if re.match(r"^\d{2}\s\d{2}$", self._passport_series):
            return True
        return False

    def check_university(self) -> bool:
        if (re.match(r"^([А-яA-z]+\.?\s?-?)+$", self._university)) and \
                (self._university not in self._invalid_university):
            return True
        return False

    def check_work_experience(self) -> bool:
        if self._work_experience < 60:
            return True
        return False

    def check_political_views(self) -> bool:
        if (re.match(r"^(([А-яA-z])+\.?\s?-?)+$", self._political_views)) and \
                (self._political_views not in self._invalid_political_views):
            return True
        return False

    def check_worldview(self) -> bool:
        if (re.match(r"^([А-яA-z]+\.?\s?-?)+$", self._worldview)) and (self._worldview not in self._invalid_worldview):
            return True
        return False

    def check_adress(self) -> bool:
        if re.match(r"^(ул\.)?(Аллея)?\s[\w\.\s-]+\d+$", self._address):
            return True
        return False
