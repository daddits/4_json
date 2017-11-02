import json


def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def pretty_print_json(json_content):
    return json.dumps(json_content, sort_keys=True, indent=4)


if __name__ == '__main__':
    print(pretty_print_json(load_data('data.json')))
