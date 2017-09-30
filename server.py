# -*- coding: utf-8 -*-
from flask import Flask
from handlers import site

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    app.register_blueprint(site)
    return app


def main():
    app = create_app()
    debug = app.config['DEBUG']
    port = app.config.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
