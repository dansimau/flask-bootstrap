from flask.ext.sqlalchemy import SQLAlchemy as FlaskSQLAlchemyBase


class SQLAlchemy(FlaskSQLAlchemyBase):

    def apply_driver_hacks(self, app, info, options):
        """
        Extend Flask-SQLAlchemy's apply_driver_hacks function to apply
        our own hacks.
        """
        super(SQLAlchemy, self).apply_driver_hacks(app, info, options)
        if info.drivername == 'postgresql+psycopg2':
            # Explicitly set client_encoding to utf8, as some systems default
            # to SQL_ASCII which gives unexpected behaviour for in psycopg2's
            # native unicode conversion.
            options['client_encoding'] = 'utf8'


db = SQLAlchemy()

def init(app):
    db.init_app(app)
