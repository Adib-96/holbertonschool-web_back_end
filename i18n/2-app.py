#!/usr/bin/env python3
''' Flask app '''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' App config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    ''' return best languages '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world():
    ''' return the template '''
    local = get_locale()
    return render_template('2-index.html', local=local)


if __name__ == '__main__':
    app.run()
