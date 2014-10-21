#
# Ensure syslog is installed and running.
#
# Also provides the rsyslog Puppet service resource primarily so it can be
# notified about system timezone changes (otherwise syslog timestamps are
# wrong).
#
class rsyslog {
  package { 'rsyslog':
    ensure => installed,
  }
  service { 'rsyslog':
    ensure => running,
  }
}
