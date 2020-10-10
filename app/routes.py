# -*- coding: utf-8 -*-
from flask import render_template, request
from app.race_table import get_html_report
from app import app

ALL_COLUMNS = {'Position': 'pos',
               'Abbreviation': 'abr',
               'Name': 'name',
               'Team': 'team',
               'Start time': 'start',
               'Finish time': 'finish',
               'Race time': 'race_time'}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/report/', methods=['GET'])
def report():
    sort = request.args.get('order') or ''
    html_report = get_html_report(sort)
    return render_template('report.html', records=html_report, colnames=ALL_COLUMNS)


@app.route('/report/drivers/', methods=['GET'])
def drivers():
    abr = request.args.get('driver_id') or ''
    if abr:
        driver_info = list(filter(lambda driver: abr == driver.abr, get_html_report()))
        if driver_info:
            return render_template('driver.html',  driver_info=driver_info[0], col_names=ALL_COLUMNS)
        else:
            return render_template('not_found.html')
    else:
        column_names = {
            'Name': 'name',
            'Abbreviation': 'abr'
        }
        drivers_html = get_html_report()
        return render_template('drivers.html', records=drivers_html, col_names=column_names)

