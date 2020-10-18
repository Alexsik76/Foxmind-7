from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import views
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/report', endpoint='report')
    app.add_url_rule('/report/drivers', endpoint='drivers')
    return app
