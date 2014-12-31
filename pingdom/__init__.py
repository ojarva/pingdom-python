# -*- coding: utf-8 -*-
"""

    pingdom.__init__
# Author: Mike Babineau <mikeb@ea2d.com>
# Copyright 2011 Electronic Arts Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__version__ = '0.1.3.5.dd.1'

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
