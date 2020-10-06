# -*- coding: utf-8 -*-
from flask import render_template
from app.race_table import get_html_report
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    column_names = {'Position': 'pos',
                    'Abbreviation': 'abr',
                    'Name': 'name',
                    'Team': 'team',
                    'Start time': 'start',
                    'Finish time': 'finish',
                    'Race time': 'race_time'}
    racers = get_html_report()
    return render_template('report.html', records=racers, colnames=column_names)

