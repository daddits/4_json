import json


def load_data(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as f:
        return json.load(f)


def pretty_print_json(json_content):
    for shops in json_content:
        for shop in range(3):
            return json.dumps([
                {
                    'Cells': {
                        'Address': shops[shop]['Cells']['Address'],
                        'AdmArea': shops[shop]['Cells']['AdmArea'],
                        'ClarificationOfWorkingHours': shops[shop]['Cells']['ClarificationOfWorkingHours'],
                        'District': shops[shop]['Cells']['District'],
                        'IsNetObject': shops[shop]['Cells']['IsNetObject'],
                        'Name': shops[shop]['Cells']['Name'],
                        'OperatingCompany': shops[shop]['Cells']['OperatingCompany'],
                        'PublicPhone': [
                            {
                                'PublicPhone': shops[shop]['Cells']['PublicPhone'][0]['PublicPhone']
                            }
                        ],
                        'TypeService': shops[shop]['Cells']['TypeService'],
                        'WorkingHours': [{
                            'DayOfWeek': shops[shop]['Cells']['WorkingHours'][0]['DayOfWeek'],
                            'Hours': shops[shop]['Cells']['WorkingHours'][0]['Hours']
                         },
                         {
                            'DayOfWeek': shops[shop]['Cells']['WorkingHours'][1]['DayOfWeek'],
                            'Hours': shops[shop]['Cells']['WorkingHours'][1]['Hours']
                         },
                         {
                            'DayOfWeek': shops[shop]['Cells']['WorkingHours'][2]['DayOfWeek'],
                            'Hours': shops[shop]['Cells']['WorkingHours'][2]['Hours']
                         },
                         {
                            'DayOfWeek': shops[shop]['Cells']['WorkingHours'][3]['DayOfWeek'],
                            'Hours': shops[shop]['Cells']['WorkingHours'][3]['Hours']
                         },
                         {
                            'DayOfWeek': shops[shop]['Cells']['WorkingHours'][4]['DayOfWeek'],
                            'Hours': shops[shop]['Cells']['WorkingHours'][4]['Hours']
                         },
                         {
                            'DayOfWeek': shops[shop]['Cells']['WorkingHours'][5]['DayOfWeek'],
                            'Hours': shops[shop]['Cells']['WorkingHours'][5]['Hours']
                         },
                         {
                            'DayOfWeek': shops[shop]['Cells']['WorkingHours'][6]['DayOfWeek'],
                            'Hours': shops[shop]['Cells']['WorkingHours'][6]['Hours']
                         }
                        ],
                        'geoData': {
                           'coordinates': [
                               shops[shop]['Cells']['geoData']['coordinates'][0],
                               shops[shop]['Cells']['geoData']['coordinates'][1]
                            ],
                           'type': shops[shop]['Cells']['geoData']['type']
                        },
                        'global_id': shops[shop]['Cells']['global_id']
                    },
                    'Id': shops[shop]['Id'],
                    'Number': shops[shop]['Number']
                 }], sort_keys=True, indent=4)


if __name__ == '__main__':
    json_data = load_data('data.json', 'utf-8')
    print(pretty_print_json(json_data))
