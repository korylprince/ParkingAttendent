# Languages #

Python (2.7)

HTML ([Jinja2](http://jinja.pocoo.org/docs/) templates)

Javascript ([Coffeescript](http://coffeescript.org/))

CSS ([LESS](http://lesscss.org/))

# Database #

[SQLAlchemy](http://www.sqlalchemy.org/) as an ORM. In development using [SQLite](http://www.sqlite.org/) but SQLAlchemy supports many databases.

Could use [Redis](http://redis.io/) or [Memcached](http://memcached.org/) to cache realtime data for scaling to more users.

# Libraries #

## Python ##

[Flask](http://flask.pocoo.org/)

[Flask-Assets](http://elsdoerfer.name/docs/flask-assets/)

[Flask-Restless](http://flask-restless.readthedocs.org/en/latest/)

[Flask-SQLAlchemy](http://pythonhosted.org/Flask-SQLAlchemy/)

[SQLAlchemy](http://www.sqlalchemy.org/)

[cssmin](https://github.com/zacharyvoase/cssmin)

[jsmin](https://bitbucket.org/dcs/jsmin/)

## Javascript ##

[Bootstrap](http://getbootstrap.com/)

[jQuery](http://jquery.com/)

(Plus any of their dependencies)

# Code Snippets #
`templates/bootstrap_base.html` is pieced together from code from [Bootstrap](http://getbootstrap.com/components/#navbar) and [Flask-Bootstrap](https://github.com/mbr/flask-bootstrap).

# Deployment #

[Git](http://git-scm.com/) code respository on [GitHub](https://github.com/).

Deployed in a [virtualenv](http://www.virtualenv.org/en/latest/) with libraries installed with [pip](https://github.com/pypa/pip).

Run with [gunicorn](http://gunicorn.org/) in development and [uwsgi](http://projects.unbit.it/uwsgi/)+[nginx](http://wiki.nginx.org/Main) in production.
