# Нарядный JSON

Модуль для форматирования JSON-списка алкогольный магазинов в Москве с портала https://data.mos.ru.
Сохраняем данные в файл data.json и передаем его в модуль pprint_json.
Для полкдчения модуля необходимо импортировать модудь json и pprint_json

# Быстрый старт

```

import json
import pprint_json

print(pretty_print_json(load_data('data.json')))

```

Пример запуска скрипта в системе Linux, Python 3.5:

```#!bash

$ python3 pprint_json.py data.json

[
    {
        "Cells": {
            "Address": "\u0443\u043b\u0438\u0446\u0430,
            "AdmArea": "\u0417\u0430\u043f\u0430\u0434,
            "ClarificationOfWorkingHours": null,
            "District": "\u0440\u0430\u0439\u043e\u043d \u041a\u0443\u043d\u0446\u0435\u0432\u043e",
...

```

# Цели проекта

Данный код является частью образовательного курса web-developers - [DEVMAN.org](https://devman.org)
