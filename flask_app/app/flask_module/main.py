from flask import Flask, render_template
from flask_app.app.flask_module.race_table import get_html_report

app = Flask(__name__)


@app.route('/report')
def index():
    column_names = {'Position': 'pos',
                    'Abbreviation': 'abr',
                    'Name': 'name',
                    'Team': 'team',
                    'Start time': 'start',
                    'Finish time': 'finish',
                    'Race time': 'race_time'}
    racers = get_html_report()
    return render_template('race_table.html', records=racers, colnames=column_names)


if __name__ == '__main__':
    app.run(debug=True)
