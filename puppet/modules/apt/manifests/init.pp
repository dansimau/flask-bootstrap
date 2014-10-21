#
# Ensure apt sources cache is up-to-date.
#
class apt {
  exec { 'apt-update':
    command => '/usr/bin/apt-get -qq update'
  }
}
