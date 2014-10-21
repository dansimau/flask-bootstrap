#
# Ensures the deploy user can run Puppet via sudo.
#
class puppet::sudoers (
  $app_path = $::app_path,
  $deploy_user = $::deploy_user
) {
  file { '/etc/sudoers.d/puppet':
    owner   => root,
    group   => root,
    mode    => '0440',
    content => "${deploy_user} ALL = (root) NOPASSWD : /usr/bin/puppet apply --modulepath='${app_path}/modules' '${app_path}/puppet/manifests/site.pp'\n",
  }
}
