import json


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        pretty_print_json(json.load(f))


def pretty_print_json(json_content):
    for value in json_content:
        for x in range(3):
            print(json.dumps([
                {
                    'Cells': {
                        'Address': value[x]['Cells']['Address'],
                        'AdmArea': value[x]['Cells']['AdmArea'],
                        'ClarificationOfWorkingHours': value[x]['Cells']['ClarificationOfWorkingHours'],
                        'District': value[x]['Cells']['District'],
                        'IsNetObject': value[x]['Cells']['IsNetObject'],
                        'Name': value[x]['Cells']['Name'],
                        'OperatingCompany': value[x]['Cells']['OperatingCompany'],
                        'PublicPhone': [
                            {
                                'PublicPhone': value[x]['Cells']['PublicPhone'][0]['PublicPhone']
                            }
                        ],
                        'TypeService': value[x]['Cells']['TypeService'],
                        'WorkingHours': [{
                            'DayOfWeek': value[x]['Cells']['WorkingHours'][0]['DayOfWeek'],
                            'Hours': value[x]['Cells']['WorkingHours'][0]['Hours']
                         },
                         {
                            'DayOfWeek': value[x]['Cells']['WorkingHours'][1]['DayOfWeek'],
                            'Hours': value[x]['Cells']['WorkingHours'][1]['Hours']
                         },
                         {
                            'DayOfWeek': value[x]['Cells']['WorkingHours'][2]['DayOfWeek'],
                            'Hours': value[x]['Cells']['WorkingHours'][2]['Hours']
                         },
                         {
                            'DayOfWeek': value[x]['Cells']['WorkingHours'][3]['DayOfWeek'],
                            'Hours': value[x]['Cells']['WorkingHours'][3]['Hours']
                         },
                         {
                            'DayOfWeek': value[x]['Cells']['WorkingHours'][4]['DayOfWeek'],
                            'Hours': value[x]['Cells']['WorkingHours'][4]['Hours']
                         },
                         {
                            'DayOfWeek': value[x]['Cells']['WorkingHours'][5]['DayOfWeek'],
                            'Hours': value[x]['Cells']['WorkingHours'][5]['Hours']
                         },
                         {
                            'DayOfWeek': value[x]['Cells']['WorkingHours'][6]['DayOfWeek'],
                            'Hours': value[x]['Cells']['WorkingHours'][6]['Hours']
                         }
                        ],
                        'geoData': {
                           'coordinates': [
                               value[x]['Cells']['geoData']['coordinates'][0],
                               value[x]['Cells']['geoData']['coordinates'][1]
                            ],
                           'type': value[x]['Cells']['geoData']['type']
                        },
                        'global_id': value[x]['Cells']['global_id']
                    },
                    'Id': value[x]['Id'],
                    'Number': value[x]['Number']
                 }], sort_keys=True, indent=4))


if __name__ == '__main__':
    pass

load_data('data.json')