#
# Standalone manifest - for dev Vagrant box.
#
node vagrant-ubuntu-trusty-64 inherits default {
  include vagrant
  include vagrant::pip

  postgresql::role { 'vagrant':
    ensure     => present,
    createdb   => true,
    grant      => 'www-data',
  }

  nginx::site { 'app':
    ssl_cert     => '/etc/ssl/certs/ssl-cert-snakeoil.pem',
    ssl_cert_key => '/etc/ssl/private/ssl-cert-snakeoil.key',
  }

  # Install uwsgi, but don't run automatically at boot
  class { 'uwsgi':
    ensure => stopped,
  }

  uwsgi::app { 'app':
    uwsgi_options => [
      [ processes =>  $::processorcount ],
      [ module    => 'app:create_app()' ],
      [ env       => [
        'FLASK_CONFIG=config/dev.py',
      ]],
    ],
  }
}
