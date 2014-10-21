#
# Create vagrant postgresql user for development.
#
class vagrant::postgresql {
  postgresql::role { 'vagrant':
    ensure     => present,
    createdb   => true,
    createrole => true,
    superuser  => true,
  }
}
