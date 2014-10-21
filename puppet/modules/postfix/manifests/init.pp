class postfix {
  package { 'postfix':
    ensure => installed,
  }
  service { 'postfix':
    ensure  => running,
    require => Package[postfix]
  }
}
