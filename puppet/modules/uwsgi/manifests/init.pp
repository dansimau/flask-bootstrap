#
# Latest uWSGI, installed using pip.
#
class uwsgi ($ensure = 'running') {

  include uwsgi::tuning

  package { 'uwsgi':
    ensure   => installed,
    name     => 'uWSGI',
    provider => 'pip',
  }

  file { ['/etc/uwsgi', '/etc/uwsgi/apps-available', '/etc/uwsgi/apps-enabled']:
    ensure  => directory,
    owner   => root,
    group   => root,
    mode    => '0755',
    require => Package['uwsgi'],
  }

  file { '/etc/init/uwsgi.conf':
    ensure  => file,
    owner   => root,
    group   => root,
    mode    => '0644',
    source  => 'puppet:///modules/uwsgi/etc/init/uwsgi.conf',
    require => Package['uwsgi'],
    notify  => Service['uwsgi'],
  }

  file { '/etc/uwsgi/uwsgi.ini':
    ensure  => file,
    owner   => root,
    group   => root,
    mode    => '0644',
    source  => 'puppet:///modules/uwsgi/etc/uwsgi/uwsgi.ini',
    require => File['/etc/uwsgi'],
    notify  => Service['uwsgi'],
  }

  file { '/etc/logrotate.d/uwsgi':
    ensure  => file,
    owner   => root,
    group   => root,
    mode    => '0644',
    source  => 'puppet:///modules/uwsgi/etc/logrotate.d/uwsgi',
  }

  file { '/etc/init.d/uwsgi':
    ensure => link,
    target => '/lib/init/upstart-job',
    owner  => root,
    group  => root,
    mode   => '0644',
  }

  file { '/var/log/uwsgi':
    ensure  => directory,
    owner   => 'www-data',
    group   => 'www-data',
    require => Package['uwsgi'],
  }

  service { 'uwsgi':
    ensure   => $ensure,
    provider => upstart,
    enable   => true,
    require  => File['/etc/uwsgi/uwsgi.ini'],
  }
}

#
# For defining uWSGI app instances.
#
define uwsgi::app($port = 8000, $uwsgi_options = []) {

  $settings = $::environment ? {
    undef   => 'settings.dev',
    default => "settings.${::environment}",
  }

  $venv = $::venv ? {
    undef   => '/srv/www/app/venv',
    default => $::venv,
  }

  file { "/etc/uwsgi/apps-available/${name}.ini":
    ensure  => present,
    content => template('uwsgi/app.ini.erb'),
    notify  => Service['uwsgi'],
  }

  file { "/var/log/uwsgi/${name}.log":
    ensure => present,
  }

  file { "/etc/uwsgi/apps-enabled/${name}.ini":
    ensure => link,
    target => "/etc/uwsgi/apps-available/${name}.ini",
    notify => Service['uwsgi'],
  }
}
