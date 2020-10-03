from flask import Flask, render_template
from flask_app.app.flask_module.race_table import print_report

app = Flask(__name__)


@app.route('/')
def index():
    column_names = ('pos', 'name', 'team', 'start', 'finish', 'race_time', )
    racers = print_report()
    return render_template('race_table.html', records=racers)


if __name__ == '__main__':
    app.run()
