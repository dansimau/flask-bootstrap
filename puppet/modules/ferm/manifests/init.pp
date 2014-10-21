class ferm {

    package { 'ferm':
        ensure => installed
    }

    file {
        '/etc/ferm/rules.d':
            ensure => directory,
            purge   => true,
            owner   => root,
            group   => root,
            force   => true,
            recurse => true,
            notify  => Service['ferm'],
            require => Package['ferm'];
        '/etc/ferm':
            ensure  => directory,
            owner   => root,
            group   => root,
            mode    => 0755;
        '/etc/ferm/conf.d':
            ensure  => directory,
            owner   => root,
            group   => root,
            require => Package['ferm'];
        '/etc/default/ferm':
            source  => 'puppet:///modules/ferm/ferm.default',
            owner   => root,
            group   => root,
            require => Package['ferm'],
            notify  => Service['ferm'];
        '/etc/ferm/ferm.conf':
            source  => 'puppet:///modules/ferm/ferm.conf',
            owner   => root,
            group   => root,
            require => Package['ferm'],
            mode    => 0400,
            notify  => Service['ferm'];
        '/etc/ferm/conf.d/defs.conf':
            content => template('ferm/defs.conf.erb'),
            owner   => root,
            group   => root,
            require => Package['ferm'],
            mode    => 0400,
            notify  => Service['ferm'];
    }

    service { 'ferm':
        ensure  => running,
        require => Package['ferm']
    }
}
