import socket

# No debugging by default; this is overriden dev config
DEBUG = False

# Override this; best to make it different for each environment
SECRET_KEY = ''

# Email address that emails originate from. Make sure it's real, you own it,
# and SPF allows you to send from it.
DEFAULT_MAIL_SENDER = 'vagrant@%s' % socket.getfqdn()

# General email address for admins and errors
ADMIN_RECIPIENTS = ['vagrant@localhost']
ERROR_EMAIL = None

# Database connection string
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://@/app'
