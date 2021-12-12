import pickle
from tqdm import tqdm


def bubble_sort(data: list, value: str) -> None:
    with tqdm(data, desc="Прогресс сортировки") as pbar:
        for i in range(len(data)):
            swap = False
            for j in range(len(data) - i - 1):
                if data[j][value] > data[j + 1][value]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swap = True
            if not swap:
                pbar.update(len(data) - i)
                break
            pbar.update(1)


def open_file(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = pickle.load(file)
    return data


def save_file(save_path: str, data: list) -> None:
    with open(save_path, 'w', encoding='utf-8') as file:
        pickle.dump(data, file)
