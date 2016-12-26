import json
import pprint
import os
import codecs

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as data_file:
        data = json.load(data_file)
    return data

def pretty_print_json(data):
    print (json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    file_path = input('Введите путь к файлу ')
    json_data = load_data(file_path)
    pretty_print_json(json_data)