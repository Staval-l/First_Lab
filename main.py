import os
import zipfile
import hashlib

# Задание №1 - Извлечение файлов из архива в директорию
test_zip = zipfile.ZipFile('D:\\tiff-4.2.0_lab1.zip')
test_zip.extractall('D:\\Files')
test_zip.close()


# Задание №2.1 - Поиск и сохранение txt файлов
txt_files = []
for r, d, f in os.walk('D:\\Files'):
    for file in f:
        if file.endswith(".txt"):
            txt_files.append(r + '\\' + file)
print(txt_files)


# Задание №2.2 - Извлечение хэша из найденных txt файлов
result = []
for file in txt_files:
    file_data = open(file, 'rb')
    content = file_data.read()
    result.append(hashlib.md5(content).hexdigest())
    file_data.close()
print(result)
