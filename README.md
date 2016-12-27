# Форматирование файла json


О программе

Программа принимает на вход json файл и выводит его содержимое в консоль в удобном формате.
Пример:

 [
{
    "Cells": {
        "Address": "улица Академика Павлова, дом 10",
        "AdmArea": "Западный административный округ",
        "ClarificationOfWorkingHours": null,
        "District": "район Кунцево",
        "IsNetObject": "да",
        "Name": "Ароматный Мир",
        "OperatingCompany": "Ароматный Мир",
        "PublicPhone": [
            {
                "PublicPhone": "(495) 777-51-95"
            }
        ],
        "TypeService": "реализация продовольственных товаров",
        "WorkingHours": [
            {
                "DayOfWeek": "понедельник",
                "Hours": "09:30-22:30"
            },
            {
                "DayOfWeek": "вторник",
                "Hours": "09:30-22:30"
            },
            {
                "DayOfWeek": "среда",
                "Hours": "09:30-22:30"
            },
            {
                "DayOfWeek": "четверг",
                "Hours": "09:30-22:30"
            },
            {
                "DayOfWeek": "пятница",
                "Hours": "09:30-22:30"
            },
            {
                "DayOfWeek": "суббота",
                "Hours": "09:30-22:30"
            },
            {
                "DayOfWeek": "воскресенье",
                "Hours": "09:30-22:30"
            }
        ],
        "geoData": {
            "coordinates": [
                37.39703804817934,
                55.740999719549094
            ],
            "type": "Point"
        },
        "global_id": 14371450
    },
    "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
    "Number": 1
},



Работа с программой

    Запустите файл pprint_json.py
    Укажите имя json файла
