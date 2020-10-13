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
    t_spec = "milliseconds"
    pos = None
    abr, name, team = line[0].split('_')
    start = datetime.strptime(line[1][3:], f_time)
    finish = datetime.strptime(line[2][3:], f_time)
    race_time = datetime.min + abs(finish - start)
    return [pos,
            abr,
            name,
            team,
            start.time().isoformat(t_spec),
            finish.time().isoformat(t_spec),
            race_time.time().isoformat(t_spec)]


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
                    key=lambda lst: lst[6])
    for number, item in enumerate(racers, start=1):
        item[0] = number
    return [Racer(*racer) for racer in racers]


def get_html_report(sort: str = 'ASC') -> list:
    """Return the sorted by time list of racers.

    Also add a line after the 15-s racer.
    :param sort: Sort order, defaults to 'ASC'
    :type sort: str, optional
    :return: A list of strings of the the racers data.
    :rtype: list.
    """
    racers_html = get_report()
    if sort.lower() == 'desc':
        racers_html.reverse()
    return racers_html
