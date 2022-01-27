__title__ = 'dbdd'
__author__ = 'BambiKu'
__license__ = 'MIT'
__copyright__ = 'Copyright BambiKu 2022C'
__version__ = '0.12'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import logging
from typing import *

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=2, minor=0, micro=0, releaselevel='alpha', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
