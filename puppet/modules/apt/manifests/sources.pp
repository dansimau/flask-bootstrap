#
# Installs the default Ubuntu apt sources.
#
class apt::sources(
  $dist = 'trusty',
  $mirror = 'http://gb.archive.ubuntu.com/ubuntu/'
) {
  file { '/etc/apt/sources.list':
    content => template("apt/${dist}.list.tpl"),
    before  => Exec['apt-update'],
  }
}
