#
# Ensure git is installed.
#
class git {
  package { 'git':
    ensure => installed,
  }
}
