from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

assets = Environment(app)

js = Bundle('js/main.js',
            filters='coffeescript,jsmin', output='min/app.js')
assets.register('js_all', js)

css = Bundle('css/main.css',
            filters='less,cssmin', output='min/screen.css')
assets.register('css_all', css)


if __name__ == '__main__':
    from ParkingAttendent.models import db
    db.create_all()
    from ParkingAttendent.initial_data import propogate
    try:
        propogate()
    except:
        pass

    from ParkingAttendent.views import *
    app.run(debug=True)
