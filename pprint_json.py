import json
import pprint
import os
import codecs

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as data_file:
        shops_list = json.load(data_file)
    return shops_list

def pretty_print_json(shops):
    print (json.dumps(shops, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    file_path = input('Введите путь к файлу ')
    shops_list = load_data(file_path)
    pretty_print_json(shops_list)