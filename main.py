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

