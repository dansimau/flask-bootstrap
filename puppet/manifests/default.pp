import 'config.pp'
import 'lib/*.pp'

# Import node config for different environments
import 'environments/*.pp'

#
# Defaults.
#
node default {
  include cssmin
  include fabric
  include git
  include nginx
  include openssl
  include postfix
  include postgresql
  include puppet::sudoers
  include python::packages
  include rsyslog
  include sysctl
  include uglifyjs

  # Set timezone to Europe/London
  file { '/etc/localtime':
    source => '/usr/share/zoneinfo/Europe/London',
    # Restart syslog so log times are correct
    notify => Service[rsyslog],
  }

  # Create postgresql roles for the app and deploy user
  postgresql::role { 'www-data':
    ensure => present,
  }
}


#
# Base class for externally hosted production nodes.
#
class site inherits default {
  include users::deploy

  # Firewall
  class { 'ferm':
    public_ports => [
      'http',
      'https',
    ],
  }

  # Newrelic server monitoring
  class { 'newrelic::servermon':
    key => '3c11e611ab565cd0936ed88137ba555ca1500dc0',
  }

  # Give deploy user access to create and update the database
  postgresql::role { $::deploy_user:
    ensure     => present,
    createdb   => true,        # This user creates the
    grant      => 'www-data',  # app database.
  }
}
