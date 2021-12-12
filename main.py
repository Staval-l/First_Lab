import json
import re
from tqdm import tqdm
import argparse


parser = argparse.ArgumentParser(description="main.py")
parser.add_argument(
    '-input',
    type=str,
    default="98.txt",
    help="Это строковый аргумент, который подразумевает ввод пути к входному файлу, имеет значение по умолчанию",
    dest="file_input")
parser.add_argument(
    '-output',
    type=str,
    default="Output.txt",
    help="Это строковый аргумент, который подразумевает ввод пути к выходному файлу, имеет значение по умолчанию",
    dest="file_output")
parser.add_argument(
    '-output_',
    type=str,
    default="Output_Fail.txt",
    help="Это строковый аргумент, который подразумевает ввод пути к выходному файлу, имеет значение по умолчанию",
    dest="file_output_")
args = parser.parse_args()

data = File(args.file_input).data
count_valid = 0
count_invalid = 0
dict_invalid_records = {"telephone": 0,
                        "weight": 0,
                        "snils": 0,
                        "passport_series": 0,
                        "university": 0,
                        "work_experience": 0,
                        "political_views": 0,
                        "worldview": 0,
                        "address": 0}
list_result = []
list_fail_result = []

with tqdm(data, desc="Прогресс обработки записей") as progressbar:
    for elem in data:
        check = Validator(elem).check_data()
        if len(check) == 0:
            count_valid += 1
            list_result.append(
                {
                    "telephone": elem["telephone"],
                    "weight": elem["weight"],
                    "snils": elem["snils"],
                    "passport_series": elem["passport_series"],
                    "university": elem["university"],
                    "work_experience": elem["work_experience"],
                    "political_views": elem["political_views"],
                    "worldview": elem["worldview"],
                    "address": elem["address"]
                }
            )
        else:
            count_invalid += 1
            list_fail_result.append(
                {
                    "telephone": elem["telephone"],
                    "weight": elem["weight"],
                    "snils": elem["snils"],
                    "passport_series": elem["passport_series"],
                    "university": elem["university"],
                    "work_experience": elem["work_experience"],
                    "political_views": elem["political_views"],
                    "worldview": elem["worldview"],
                    "address": elem["address"]
                }
            )
            for item in check:
                dict_invalid_records[item] += 1
        progressbar.update(1)

with open(args.file_output, 'w', encoding='utf-8') as output:
    json.dump(list_result, output, indent=4, ensure_ascii=False)

with open(args.file_output_, 'w', encoding='utf-8') as output_:
    json.dump(list_fail_result, output_, indent=4, ensure_ascii=False)

print(f"Count of valid records: {count_valid}")
print(f"Count of invalid records: {count_invalid}")
print("Count of invalid entries by type of error:")
for key, value in dict_invalid_records.items():
    print(" " * 4 + str(key) + ": " + str(value))
