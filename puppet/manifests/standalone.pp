#
# Standalone manifest - for dev Vagrant box.
#

import 'lib/*.pp'

include fabric
include git
include gunicorn
include nginx
include postgresql
include python
include sass
include uglifyjs
include vagrant

nginx::site { 'gunicorn':
  config => 'gunicorn',
}