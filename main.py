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

