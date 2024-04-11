try:
    from sys import _MEIPASS
except ImportError:
    _MEIPASS = None

from pathlib import Path
from .version import VERSION

__author__ = 'https://github.com/NotStatilko'
__maintainer__ = 'https://github.com/NotStatilko'
__email__ = 'thenonproton@pm.me'

__copyright__ = 'Copyright 2024, NotStatilko'
__license__ = 'MIT'

__version__ = VERSION


ABSPATH: Path = Path(_MEIPASS) if _MEIPASS is not None \
    else Path(__file__).parent

# Will be used for generating password fingerprint
# in the uiScrypt App Title (non-security thing)
SALT = bytes.fromhex('3e430bceacb85e6cfca2bf10d18c8f82')
