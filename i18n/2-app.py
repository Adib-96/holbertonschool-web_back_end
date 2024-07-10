#!/usr/bin/env python3
''' Flask app '''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    ''' App config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world():
    local = get_locale()
    ''' return the template '''
    return render_template('2-index.html', local=local)


if __name__ == '__main__':
    app.run()
