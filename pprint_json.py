import json


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        pretty_print_json(json.load(f))


def pretty_print_json(json_content):
    for shop in json_content:
        for x in range(3):
            print(json.dumps([
                {
                    'Cells': {
                        'Address': shop[x]['Cells']['Address'],
                        'AdmArea': shop[x]['Cells']['AdmArea'],
                        'ClarificationOfWorkingHours': shop[x]['Cells']['ClarificationOfWorkingHours'],
                        'District': shop[x]['Cells']['District'],
                        'IsNetObject': shop[x]['Cells']['IsNetObject'],
                        'Name': shop[x]['Cells']['Name'],
                        'OperatingCompany': shop[x]['Cells']['OperatingCompany'],
                        'PublicPhone': [
                            {
                                'PublicPhone': shop[x]['Cells']['PublicPhone'][0]['PublicPhone']
                            }
                        ],
                        'TypeService': shop[x]['Cells']['TypeService'],
                        'WorkingHours': [{
                            'DayOfWeek': shop[x]['Cells']['WorkingHours'][0]['DayOfWeek'],
                            'Hours': shop[x]['Cells']['WorkingHours'][0]['Hours']
                         },
                         {
                            'DayOfWeek': shop[x]['Cells']['WorkingHours'][1]['DayOfWeek'],
                            'Hours': shop[x]['Cells']['WorkingHours'][1]['Hours']
                         },
                         {
                            'DayOfWeek': shop[x]['Cells']['WorkingHours'][2]['DayOfWeek'],
                            'Hours': shop[x]['Cells']['WorkingHours'][2]['Hours']
                         },
                         {
                            'DayOfWeek': shop[x]['Cells']['WorkingHours'][3]['DayOfWeek'],
                            'Hours': shop[x]['Cells']['WorkingHours'][3]['Hours']
                         },
                         {
                            'DayOfWeek': shop[x]['Cells']['WorkingHours'][4]['DayOfWeek'],
                            'Hours': shop[x]['Cells']['WorkingHours'][4]['Hours']
                         },
                         {
                            'DayOfWeek': shop[x]['Cells']['WorkingHours'][5]['DayOfWeek'],
                            'Hours': shop[x]['Cells']['WorkingHours'][5]['Hours']
                         },
                         {
                            'DayOfWeek': shop[x]['Cells']['WorkingHours'][6]['DayOfWeek'],
                            'Hours': shop[x]['Cells']['WorkingHours'][6]['Hours']
                         }
                        ],
                        'geoData': {
                           'coordinates': [
                               shop[x]['Cells']['geoData']['coordinates'][0],
                               shop[x]['Cells']['geoData']['coordinates'][1]
                            ],
                           'type': shop[x]['Cells']['geoData']['type']
                        },
                        'global_id': shop[x]['Cells']['global_id']
                    },
                    'Id': shop[x]['Id'],
                    'Number': shop[x]['Number']
                 }], sort_keys=True, indent=4))


if __name__ == '__main__':
    pass

load_data('data.json')