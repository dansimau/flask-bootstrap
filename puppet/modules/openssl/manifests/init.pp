#
# Ensures OpenSSL libraries are kept up-to-date.
#
# NOTE: This does not automatically restart services that rely on openssl.
# Services still need to be restarted manually to ensure the latest version of
# openssl is loaded.
#
class openssl {
  # Ensure openssl is latest.
  package { ['openssl', 'libssl1.0.0']:
    ensure => latest,
  }
}
