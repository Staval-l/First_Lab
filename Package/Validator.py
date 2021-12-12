import json
import re
import argparse
from tqdm import tqdm

class File:
    """
    ����� ��� ������ ������� �� �����

    Attributes:
        _data : list
        �������� ������ � ���� ������, ��������� �� ���������� �����
    """

    def __init__(self, path: str) -> None:
        self._data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> list:
        return self._data


class Validator:
    """
    ����� Validator ��������� ������ �� ������������
    Attributes:
        _telephone: str - ������ ����� �������� ������������
        _weight: float - ������ ��� ������������
        _snils: str - ������ ����� ������������
        _passport_series: str - ������ ����� �������� ������������
        _university: str - ������ ��� ������������
        _work_experience: float - ������ ������� ���� ������������
        _political_views: str - ������ ������������ ������� ������������
        _worldview: str - ������ ������ �� ��� ������������
        _address: str - ������ ����� ���������� ������������
        _invalid_university: list - ������ ������ � ��������������� ��������������
        _valid_political_views: list - ������ ������ � ������������� �����. ���������
        _valid_worldview: list - ������ ������ ������������ �������������
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
    _invalid_university: list = ['�������',
                                 '��� ���',
                                 '�������',
                                 '������� �����',
                                 '��������',
                                 '�����-���',
                                 '���������',
                                 '����������']
    _valid_political_views: list = ['��������������',
                                    '����������������',
                                    '��������������',
                                    '����������������',
                                    '�����������',
                                    '���������',
                                    '������������',
                                    '���������������']
    _valid_worldview: list = ['��������',
                              '���������� ��������',
                              '�����',
                              '������',
                              '�������',
                              '����������',
                              '�������������',
                              '�����������',
                              '�������']

    def __init__(self, data: dict):
        """
        ���������������� ������ ������ Validator
        :param data: dict
            ���������� ������� �� ����� ������ ������
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
        ����� ��������� ����� �������� ������������
        ���� ����������� ������, ���� + ����� 7, ���� � ������ ��� ������ ��� ������, �� ����� �������� ����������
        :return: bool
        ������������ ��� True ��� False
        """
        if re.match(r"(?:\+7|8)-\(\d{3}\)(-\d{3})(-\d{2}){2}", self._telephone) is not None:
            return True
        return False

    def check_weight(self) -> bool:
        """
        ����� ��������� ��� ������������
        ���� ��� �������� ��������� �����������, �� ��� �������� ����������
        :return: bool
        ������������ ��� True ��� False
        """
        if (re.match(r"^\d{2,3}$", str(self._weight)) is not None) and (int(float(self._weight) < 150)) and \
                int((float(self._weight)) > 20):
            return True
        return False

    def check_snils(self) -> bool:
        """
        ����� ��������� ����� ������������
        ���� ���������� ���� � ��� ������� �� 11, �� ����� ����������
        :return: bool
        ������������ ��� True ��� False
        """
        if re.match(r"^\d{11}$", self._snils) is not None:
            return True
        return False

    def check_passport_series(self) -> bool:
        """
        ����� ��������� ����� �������� ������������
        ���� ���������� ���� ������ ��� ������ 4 � ����� �� ������� �� ����, �� ����� ����������
        :return: bool
        ������������ ��� True ��� False
        """
        if re.match(r"^\d{2}\s\d{2}$", self._passport_series) is not None:
            return True
        return False

    def check_university(self) -> bool:
        """
        ����� ��������� ����������� ������������
        ���� ������������ �� ����������, �� �� �� ��������
        :return: bool
        ������������ ��� True ��� False
        """
        if (re.match(r"^([�-�A-z]+\.?\s?-?)+$", self._university) is not None) and \
                (self._university not in self._invalid_university):
            return True
        return False

    def check_work_experience(self) -> bool:
        """
        ����� ��������� ������� ���� ������������
        ���� �� ������� �� �� ����, ��� ��������� �������� ��������, �� �� ����������
        :return: bool
        ������������ ��� True ��� False
        """
        if (re.match(r"^\d+$", str(self._work_experience)) is not None) and (
                int(float(self._work_experience)) > 0) and (int(float(self._work_experience)) < 60):
            return True
        return False

    def check_political_views(self) -> bool:
        """
        ����� ��������� �����. ������� ������������
        ���� ��� �� ������������� ������������ �����. ��������, �� ��� ����������
        :return: bool
        ������������ ��� True ��� False
        """
        if (re.match(r"^(([�-�A-z])+\.?\s?-?)+$", self._political_views) is not None) and \
                (self._political_views in self._valid_political_views):
            return True
        return False

    def check_worldview(self) -> bool:
        """
        ����� ��������� ������������� ������������
        ���� ��� �� ������������� ������������ ��������������, �� ��� ����������
        :return: bool
        ������������ ��� True ��� False
        """
        if (re.match(r"^([�-�A-z]+\.?\s?-?)+$", self._worldview) is not None) and \
                (self._worldview in self._valid_worldview):
            return True
        return False

    def check_address(self) -> bool:
        """
        ����� ��������� ����� ������������
        ���� �� �� ���������� � ��. ��� �����, �� �� ����������
        :return: bool
        ������������ ��� True ��� False
        """
        if re.match(r"^[A-�.]+\s[\w .()-]+\d+$", self._address) is not None:
            return True
        return False

    def check_data(self) -> list:
        """
        ����� ��������� ��� ���� �� ������������
        ���� � �����-���� ���� ������� ������, �� ��� ������������ � ������
        :return: list
        ���������� ������ � ������� ������������, � �������� ������������ ���������� ������
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