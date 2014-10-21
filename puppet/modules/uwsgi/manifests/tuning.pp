#
# uWSGI system tuning
#
class uwsgi::tuning {
  # Increase system max socket queue
  sysctl::parameter { 'net.core.somaxconn':
    value => 2048,
  }
}
