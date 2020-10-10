# This option does not use classes and uses a minimum of functions.
# Therefore, many Comprehensions are used.
from datetime import datetime
from os.path import join
from collections import namedtuple


PATH = ''
Racer = namedtuple('Racer', ('pos', 'abr', 'name', 'team', 'start', 'finish', 'race_time'))


def read_file(file_name: str) -> list:
    """Reading the any file and return sorted by text list of strings.

    :param file_name: A files name.
    :type file_name: str
    :return: Sorted list of strings.
    :rtype: list
    """
    path_to_file = join(PATH, file_name)
    with open(path_to_file, encoding='utf8') as file:
        sorted_file = sorted([line.strip() for line in file if line.strip()])
    return sorted_file


def parsing_line(line: tuple) -> list:
    """Divides the line in the appropriate format into data.

    :param line: A line combined with three tapes of input files.
    :type line: tuple
    :return: A list of data.
    :rtype: list[str, str, str, datetime, datetime, datetime]
    """
    f_time = '%Y-%m-%d_%H:%M:%S.%f'
    abr, name, team = line[0].split('_')
    start = datetime.strptime(line[1][3:], f_time)
    finish = datetime.strptime(line[2][3:], f_time)
    race_time = datetime.min + abs(finish - start)
    return [abr, name, team, start, finish, race_time]


def get_report() -> list:
    """Creates a time-sorted list of drivers with all the necessary data.

    :return: A sorted by time list of racers.
    :rtype: list
    """
    files = {'name': 'abbreviations.txt',
             'start': 'start.log',
             'finish': 'end.log'}
    source_racers = zip(read_file(files['name']),
                        read_file(files['start']),
                        read_file(files['finish']))
    racers = sorted([parsing_line(line) for line in source_racers],
                    key=lambda lst: lst[5])
    for number, item in enumerate(racers, start=1):
        item.append(number)
    return racers


def get_racer_str(racer: list) -> str:
    """Converts data about each racer into a convenient text format.

    :param racer: A list of the racers data.
    :type racer: list
    :return: A convenient string of the the racers data.
    :rtype: str.
    """
    spec = 'milliseconds'
    return (f'{racer[6]:<4}'
            f'{racer[1]:<20}'
            f'{racer[2]:<27}'
            f'{racer[3].time().isoformat(timespec=spec):<15}'
            f'{racer[4].time().isoformat(timespec=spec):<15}'
            f'{racer[5].time().isoformat(timespec=spec):<15}')


def get_racer_html(racer: list) -> namedtuple:
    """Converts data about each racer into a convenient text format.

    :param racer: A list of the racers data.
    :type racer: list
    :return: A named tuple of the the racers data.
    :rtype: namedtuple.
    """
    t_spec = "milliseconds"
    driver = Racer(str(racer[6]),
                   racer[0],
                   racer[1],
                   racer[2],
                   str(racer[3].time().isoformat(t_spec)),
                   str(racer[4].time().isoformat(t_spec)),
                   str(racer[5].time().isoformat(t_spec)))
    return driver


def get_html_report(sort: str = 'ASC') -> list:
    """Return the sorted by time list of racers.

    Also add a line after the 15-s racer.
    :param sort: Sort order, defaults to 'ASC'
    :type sort: str, optional
    :return: A list of strings of the the racers data.
    :rtype: list.
    """
    racers = get_report()
    racers_str = []
    for racer in racers:
        racers_str.append(get_racer_html(racer))
    if sort.lower() == 'desc':
        racers_str.reverse()
    return racers_str
