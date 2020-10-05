from app import app
from app import race_table


race_table.PATH = app.config['DATA_PATH']
