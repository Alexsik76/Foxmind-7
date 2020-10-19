# -*- coding: utf-8 -*-
from flask import (Blueprint, abort, render_template, request)
from . import race_table

bp = Blueprint('report', __name__)
BIG_TABLE = {'Position': 'pos',
             'Abbreviation': 'abr',
             'Name': 'name',
             'Team': 'team',
             'Start time': 'start',
             'Finish time': 'finish',
             'Race time': 'race_time'}

SMALL_TABLE = {'Name': 'name',
               'Abbreviation': 'abr'}


@bp.route('/report/', methods=['GET'])
def report():
    order = request.args.get('order') or ''
    html_report = race_table.get_report(order)
    return render_template('report.html', records=html_report, col_names=BIG_TABLE)


@bp.route('/report/drivers/', methods=['GET'])
def drivers():
    abr = request.args.get('driver_id') or ''
    order = request.args.get('order') or ''
    if abr:
        driver_info = list(filter(lambda driver: abr == driver.abr, race_table.get_report())) \
                      or abort(404, 'Driver not found')
        return render_template('report.html', records=driver_info, col_names=BIG_TABLE)
    else:
        drivers_html = race_table.get_report(order)
        return render_template('drivers.html', records=drivers_html, col_names=SMALL_TABLE)


@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', error=error)
