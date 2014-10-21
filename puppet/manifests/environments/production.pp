#
# Production node(s). Rename or inherit from this.
#
node production inherits site {
  include uwsgi

  nginx::site { 'app':
    ssl_cert     => '/etc/ssl/certs/your-cert-here.pem',
    ssl_cert_key => '/etc/ssl/private/your-key-here.key',
  }

  uwsgi::app { 'app':
    uwsgi_options => [
      [ processes =>  $::processorcount ],
      [ module    => 'app:create_app()' ],
      [ env       => [
        'FLASK_CONFIG=config/production.py',
      ]],
    ],
  }
}
