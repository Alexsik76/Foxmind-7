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


def parsing_line(line: tuple) -> tuple:
    """Divides the line in the appropriate format into data.

    :param line: A line combined with three tapes of input files.
    :type line: tuple
    :return: A list of data.
    :rtype: tuple[str, str, str, datetime, datetime, datetime]
    """
    f_time = '%Y-%m-%d_%H:%M:%S.%f'
    t_spec = "milliseconds"
    abr, name, team = line[0].split('_')
    start = datetime.strptime(line[1][3:], f_time)
    finish = datetime.strptime(line[2][3:], f_time)
    race_time = datetime.min + abs(finish - start)
    return (abr,
            name,
            team,
            start.time().isoformat(t_spec),
            finish.time().isoformat(t_spec),
            race_time.time().isoformat(t_spec))


def get_report(sort: str = 'ASC') -> list:
    """Creates a time-sorted list of drivers with all the necessary data.

    :param sort: Sort order, defaults to 'ASC'
    :type sort: str, optional
    :return: A sorted by time list of racers.
    :rtype: list[NamedTuple[[int, str, str, str, datetime, datetime, datetime]]]
    """
    # TODO replace reverse to views
    files = ('abbreviations.txt', 'start.log', 'end.log')
    reverse = (sort.lower() == 'desc')
    source_racers = zip(*[read_file(file_name) for file_name in files])
    racers = sorted([parsing_line(line) for line in source_racers],
                    key=lambda lst: lst[5])
    numerated_racers = [Racer(number, *item) for number, item in enumerate(racers, start=1)]
    return reversed(numerated_racers) if reverse else numerated_racers
