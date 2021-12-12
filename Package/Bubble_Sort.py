import pickle
from tqdm import tqdm
import json


def bubble_sort(data: list, value: str) -> None:
    with tqdm(data, desc="Прогресс сортировки") as pbar:
        for i in range(len(data)):
            swap = False
            for j in range(len(data) - i - 1):
                if float(data[j][value]) > float(data[j+1][value]):
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swap = True
            if not swap:
                pbar.update(len(data) - i)
                break
            pbar.update(1)


def read_data(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as rfile:
        database = json.load(rfile)
    return database


def open_file(file_path: str) -> list:
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data


def save_file(save_path: str, data: list) -> None:
    with open(save_path, 'wb') as file:
        pickle.dump(data, file)


def save_json(save_path: str, data: list) -> None:
    with open(save_path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
