#
# apt-update bootstrap
#
# Ubuntu vagrant boxes ship with US apt mirrors which are slow. Here
# we overwrite them with the UK ones prior to running an apt-get update.
#

include apt

class { 'apt::sources':
  mirror => 'http://gb.archive.ubuntu.com/ubuntu/',
}
