#
# Set up deploy user.
#
class users::deploy($deploy_user = $::deploy_user) {

  user { $deploy_user:
    ensure     => present,
    comment    => 'App deployment user',
    managehome => true,
    shell      => '/bin/bash',
  }

  # Grant sudo access
  file { "/etc/sudoers.d/${deploy_user}":
    owner   => root,
    group   => root,
    mode    => '0440',
    content => "${deploy_user} ALL = (root) NOPASSWD : ALL\n"
  }
}
