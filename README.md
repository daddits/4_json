# Prettify JSON

Модуль для форматирования JSON-списка алкогольный магазинов в Москве с портала https://data.mos.ru.
Сохраняем данные в файл data.json и передаем его в модуль pprint_json.
Для полкдчения модуля необходимо импортировать модудь json и pprint_json

# Quickstart

```

import json
import pprint_json

load_data('data.json')

```

Example of script launch on Linux, Python 3.5:

```#!bash

$ python3 pprint_json.py data.json

[
    {
        "Cells": {
            "Address": "\u0443\u043b\u0438\u0446\u0430 \u0410\u043a\u0430\u0434\u0435\u043c\u0438\u043a\u0430 \u041f\u0430\u0432\u043b\u043e\u0432\u0430, \u0434\u043e\u043c 10",
            "AdmArea": "\u0417\u0430\u043f\u0430\u0434\u043d\u044b\u0439 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433",
            "ClarificationOfWorkingHours": null,
            "District": "\u0440\u0430\u0439\u043e\u043d \u041a\u0443\u043d\u0446\u0435\u0432\u043e",
...

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
