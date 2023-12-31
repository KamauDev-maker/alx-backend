#!/usr/bin/env python3
"""  Force locale with url parameters
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _, get_locale
from flask_babel import gettext as _

app = Flask(__name__)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    JINJA_ENVIRONMENT_OPTIONS = {
        'autoescape': True,
    }


app.config.from_object(Config)

babel = Babel(app)


# @babel.localeselector
def get_locale() -> str:
    """
    request locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    default route
    """
    return render_template('4-index.html')


if __name__ == '__main__':
     app.run()
