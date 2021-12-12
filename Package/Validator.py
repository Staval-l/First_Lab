import json
import re
import argparse
from tqdm import tqdm

class File:
    """
    Класс для чтения записей из файла

    Attributes:
        _data : list
        Содержит данные в виде списка, считанные из текстового файла
    """

    def __init__(self, path: str) -> None:
        self._data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> list:
        return self._data


class Validator:
    """
    Класс Validator проверяет данные на корректность
    Attributes:
        _telephone: str - хранит номер телефона пользователя
        _weight: float - хранит вес пользователя
        _snils: str - хранит снилс пользователя
        _passport_series: str - хранит серию паспорта пользователя
        _university: str - хранит вуз пользователя
        _work_experience: float - хранит рабочий стаж пользователя
        _political_views: str - хранит политические взгляды пользователя
        _worldview: str - хранит взгляд на мир пользователя
        _address: str - хранит адрес проживания пользователя
        _invalid_university: list - хранит список с несуществующими университетами
        _valid_political_views: list - хранит список с существующими полит. взглядами
        _valid_worldview: list - хранит список существующих мировоззрений
    """
    _telephone: str
    _weight: float
    _snils: str
    _passport_series: str
    _university: str
    _work_experience: float
    _political_views: str
    _worldview: str
    _address: str
    _invalid_university: list = ['Каражан',
                                 'Бан Ард',
                                 'Аретуза',
                                 'Гвейсон Хайль',
                                 'Хогвартс',
                                 'Кирин-Тор',
                                 'Шармбатон',
                                 'Дурмстранг']
    _valid_political_views: list = ['Индифферентные',
                                    'Социалистические',
                                    'Консервативные',
                                    'Коммунистические',
                                    'Либеральные',
                                    'Умеренные',
                                    'Анархистские',
                                    'Либертарианские']
    _valid_worldview: list = ['Пантеизм',
                              'Секулярный гуманизм',
                              'Деизм',
                              'Атеизм',
                              'Иудаизм',
                              'Католицизм',
                              'Конфуцианство',
                              'Агностицизм',
                              'Буддизм']

    def __init__(self, data: dict):
        """
        Инициализируется объект класса Validator
        :param data: dict
            Передается словарь со всеми полями данных
        """
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
        """
        Метод проверяет номер телефона пользователя
        Если отсутствуют скобки, знак + перед 7, цифр в номере или больше или меньше, то номер является невалидным
        :return: bool
        Возвращается или True или False
        """
        if re.match(r"(?:\+7|8)-\(\d{3}\)(-\d{3})(-\d{2}){2}", self._telephone) is not None:
            return True
        return False

    def check_weight(self) -> bool:
        """
        Метод проверяет вес пользователя
        Если вес является физически невозможным, то вес является невалидным
        :return: bool
        Возвращается или True или False
        """
        if (re.match(r"^\d{2,3}$", str(self._weight)) is not None) and (int(float(self._weight) < 150)) and \
                int((float(self._weight)) > 20):
            return True
        return False

    def check_snils(self) -> bool:
        """
        Метод проверяет снилс пользователя
        Если количество цифр в нем отлично от 11, то снилс невалидный
        :return: bool
        Возвращается или True или False
        """
        if re.match(r"^\d{11}$", self._snils) is not None:
            return True
        return False

    def check_passport_series(self) -> bool:
        """
        Метод проверяет серию паспорта пользователя
        Если количество цифр больше или меньше 4 и цифры не разбиты на пары, то серия невалидная
        :return: bool
        Возвращается или True или False
        """
        if re.match(r"^\d{2}\s\d{2}$", self._passport_series) is not None:
            return True
        return False

    def check_university(self) -> bool:
        """
        Метод проверяет университет пользователя
        Если университета не существует, то он не валидный
        :return: bool
        Возвращается или True или False
        """
        if (re.match(r"^([А-яA-z]+\.?\s?-?)+$", self._university) is not None) and \
                (self._university not in self._invalid_university):
            return True
        return False

    def check_work_experience(self) -> bool:
        """
        Метод проверяет рабочий стаж пользователя
        Если он состоит не из цифр, или превышает разумное значение, то он невалидный
        :return: bool
        Возвращается или True или False
        """
        if (re.match(r"^\d+$", str(self._work_experience)) is not None) and (
                int(float(self._work_experience)) > 0) and (int(float(self._work_experience)) < 60):
            return True
        return False

    def check_political_views(self) -> bool:
        """
        Метод проверяет полит. взгляды пользователя
        Если они не соответствуют существующим полит. взглядам, то они невалидные
        :return: bool
        Возвращается или True или False
        """
        if (re.match(r"^(([А-яA-z])+\.?\s?-?)+$", self._political_views) is not None) and \
                (self._political_views in self._valid_political_views):
            return True
        return False

    def check_worldview(self) -> bool:
        """
        Метод проверяет мировоззрение пользователя
        Если оно не соответствует существующим мировоззрениям, то оно невалидное
        :return: bool
        Возвращается или True или False
        """
        if (re.match(r"^([А-яA-z]+\.?\s?-?)+$", self._worldview) is not None) and \
                (self._worldview in self._valid_worldview):
            return True
        return False

    def check_address(self) -> bool:
        """
        Метод проверяет адрес пользователя
        Если он не начинается с ул. или Аллея, то он невалидный
        :return: bool
        Возвращается или True или False
        """
        if re.match(r"^[A-я.]+\s[\w .()-]+\d+$", self._address) is not None:
            return True
        return False

    def check_data(self) -> list:
        """
        Метод проверяет все поля на корректность
        Если в каком-либо поле найдена ошибка, то оно записывается в список
        :return: list
        Возвращает список с данными пользователя, у которого присутствует невалидная запись
        """
        invalid_values = []
        if not self.check_telephone():
            invalid_values.append("telephone")
        if not self.check_weight():
            invalid_values.append("weight")
        if not self.check_snils():
            invalid_values.append("snils")
        if not self.check_passport_series():
            invalid_values.append("passport_series")
        if not self.check_university():
            invalid_values.append("university")
        if not self.check_work_experience():
            invalid_values.append("work_experience")
        if not self.check_political_views():
            invalid_values.append("political_views")
        if not self.check_worldview():
            invalid_values.append("worldview")
        if not self.check_address():
            invalid_values.append("address")
        return invalid_values