#
# Standalone manifest - for dev Vagrant box.
#

import 'lib/*.pp'

include fabric
include git
include postgresql
include python
include vagrant
