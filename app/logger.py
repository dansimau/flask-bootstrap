import logging
from logging.handlers import SMTPHandler


def init(app):

    if app.config.get('ERROR_EMAIL'):

        if app.debug:
            logging.getLogger().setLevel(logging.DEBUG)
        else:
            log_format = logging.Formatter('''
    ---
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

%(message)s

    ''')

            # Send errors via email
            mail_handler = SMTPHandler('127.0.0.1',
                                       app.config.get('DEFAULT_MAIL_SENDER'),
                                       app.config.get('ERROR_EMAIL'), 'Error')
            mail_handler.setLevel(logging.ERROR)
            mail_handler.setFormatter(log_format)

            # Also continue to log errors to stderr
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(log_format)

            app.logger.addHandler(stream_handler)
            app.logger.addHandler(mail_handler)
