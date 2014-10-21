#
# Configure nginx for secure SSL by default.
#
class nginx::ssl {
  # Generate secure Diffie-Hellman params for PFS
  exec {'nginx:ssl::generate-dhparams':
    command => '/usr/bin/openssl dhparam -out /etc/ssl/private/dhparam.pem 2048 && chmod 0600 /etc/ssl/private/dhparam.pem &',
    creates => '/etc/ssl/private/dhparam.pem',
  }
}
