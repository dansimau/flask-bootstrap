#
# Ensure Fabric is installed.
#
# Fabric is used for app deployment.
#
class fabric {
  package { 'fabric':
    ensure   => 'present',
  }
}
