import os
import zipfile
import hashlib
import re
import requests


# Задание №1 - Извлечение файлов из архива в директорию
arch_path = 'D:\\tiff-4.2.0_lab1.zip'
directory_to_extract = 'D:\\Files'

test_zip = zipfile.ZipFile(arch_path)
test_zip.extractall(directory_to_extract)
test_zip.close()


# Задание №2.1 - Поиск и сохранение txt файлов
txt_files = []
for r, d, f in os.walk(directory_to_extract):
    for file in f:
        if file.find(".txt"):
            txt_files.append(r + os.path.sep + file)
print(txt_files)
print('===============' *5)


# Задание №2.2 - Извлечение хэша из найденных txt файлов
result = []
for file in txt_files:
    file_data = open(file, 'rb').read()
    file_hash = hashlib.md5(file_data).hexdigest()
    result.append(file_hash)
print(result)
print('===============' *5)


# Задание №3 - Найти файл, хэш которого равен: "4636f9ae9fef12ebd56cd39586d33cfb"
target_hash = '4636f9ae9fef12ebd56cd39586d33cfb'
file_path = ''
file_content = ''
for r, d, f in os.walk(directory_to_extract):
    for i in f:
        file_data = open(r + os.path.sep + i, 'rb').read()
        file_hash = hashlib.md5(file_data).hexdigest()
        if file_hash == target_hash:
            file_path = r + os.path.sep + i
            file_content = open(r + os.path.sep + i, 'r').read()
print(file_path)
print(file_content)
print('===============' *5)

# Задание №4 - Получить содержимое веб-страницы
r = requests.get(file_content)
result_dct = {}

counter = 0
headers = []
lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)
for line in lines:
    if counter == 0:
        headers = re.findall('([А-ЯЁа-яё]+ ?[А-ЯЁа-яё]*)+', line)
        counter += 1
    else:
        tmp = re.sub('<.*?>', ';', line)
        tmp = re.sub(r'(\(\+\d+\s?\d*\))', ';', tmp)
        tmp = re.sub('(;)+', ';', tmp)
        tmp = re.sub('(_)', '0', tmp)
        tmp = re.sub(r'(\*)', '', tmp)
        tmp = tmp[3:].strip()
        tmp = re.sub(r';$', '', tmp)
        tmp = re.sub(r'^;', '', tmp)
        tmp = re.sub(r'\xa0', '', tmp)
        tmp_split = tmp.split(';')

        country_name = tmp_split[0]

        col1_val = tmp_split[1]
        col2_val = tmp_split[2]
        col3_val = tmp_split[3]
        col4_val = tmp_split[4]
        counter += 1

        result_dct[country_name] = {}
        result_dct[country_name][headers[0]] = int(col1_val)
        result_dct[country_name][headers[1]] = int(col2_val)
        result_dct[country_name][headers[2]] = int(col3_val)
        result_dct[country_name][headers[3]] = int(col4_val)

        print(country_name, result_dct[country_name])
print('===============' *5)


# Задание №5 - Запись данных из полученного словаря в файл
output = open('data.csv', 'w')
headline = '; '.join(headers)
output.write('Страна;' + headline + '\n')
for key in result_dct.keys():
    values_of_dict = result_dct[key].values()
    row = '; '.join(map(str, values_of_dict))
    output.write(key + ';' + row + '\n')
output.close()


# Задание №6 - Вывод на экран для указанной страны
target_country = input("Введите название страны: ")
f = False
for key in result_dct.keys():
    if key.lower() == target_country.lower():
        print(key + ': ' + str(result_dct[key]))
        f = True
if not f:
    print('Данной страны нет в списке')
