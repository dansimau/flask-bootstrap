#
# Python packages required by the app.
#
class python::packages {
  package { [ 'python-virtualenv', 'python-dev', ]:
    ensure => installed
  }
}
