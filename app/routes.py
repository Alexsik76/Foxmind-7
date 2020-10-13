# -*- coding: utf-8 -*-
from flask import render_template, request, abort
from app.race_table import get_report
from app import app

BIG_TABLE = {'Position': 'pos',
             'Abbreviation': 'abr',
             'Name': 'name',
             'Team': 'team',
             'Start time': 'start',
             'Finish time': 'finish',
             'Race time': 'race_time'}

SMALL_TABLE = {'Name': 'name',
               'Abbreviation': 'abr'}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/report/', methods=['GET'])
def report():
    order = request.args.get('order') or ''
    html_report = get_report(order)
    return render_template('report.html', records=html_report, col_names=BIG_TABLE)


@app.route('/report/drivers/', methods=['GET'])
def drivers():
    abr = request.args.get('driver_id') or ''
    order = request.args.get('order') or ''
    if abr:
        driver_info = list(filter(lambda driver: abr == driver.abr, get_report()))\
                      or abort(404, 'Driver not Found')
        return render_template('report.html', records=driver_info, col_names=BIG_TABLE)
    else:
        drivers_html = get_report(order)
        return render_template('drivers.html', records=drivers_html, col_names=SMALL_TABLE)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', error=error)
