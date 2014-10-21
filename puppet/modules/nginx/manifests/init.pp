#
# Nginx
#
class nginx {
  include nginx::ssl

  package { 'nginx':
    ensure => installed,
  }
  # Disable default nginx site
  file { '/etc/nginx/sites-enabled/default':
    ensure => absent,
    before => Service[nginx]
  }
  service { 'nginx':
    ensure  => running,
    require => Exec['nginx:ssl::generate-dhparams'],
  }
}
