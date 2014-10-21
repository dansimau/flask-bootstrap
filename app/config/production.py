import socket

DEFAULT_MAIL_SENDER = 'www-data@%s' % socket.getfqdn()

ADMIN_RECIPIENTS = ['devs@tobias.tv']
ERROR_EMAIL = 'devs@tobias.tv'

# dd bs=1 count=32 if=/dev/random |pbcopy
SECRET_KEY = ''
