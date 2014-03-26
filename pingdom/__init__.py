# -*- coding: utf-8 -*-
"""

    pingdom.__init__

"""
from pkg_resources import get_distribution, DistributionNotFound

#
# Added support for surfacing the VERSION, __version__ attributes
# with the package installation.
#
# Ref: http://stackoverflow.com/questions/17583443/what-is-the-correct-way-to-share-package-version-with-setup-py-and-the-package
#
__project__ = 'pingdom'
__version__ = None  # required for initial installation

__author__ = 'Mike Babineau <michael.babineau@gmail.com>'
__copyright__ = "Copyright 2011 Electronic Arts Inc."
__license__ = "Apache v2.0"

try:
    __version__ = get_distribution(__project__).version
except DistributionNotFound:
    VERSION = __project__ + '-' + '(local)'
else:
    VERSION = __project__ + '-' + __version__

from pingdom.connection import (PingdomRequest, PingdomResponse,
                                 PingdomConnection)
from pingdom.exception import PingdomError
from pingdom.resources import PingdomCheck, PingdomContact
