#
# For defining nginx sites.
#
define nginx::site(
  $auth = false,
  $app_path = $::app_path,
  $ssl_cert = '/etc/ssl/certs/ssl-cert-snakeoil.pem',
  $ssl_cert_key = '/etc/ssl/private/ssl-cert-snakeoil.key',
  $redirects = false)
{
  file { "/etc/nginx/sites-available/${name}":
    ensure  => present,
    owner   => root,
    group   => root,
    mode    => '0644',
    content => template("nginx/${name}.erb"),
    require => Package['nginx'],
    notify  => Service['nginx']
  }

  file { "/etc/nginx/sites-enabled/${name}":
    ensure => link,
    target => "/etc/nginx/sites-available/${name}",
    notify => Service['nginx']
  }

  if $auth {
    file {"/etc/nginx/htpasswd-${name}":
      ensure  => present,
      owner   => root,
      group   => root,
      mode    => '0644',
      content => template('nginx/auth.erb'),
      require => Package['nginx'],
    }
  }

  # Ensure SSL key is secured
  file { $ssl_cert_key:
    owner => root,
    group => 'ssl-cert',
    mode  => '0640',
  }
}
