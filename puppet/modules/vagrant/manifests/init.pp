#
# For developement environment.
#
class vagrant {

  # Set up app directory
  file { '/srv/www':
    ensure => directory,
  }
  file { '/srv/www/app':
    ensure => link,
    target => '/vagrant',
  }

  # Active the app venv on login
  line { 'line-venv-activate':
    ensure => present,
    file   => '/home/vagrant/.bashrc',
    line   => 'cd /vagrant && source .venv/bin/activate',
  }
}
