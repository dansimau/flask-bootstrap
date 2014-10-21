class sysctl {
  # This service is always stopped, but needs to be refreshed when a value
  # changes.
  exec { 'sysctl::reload':
    command     => '/etc/init.d/procps start',
    refreshonly => true,
  }
}

define sysctl::parameter ( $value ) {
  file { "/etc/sysctl.d/60-${name}.conf":
    ensure  => present,
    content => "${name} = ${value}\n",
    notify  => Exec['sysctl::reload'],
  }
}
