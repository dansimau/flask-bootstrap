class vagrant::pip {
    # Create pip.conf for vagrant
    file { '/home/vagrant/.pip':
        source  => 'puppet:///modules/vagrant/pip',
        recurse => remote,
    }
}
