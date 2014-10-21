#
# Ensure New Relic server monitoring daemon is installed and up-to-date.
#
class newrelic::servermon( $key = $::newrelic_key ) {
  # Add newrelic apt repo
  file { '/etc/apt/sources.list.d/newrelic.list':
    ensure => present,
    owner  => root,
    group  => root,
    mode   => '0644',
    source => 'puppet:///modules/newrelic/newrelic.list'
  }
  file { '/etc/apt/trusted.gpg.d/newrelic.gpg':
    ensure    => present,
    owner     => root,
    group     => root,
    mode      => '0644',
    source    => 'puppet:///modules/newrelic/newrelic.gpg',
    subscribe => File['/etc/apt/sources.list.d/newrelic.list'],
  }
  exec { 'newrelic-apt-refresh':
    command     => '/usr/bin/apt-get update',
    subscribe   => File['/etc/apt/trusted.gpg.d/newrelic.gpg'],
    refreshonly => true,
  }
  package { 'newrelic-sysmond':
    ensure    => latest,
    subscribe => Exec['newrelic-apt-refresh']
  }
  # Configuration
  file { '/etc/newrelic/nrsysmond.cfg':
    ensure  => present,
    owner   => root,
    group   => newrelic,
    mode    => '0640',
    content => template('newrelic/nrsysmond.cfg.tpl'),
    require => Package['newrelic-sysmond'],
  }
  service { 'newrelic-sysmond':
    ensure    => running,
    subscribe => File['/etc/newrelic/nrsysmond.cfg']
  }
}
