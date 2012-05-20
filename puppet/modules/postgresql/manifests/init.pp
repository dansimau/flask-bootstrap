class postgresql {
  # postgresql-dev required for Python's psycopg2
  package { [ 'postgresql', 'postgresql-server-dev-all' ]:
    ensure => 'installed',
  }
  service { 'postgresql':
    ensure  => running,
    require => Package[postgresql],
  }
}